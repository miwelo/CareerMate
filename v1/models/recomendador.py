from __future__ import annotations

from typing import Dict, List, Tuple

import numpy as np

from models.carreras import CARRERAS_OBJETIVO
from models.entrenamiento import FEATURE_COLUMNS


def construir_vector_usuario(respuestas: List[Tuple[int, int]]) -> np.ndarray:
    """Construye el vector de 27 features a partir de las respuestas.

    La idea es sumar los "pesos" definidos en ``models.preguntas.PREGUNTAS_BASE``
    para cada respuesta seleccionada.

    Pasos:
    1. Inicializar un diccionario ``perfil`` con valores base apropiados:
       - Features técnicas (habilidades): valor base de 2.0
       - Features de personalidad: valor base de 0.15 
       (según los datos del CSV)
    2. Por cada respuesta (id_pregunta, idx_opcion):
       - Recuperar la pregunta.
       - Obtener la opción seleccionada y su diccionario de ``pesos``.
       - Sumar cada peso a la feature correspondiente en ``perfil``.
    3. Generar un vector NumPy ordenado según ``FEATURE_COLUMNS``.
    """
    from models.preguntas import obtener_pregunta

    # Features de personalidad (valores bajos en el dataset ~0.1-0.7)
    personality_features = {
        "Openness", "Conscientousness", "Extraversion", "Agreeableness",
        "Emotional_Range", "Conversation", "Openness to Change",
        "Hedonism", "Self-enhancement", "Self-transcendence"
    }

    # Inicializar con valores base apropiados
    perfil: Dict[str, float] = {}
    for col in FEATURE_COLUMNS:
        if col in personality_features:
            perfil[col] = 0.15  # Valor base bajo para rasgos de personalidad
        else:
            perfil[col] = 2.0   # Valor base normal para habilidades técnicas

    for idx_pregunta, idx_opcion in respuestas:
        pregunta = obtener_pregunta(idx_pregunta)
        if not pregunta:
            continue

        opciones = pregunta.get("opciones", [])
        if not (0 <= idx_opcion < len(opciones)):
            continue

        opcion = opciones[idx_opcion]
        pesos: Dict[str, float] = opcion.get("pesos", {})  # type: ignore[assignment]

        for feature_name, delta in pesos.items():
            if feature_name in perfil:
                perfil[feature_name] += float(delta)

    # Construimos el vector en el orden correcto de columnas
    vector = np.array([perfil[col] for col in FEATURE_COLUMNS], dtype=float)
    return vector.reshape(1, -1)


def recomendar_carreras(respuestas: List[Tuple[int, int]], top: int = 1):
    """Recomienda la carrera más cercana por distancia euclidiana."""
    from models.carreras import DESCRIPCIONES, obtener_imagen_carrera
    from models.entrenamiento import cargar_datos, TARGET_COLUMN
    from sklearn.metrics.pairwise import euclidean_distances

    if not respuestas:
        return []

    # Construir vector del usuario
    vector_usuario = construir_vector_usuario(respuestas)
    
    # Cargar datos de entrenamiento
    df = cargar_datos()
    
    # Obtener vectores de cada carrera
    X = df[FEATURE_COLUMNS].values
    y = df[TARGET_COLUMN].values
    
    # Calcular distancias euclidianas
    distancias = euclidean_distances(vector_usuario, X)[0]
    
    # Crear mapeo de carrera a mejor distancia (puede haber duplicados en dataset)
    carrera_distancias = {}
    for carrera, distancia in zip(y, distancias):
        if carrera not in carrera_distancias or distancia < carrera_distancias[carrera]:
            carrera_distancias[carrera] = distancia
    
    # Convertir distancias a "compatibilidad" (0-100%)
    # Distancia 0 = 100%, distancia alta = 0%
    # Usamos una función exponencial decreciente para el mapeo
    max_distancia = max(carrera_distancias.values()) if carrera_distancias else 1.0
    
    resultados = []
    for carrera, distancia in carrera_distancias.items():
        # Convertir distancia a compatibilidad
        # Mientras más cerca (menor distancia), mayor compatibilidad
        if max_distancia > 0:
            compatibilidad_normalizada = 1.0 - (distancia / (max_distancia * 1.5))
            compatibilidad_normalizada = max(0.0, min(1.0, compatibilidad_normalizada))
        else:
            compatibilidad_normalizada = 1.0
        
        compatibilidad = int(round(compatibilidad_normalizada * 100))
        
        resultado = {
            "carrera": carrera,
            "compatibilidad": compatibilidad,
            "descripcion": DESCRIPCIONES.get(carrera, "Sin descripción disponible."),
            "imagen": obtener_imagen_carrera(carrera),
            "indice": CARRERAS_OBJETIVO.index(carrera) if carrera in CARRERAS_OBJETIVO else -1,
            "probabilidad": compatibilidad_normalizada,
            "distancia": float(distancia),
        }
        resultados.append(resultado)
    
    # Ordenar por distancia (menor = mejor) y tomar top
    resultados.sort(key=lambda x: x["distancia"])
    return resultados[:top]

def calcular_estadisticas(historial):
    """
    Calcula estadísticas del historial de tests.
    
    Args:
        historial: Lista de tests completados
    
    Returns:
        Diccionario con estadísticas
    """
    if not historial:
        return {
            "total_tests": 0,
            "compatibilidad_promedio": 0,
            "carrera_popular": None,
            "tasa_completacion": 0,
            "por_carrera": {}
        }
    
    total_tests = len(historial)
    compatibilidad_total = 0
    conteo_carreras = {carrera: 0 for carrera in CARRERAS_OBJETIVO}
    compatibilidad_carrera = {carrera: [] for carrera in CARRERAS_OBJETIVO}
    
    for test in historial:
        for i, carrera in enumerate(test['carreras']):
            compatibilidad = test['compatibilidades'][i]
            conteo_carreras[carrera] += 1
            compatibilidad_carrera[carrera].append(compatibilidad)
            compatibilidad_total += compatibilidad
    
    compatibilidad_promedio = int(compatibilidad_total / (total_tests * 2)) if total_tests > 0 else 0
    carrera_popular = max(conteo_carreras.items(), key=lambda item: item[1])[0] if conteo_carreras else None
    
    # Calcular promedio por carrera
    por_carrera = {}
    for carrera, compatibilidades in compatibilidad_carrera.items():
        if compatibilidades:
            por_carrera[carrera] = {
                "count": conteo_carreras[carrera],
                "promedio": int(sum(compatibilidades) / len(compatibilidades))
            }
        else:
            por_carrera[carrera] = {"count": 0, "promedio": 0}
    
    return {
        "total_tests": total_tests,
        "compatibilidad_promedio": compatibilidad_promedio,
        "carrera_popular": carrera_popular,
        "tasa_completacion": 100,
        "por_carrera": por_carrera
    }
