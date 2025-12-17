import json
import os
from datetime import datetime

HISTORIAL_FILE = "historial.json"
ESTADISTICAS_FILE = "estadisticas.json"


def guardar_historial(historial):
    try:
        with open(HISTORIAL_FILE, 'w', encoding='utf-8') as file:
            json.dump(historial, file, ensure_ascii=False, indent=2)
        return True
    except Exception:
        return False


def cargar_historial():
    try:
        if os.path.exists(HISTORIAL_FILE):
            with open(HISTORIAL_FILE, 'r', encoding='utf-8') as file:
                return json.load(file)
    except Exception:
        pass
    return []


def agregar_al_historial(historial, carreras, compatibilidades):
    nuevo_test = {
        "fecha": datetime.now().isoformat(),
        "carreras": carreras,
        "compatibilidades": compatibilidades,
    }
    historial.append(nuevo_test)
    guardar_historial(historial)
    return historial


def limpiar_historial():
    guardar_historial([])
    return []


def guardar_estadisticas(estadisticas):
    try:
        with open(ESTADISTICAS_FILE, 'w', encoding='utf-8') as file:
            json.dump(estadisticas, file, ensure_ascii=False, indent=2)
        return True
    except Exception:
        return False


def cargar_estadisticas():
    try:
        if os.path.exists(ESTADISTICAS_FILE):
            with open(ESTADISTICAS_FILE, 'r', encoding='utf-8') as file:
                return json.load(file)
    except Exception:
        pass
    return {}
