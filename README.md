# CareerMate
Sistema de recomendación vocacional tecnológica basado en un enfoque híbrido:
**Machine Learning + lógica de dominio profesional**.

CareerMate no es un clasificador académico, sino un recomendador coherente y explicable,
diseñado para orientar perfiles técnicos reales hacia carreras tecnológicas compatibles
con sus habilidades, intereses y rasgos personales.

---

## 🎯 Objetivo del proyecto

Orientar a usuarios hacia **carreras tecnológicas coherentes** a partir de:
- habilidades técnicas
- competencias blandas
- patrones de especialización
- requisitos profesionales reales

El sistema prioriza la **coherencia humana** sobre la maximización ciega de probabilidad.

---

## 🧠 Enfoque general

CareerMate utiliza un **pipeline híbrido**:

- **Machine Learning** para ranking probabilístico
- **Reglas explícitas de dominio** para validación semántica

Este enfoque evita recomendaciones lógicamente incompatibles
(ej. *Database Administrator* sin bases de datos).

---

## 🧩 Arquitectura del sistema

1. Respuesta al cuestionario (18 técnicas + 12 blandas)
2. Construcción del vector de usuario (27 features)
3. Normalización y análisis de dominancia técnica
4. Clasificación de macro-perfil profesional
5. Filtrado lógico pre-ML de carreras incompatibles
6. Ranking probabilístico con modelo ML
7. **Validación dura por requisitos técnicos mínimos**
8. Presentación de resultados finales

---

## 📊 Cuestionario

### Preguntas técnicas (18)
Evalúan competencias específicas en áreas como:
- programación
- bases de datos
- redes
- ciberseguridad
- ciencia de datos
- ingeniería de software
- troubleshooting
- diseño gráfico (como skill explícito)

Cada pregunta impacta **una sola feature técnica** para evitar ruido y colinealidad.

---

### Preguntas blandas (12)
Basadas en:
- Big Five
- valores motivacionales
- comunicación y estilo de trabajo

Se usan para:
- modular el perfil
- detectar generalismo vs especialización
- evitar sesgos técnicos extremos

---

## 📐 Vector de usuario

- Dimensión: **27 features**
- Rango típico por feature: **~1.5 – 2.2**
- Desviación estándar saludable: **0.55 – 0.60**

Un `std` estable indica señal suficiente sin ruido excesivo.

---

## 🤖 Modelo de Machine Learning

- Algoritmo: `SGDClassifier`
- Tipo: clasificación multiclase
- Rol: **ranking de carreras**
- Entrenamiento: previo

El modelo **no decide validez profesional**,
solo ordena probabilidades entre carreras permitidas.

---

## 🧠 Lógica de dominio (clave del proyecto)

### 1️⃣ Macro-perfiles profesionales
El sistema clasifica al usuario en uno de los siguientes macro-perfiles:

- Técnico analítico (AI/ML, Data Science, Cyber)
- Técnico operativo (Software, Networking, Systems)
- Creativo
- Soporte / gestión

Esto reduce ruido y evita colisiones semánticas.

---

### 2️⃣ Dominancia técnica
Se mide la especialización técnica vs rasgos blandos.

- Dominancia alta → se penalizan carreras generalistas
- Dominancia baja → se permiten opciones híbridas

---

### 3️⃣ Requisitos mínimos no compensables
Algunas habilidades son **habilitadoras obligatorias**.

Ejemplos:
- Database Administrator → Database Fundamentals
- AI/ML Specialist → AI ML + Programming
- Cyber Security Specialist → Cyber Security + Networking

Si una feature crítica no alcanza el umbral:
→ la carrera se excluye **aunque el ML la rankee alto**.

Esta capa cierra la coherencia del sistema.

---

## 🧪 Validación y testing

El proyecto incluye tests sintéticos para:

- estabilidad del vector
- coherencia entre ejes profesionales
- exclusión de carreras incompatibles
- validación de perfiles extremos

Archivos relevantes:
- `tests/test_vectores_sinteticos.py`
- `tests/test_ejes_profesionales.py`

---

## 🧰 Tecnologías utilizadas

- **Python 3**
- **NumPy** – operaciones vectoriales
- **scikit-learn** – modelo ML
- **CSV / pandas** – datos de carreras
- **pytest** – testing
- Arquitectura modular orientada a producto

---

## 📁 Estructura del proyecto

CareerMate/
│
├── app.py
│
├── models/
│ ├── recomendador.py
│ ├── modelo_ml.py
│ ├── preguntas.py
│ ├── carreras.py
│ └── entrenamiento.py
│
├── utils/
│ └── storage.py
│
├── tests/
│ ├── test_vectores_sinteticos.py
│ └── test_ejes_profesionales.py
│
├── CareerMap.csv
├── README.md
└── CHANGELOG.md


---

## 🚫 Qué NO hace CareerMate

- No promete precisión del 100%
- No reemplaza orientación profesional humana
- No fuerza recomendaciones incompatibles
- No toma decisiones opacas

---

## 🏁 Estado del proyecto

- Versión: **v2.0.0**
- Estado: **Stable / Production Ready**
- Desarrollo funcional: **cerrado**

Las mejoras futuras se enfocan en:
- UX
- tests adaptativos
- despliegue como servicio

---

## 📌 Conclusión

CareerMate demuestra que:
- el ML debe estar subordinado a la lógica de dominio
- la coherencia humana es prioritaria sobre métricas abstractas
- los sistemas de recomendación reales son híbridos por diseño

Este proyecto está pensado para uso real,
no como demo académica.

---

## 📄 Licencia
[LICENSE](LICENSE)
