PREGUNTAS_BASE = [
    {
        "id": 0,
        "texto": "¿Qué tipo de reto te motiva más?",
        "opciones": [
            {"texto": "Optimizar algoritmos que aprendan de datos", "pesos": {"AI ML": 0.25, "Programming Skills": 0.10, "Openness": 0.05}},
            {"texto": "Encontrar patrones y explicar hallazgos", "pesos": {"Data Science": 0.25, "Business Analysis": 0.10, "Conscientousness": 0.05}},
            {"texto": "Cerrar brechas de seguridad y vulnerabilidades", "pesos": {"Cyber Security": 0.25, "Computer Forensics Fundamentals": 0.10, "Emotional_Range": 0.05}},
        ],
    },
    {
        "id": 1,
        "texto": "¿Dónde te sientes más cómodo construyendo?",
        "opciones": [
            {"texto": "Infraestructura distribuida y escalable", "pesos": {"Distributed Computing Systems": 0.25, "Networking": 0.10, "Computer Architecture": 0.05}},
            {"texto": "Pipelines de despliegue y automatización", "pesos": {"Software Engineering": 0.25, "Project Management": 0.10, "Troubleshooting skills": 0.05}},
            {"texto": "Aplicaciones de punta a punta (frontend y backend)", "pesos": {"Software Development": 0.25, "Programming Skills": 0.10, "Technical Communication": 0.05}},
        ],
    },
    {
        "id": 2,
        "texto": "¿Qué tipo de producto te atrae más?",
        "opciones": [
            {"texto": "Sistemas descentralizados y seguros", "pesos": {"Distributed Computing Systems": 0.15, "Cyber Security": 0.20, "Programming Skills": 0.10, "Database Fundamentals": 0.05}},
            {"texto": "Experiencias visuales claras y accesibles", "pesos": {"Graphics Designing": 0.25, "Communication skills": 0.10, "Agreeableness": 0.05}},
            {"texto": "Decisiones estratégicas basadas en negocio", "pesos": {"Project Management": 0.20, "Business Analysis": 0.20, "Conversation": 0.10}},
        ],
    },
    {
        "id": 3,
        "texto": "¿Cómo abordas un diagnóstico rápido?",
        "opciones": [
            {"texto": "Reviso conexiones, latencias y estado de red", "pesos": {"Networking": 0.25, "Troubleshooting skills": 0.15, "Computer Architecture": 0.05}},
            {"texto": "Analizo datos y métricas para ver tendencias", "pesos": {"Data Science": 0.20, "Business Analysis": 0.15, "Conscientousness": 0.05}},
            {"texto": "Depuro el código y busco errores lógicos", "pesos": {"Programming Skills": 0.20, "Software Engineering": 0.15, "Software Development": 0.10}},
        ],
    },
    {
        "id": 4,
        "texto": "¿Qué tema te gustaría investigar más?",
        "opciones": [
            {"texto": "Modelos predictivos y aprendizaje profundo", "pesos": {"AI ML": 0.25, "Programming Skills": 0.10, "Openness": 0.05}},
            {"texto": "Análisis de mercado y comportamiento de usuarios", "pesos": {"Business Analysis": 0.20, "Data Science": 0.15, "Openness to Change": 0.05}},
            {"texto": "Técnicas avanzadas de defensa digital", "pesos": {"Cyber Security": 0.25, "Computer Forensics Fundamentals": 0.10, "Networking": 0.05}},
        ],
    },
    {
        "id": 5,
        "texto": "¿Cómo prefieres aprender algo nuevo?",
        "opciones": [
            {"texto": "Prototipos rápidos de código y pruebas A/B", "pesos": {"Software Development": 0.20, "Programming Skills": 0.15, "Openness": 0.05}},
            {"texto": "Diagramas de arquitectura y flujos de datos", "pesos": {"Distributed Computing Systems": 0.20, "Database Fundamentals": 0.15, "Computer Architecture": 0.05}},
            {"texto": "Casos de uso con usuarios reales y feedback", "pesos": {"Communication skills": 0.20, "Technical Communication": 0.10, "Agreeableness": 0.05}},
        ],
    },
    {
        "id": 6,
        "texto": "¿Qué priorizas al diseñar una solución?",
        "opciones": [
            {"texto": "Precisión y rendimiento del modelo", "pesos": {"AI ML": 0.25, "Software Engineering": 0.10, "Programming Skills": 0.05}},
            {"texto": "Claridad de los datos y trazabilidad", "pesos": {"Data Science": 0.20, "Database Fundamentals": 0.15, "Conscientousness": 0.05}},
            {"texto": "Seguridad y control de accesos", "pesos": {"Cyber Security": 0.25, "Networking": 0.10, "Emotional_Range": 0.05}},
        ],
    },
    {
        "id": 7,
        "texto": "¿Qué problema cotidiano te parece más interesante?",
        "opciones": [
            {"texto": "Reducir la latencia y caídas de servicio", "pesos": {"Networking": 0.25, "Distributed Computing Systems": 0.10, "Troubleshooting skills": 0.10}},
            {"texto": "Automatizar despliegues para evitar tareas manuales", "pesos": {"Software Engineering": 0.20, "Project Management": 0.15, "Troubleshooting skills": 0.05}},
            {"texto": "Mejorar la experiencia visual y de uso", "pesos": {"Graphics Designing": 0.25, "Communication skills": 0.10, "Agreeableness": 0.05}},
        ],
    },
    {
        "id": 8,
        "texto": "¿Qué herramienta te llama más la atención?",
        "opciones": [
            {"texto": "Orquestadores de contenedores y escalado", "pesos": {"Distributed Computing Systems": 0.20, "Networking": 0.15, "Troubleshooting skills": 0.05}},
            {"texto": "Frameworks de interfaz y componentes reutilizables", "pesos": {"Software Development": 0.20, "Graphics Designing": 0.15, "Technical Communication": 0.05}},
            {"texto": "Plataformas de BI y cuadros de mando", "pesos": {"Business Analysis": 0.20, "Data Science": 0.15, "Conversation": 0.05}},
        ],
    },
    {
        "id": 9,
        "texto": "¿Qué te motiva a terminar un proyecto?",
        "opciones": [
            {"texto": "Automatizar y simplificar procesos repetitivos", "pesos": {"AI ML": 0.20, "Software Engineering": 0.15, "Openness to Change": 0.05}},
            {"texto": "Ver que los usuarios entienden y disfrutan la interfaz", "pesos": {"Communication skills": 0.20, "Graphics Designing": 0.15, "Agreeableness": 0.05}},
            {"texto": "Mantener el servicio disponible sin incidentes", "pesos": {"Distributed Computing Systems": 0.20, "Networking": 0.15, "Troubleshooting skills": 0.05}},
        ],
    },
    {
        "id": 10,
        "texto": "¿Qué rol disfrutas más dentro de un equipo?",
        "opciones": [
            {"texto": "Explorar y probar nuevas técnicas de modelado", "pesos": {"AI ML": 0.25, "Programming Skills": 0.10, "Openness": 0.05}},
            {"texto": "Analizar información para tomar decisiones", "pesos": {"Business Analysis": 0.25, "Data Science": 0.10, "Conscientousness": 0.05}},
            {"texto": "Actuar como primer filtro de seguridad", "pesos": {"Cyber Security": 0.25, "Computer Forensics Fundamentals": 0.10, "Networking": 0.05}},
        ],
    },
    {
        "id": 11,
        "texto": "¿Qué tipo de proyecto te gustaría liderar?",
        "opciones": [
            {"texto": "Integraciones y microservicios bien acoplados", "pesos": {"Distributed Computing Systems": 0.20, "Computer Architecture": 0.15, "Software Engineering": 0.05}},
            {"texto": "Pipelines de integración y entrega continua", "pesos": {"Software Engineering": 0.20, "Project Management": 0.15, "Troubleshooting skills": 0.05}},
            {"texto": "Aplicación web completa con buen performance", "pesos": {"Software Development": 0.20, "Programming Skills": 0.15, "Graphics Designing": 0.05}},
        ],
    },
    {
        "id": 12,
        "texto": "¿En qué habilidad sientes que destacas?",
        "opciones": [
            {"texto": "Visualizar y maquetar interfaces claras", "pesos": {"Graphics Designing": 0.25, "Communication skills": 0.10, "Technical Communication": 0.05}},
            {"texto": "Alinear objetivos y negociar entregables", "pesos": {"Project Management": 0.20, "Business Analysis": 0.15, "Conversation": 0.05}},
            {"texto": "Resolver incidentes de red y hardware", "pesos": {"Networking": 0.25, "Troubleshooting skills": 0.15, "Computer Architecture": 0.05}},
        ],
    },
    {
        "id": 13,
        "texto": "¿Qué indicador de éxito te importa más?",
        "opciones": [
            {"texto": "Precisión y mejora continua del modelo", "pesos": {"AI ML": 0.20, "Software Engineering": 0.15, "Programming Skills": 0.05}},
            {"texto": "Impacto en ingresos o conversiones", "pesos": {"Business Analysis": 0.20, "Project Management": 0.15, "Self-enhancement": 0.05}},
            {"texto": "Cero incidentes críticos y brechas", "pesos": {"Cyber Security": 0.20, "Networking": 0.15, "Troubleshooting skills": 0.05}},
        ],
    },
    {
        "id": 14,
        "texto": "¿Qué tema técnico te gustaría certificar?",
        "opciones": [
            {"texto": "Arquitectura y servicios en la nube", "pesos": {"Distributed Computing Systems": 0.20, "Database Fundamentals": 0.10, "Openness to Change": 0.05}},
            {"texto": "Analítica y visualización de datos", "pesos": {"Data Science": 0.20, "Business Analysis": 0.15, "Conscientousness": 0.05}},
            {"texto": "Seguridad ofensiva y defensiva", "pesos": {"Cyber Security": 0.25, "Computer Forensics Fundamentals": 0.10, "Emotional_Range": 0.05}},
        ],
    },
    {
        "id": 15,
        "texto": "¿Qué te frustra más en un proyecto?",
        "opciones": [
            {"texto": "Datos incompletos o desordenados", "pesos": {"Data Science": 0.20, "Database Fundamentals": 0.15, "Conscientousness": 0.05}},
            {"texto": "Procesos manuales de build/deploy", "pesos": {"Software Engineering": 0.20, "Project Management": 0.15, "Troubleshooting skills": 0.05}},
            {"texto": "Interfaces confusas para el usuario", "pesos": {"Graphics Designing": 0.20, "Communication skills": 0.15, "Agreeableness": 0.05}},
        ],
    },
    {
        "id": 16,
        "texto": "¿Qué prefieres documentar?",
        "opciones": [
            {"texto": "APIs limpias y ejemplos de código", "pesos": {"Programming Skills": 0.20, "Software Development": 0.15, "Technical Communication": 0.05}},
            {"texto": "Decisiones de producto y métricas clave", "pesos": {"Project Management": 0.20, "Business Analysis": 0.15, "Conversation": 0.05}},
            {"texto": "Políticas de acceso y respuesta a incidentes", "pesos": {"Cyber Security": 0.20, "Networking": 0.15, "Conscientousness": 0.05}},
        ],
    },
    {
        "id": 17,
        "texto": "¿Cómo te gusta colaborar?",
        "opciones": [
            {"texto": "Sprints de automatización y calidad técnica", "pesos": {"Software Engineering": 0.20, "Project Management": 0.15, "Troubleshooting skills": 0.05}},
            {"texto": "Sesiones de diseño y pruebas con usuarios", "pesos": {"Graphics Designing": 0.20, "Communication skills": 0.15, "Agreeableness": 0.05}},
            {"texto": "War rooms para contener incidentes", "pesos": {"Cyber Security": 0.20, "Computer Forensics Fundamentals": 0.10, "Emotional_Range": 0.05}},
        ],
    },
    {
        "id": 18,
        "texto": "¿Qué sueles medir primero?",
        "opciones": [
            {"texto": "Latencia, disponibilidad y uso de recursos", "pesos": {"Networking": 0.20, "Distributed Computing Systems": 0.15, "Troubleshooting skills": 0.05}},
            {"texto": "Conversión, retención y satisfacción de usuarios", "pesos": {"Business Analysis": 0.20, "Communication skills": 0.10, "Self-enhancement": 0.05}},
            {"texto": "Precisión y recall de modelos", "pesos": {"AI ML": 0.20, "Data Science": 0.15, "Conscientousness": 0.05}},
        ],
    },
    {
        "id": 19,
        "texto": "¿Qué reto creativo prefieres?",
        "opciones": [
            {"texto": "Prototipos rápidos para validar ideas", "pesos": {"Software Development": 0.20, "Graphics Designing": 0.15, "Openness": 0.05}},
            {"texto": "Nuevos enfoques de IA para un problema", "pesos": {"AI ML": 0.20, "Programming Skills": 0.15, "Openness": 0.05}},
            {"texto": "Dashboards accionables que cuenten historias", "pesos": {"Data Science": 0.20, "Business Analysis": 0.15, "Conversation": 0.05}},
        ],
    },
    {
        "id": 20,
        "texto": "¿Con qué stack te sientes más identificado?",
        "opciones": [
            {"texto": "Python y librerías de ciencia de datos", "pesos": {"Data Science": 0.20, "AI ML": 0.15, "Programming Skills": 0.10}},
            {"texto": "JavaScript/TypeScript para frontend y backend", "pesos": {"Software Development": 0.20, "Programming Skills": 0.15, "Technical Communication": 0.05}},
            {"texto": "Infraestructura como código y scripts de automatización", "pesos": {"Software Engineering": 0.20, "Distributed Computing Systems": 0.15, "Troubleshooting skills": 0.05}},
        ],
    },
    {
        "id": 21,
        "texto": "¿Cómo abordarías un sistema que debe escalar?",
        "opciones": [
            {"texto": "Particionando datos y optimizando consultas", "pesos": {"Database Fundamentals": 0.20, "Data Science": 0.15, "Conscientousness": 0.05}},
            {"texto": "Balanceando tráfico y replicando servicios", "pesos": {"Distributed Computing Systems": 0.20, "Networking": 0.15, "Computer Architecture": 0.05}},
            {"texto": "Separando responsabilidades en frontend/backend", "pesos": {"Software Development": 0.20, "Software Engineering": 0.15, "Technical Communication": 0.05}},
        ],
    },
    {
        "id": 22,
        "texto": "¿Qué riesgo te parece más crítico?",
        "opciones": [
            {"texto": "Brechas de seguridad y fuga de datos", "pesos": {"Cyber Security": 0.25, "Computer Forensics Fundamentals": 0.10, "Networking": 0.05}},
            {"texto": "Decisiones sin evidencia ni métricas", "pesos": {"Business Analysis": 0.20, "Data Science": 0.15, "Conscientousness": 0.05}},
            {"texto": "Deuda técnica en pipelines y despliegues", "pesos": {"Software Engineering": 0.20, "Project Management": 0.15, "Troubleshooting skills": 0.05}},
        ],
    },
    {
        "id": 23,
        "texto": "¿Qué logro te hace sentir orgulloso?",
        "opciones": [
            {"texto": "Contar una historia clara con datos", "pesos": {"Data Science": 0.20, "Business Analysis": 0.15, "Communication skills": 0.10}},
            {"texto": "Mejorar tiempos de respuesta y estabilidad", "pesos": {"Networking": 0.20, "Distributed Computing Systems": 0.15, "Troubleshooting skills": 0.05}},
            {"texto": "Crear una experiencia fluida y simple", "pesos": {"Graphics Designing": 0.20, "Communication skills": 0.10, "Agreeableness": 0.05}},
        ],
    },
    {
        "id": 24,
        "texto": "¿Dónde pasas más tiempo al resolver?",
        "opciones": [
            {"texto": "Tuning de consultas y calidad de datos", "pesos": {"Database Fundamentals": 0.20, "Data Science": 0.15, "Conscientousness": 0.05}},
            {"texto": "Monitoreo de logs, alertas y vulnerabilidades", "pesos": {"Cyber Security": 0.20, "Computer Forensics Fundamentals": 0.10, "Emotional_Range": 0.05}},
            {"texto": "Refinando componentes y microcopys", "pesos": {"Graphics Designing": 0.20, "Communication skills": 0.10, "Technical Communication": 0.05}},
        ],
    },
    {
        "id": 25,
        "texto": "¿Qué te inspira a seguir aprendiendo?",
        "opciones": [
            {"texto": "Resolver bugs difíciles y optimizar código", "pesos": {"Programming Skills": 0.20, "Software Development": 0.15, "Troubleshooting skills": 0.05}},
            {"texto": "Ver cómo un dashboard ayuda a decidir", "pesos": {"Business Analysis": 0.20, "Data Science": 0.15, "Conversation": 0.05}},
            {"texto": "Construir infraestructura resiliente", "pesos": {"Distributed Computing Systems": 0.20, "Networking": 0.15, "Computer Architecture": 0.05}},
        ],
    },
    {
        "id": 26,
        "texto": "¿Cómo prefieres aprender una tecnología nueva?",
        "opciones": [
            {"texto": "Papers y prototipos de modelos", "pesos": {"AI ML": 0.20, "Programming Skills": 0.15, "Openness": 0.05}},
            {"texto": "Cursos de visualización y storytelling", "pesos": {"Graphics Designing": 0.20, "Communication skills": 0.10, "Openness": 0.05}},
            {"texto": "Laboratorios de seguridad y retos prácticos", "pesos": {"Cyber Security": 0.20, "Computer Forensics Fundamentals": 0.10, "Networking": 0.05}},
        ],
    },
    {
        "id": 27,
        "texto": "Si tuvieras que elegir un trade-off, prefieres...",
        "opciones": [
            {"texto": "Lanzar rápido aunque el modelo mejore después", "pesos": {"AI ML": 0.15, "Software Engineering": 0.15, "Openness to Change": 0.05}},
            {"texto": "Asegurar datos limpios antes de cualquier entrega", "pesos": {"Data Science": 0.15, "Database Fundamentals": 0.15, "Conscientousness": 0.05}},
            {"texto": "No ceder seguridad aunque retrase el release", "pesos": {"Cyber Security": 0.20, "Networking": 0.10, "Emotional_Range": 0.05}},
        ],
    },
    {
        "id": 28,
        "texto": "¿Qué feedback valoras más?",
        "opciones": [
            {"texto": "Usuarios finales diciendo que lo entienden", "pesos": {"Communication skills": 0.20, "Graphics Designing": 0.15, "Agreeableness": 0.05}},
            {"texto": "Equipo de infraestructura reportando estabilidad", "pesos": {"Distributed Computing Systems": 0.20, "Networking": 0.15, "Troubleshooting skills": 0.05}},
            {"texto": "Datos de rendimiento que validen el modelo", "pesos": {"AI ML": 0.15, "Data Science": 0.15, "Software Engineering": 0.05}},
        ],
    },
    {
        "id": 29,
        "texto": "Pensando en tu futuro, ¿qué te entusiasma más?",
        "opciones": [
            {"texto": "IA generativa y nuevos enfoques de aprendizaje", "pesos": {"AI ML": 0.20, "Openness": 0.10, "Programming Skills": 0.10}},
            {"texto": "Analítica en tiempo real y datos en streaming", "pesos": {"Data Science": 0.20, "Distributed Computing Systems": 0.10, "Database Fundamentals": 0.10}},
            {"texto": "Redes confiables, edge y seguridad avanzada", "pesos": {"Networking": 0.20, "Cyber Security": 0.15, "Computer Architecture": 0.05}},
        ],
    },
]

def obtener_pregunta(indice):
    """Obtiene una pregunta por índice"""
    if 0 <= indice < len(PREGUNTAS_BASE):
        return PREGUNTAS_BASE[indice]
    return None

def obtener_todas_preguntas():
    """Retorna todas las preguntas"""
    return PREGUNTAS_BASE

def contar_preguntas():
    """Retorna el total de preguntas"""
    return len(PREGUNTAS_BASE)
