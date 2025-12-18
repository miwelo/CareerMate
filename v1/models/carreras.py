CARRERAS_OBJETIVO = [
    "Artificial Intelligence (AI)",
    "Data analysts and scientists",
    "Cybersecurity analyst",
    "Cloud engineers",
    "DevOps engineers",
    "Full stack developers",
    "Blockchain engineers",
    "UX/UI Product Designers",
    "Product Managers",
    "Network and Systems Administrators"
]

DESCRIPCIONES = {
    "Artificial Intelligence (AI)": "Especialista en crear sistemas que aprenden y piensan como humanos. Trabajarás con máquinas inteligentes, algoritmos avanzados y soluciones futuristas.",
    "Data analysts and scientists": "Experto en buscar patrones ocultos en datos. Convierten números en decisiones inteligentes y descubren historias que los datos cuentan.",
    "Cybersecurity analyst": "Guardián digital. Proteges información valiosa, identificas amenazas y defensas sistemas contra ataques maliciosos.",
    "Cloud engineers": "Constructor de infraestructuras en la nube. Diseñas sistemas escalables que permiten que aplicaciones funcionen en cualquier lugar del mundo.",
    "DevOps engineers": "Conecta desarrollo y operaciones. Automatizas procesos, despliegas código y aseguras que todo funcione sin interrupciones.",
    "Full stack developers": "Creador completo de aplicaciones. Trabajas en el frontend (lo que ves), backend (lo invisible) y todo lo necesario para que funcione.",
    "Blockchain engineers": "Arquitecto de tecnología descentralizada. Construyes sistemas seguros de transacciones y dinero digital que no necesitan intermediarios.",
    "UX/UI Product Designers": "Creador de experiencias. Diseñas interfaces bonitas e intuitivas que hacen que las aplicaciones sean fáciles y agradables de usar.",
    "Product Managers": "Visionario del producto. Diriges equipos, defines estrategias y aseguras que los productos resuelvan problemas reales.",
    "Network and Systems Administrators": "Guardián de la infraestructura. Mantienes redes, servidores y sistemas funcionando perfectamente 24/7."
}

IMAGENES_CARRERA = {
    "artificial intelligence": "https://images.unsplash.com/photo-1504384308090-c894fdcc538d?auto=format&fit=crop&w=800&q=60",
    "data": "https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?auto=format&fit=crop&w=800&q=60",
    "cybersecurity": "https://images.unsplash.com/photo-1510511459019-5dda7724fd87?auto=format&fit=crop&w=800&q=60",
    "cloud": "https://images.unsplash.com/photo-1493217465235-252dd9c0d632?auto=format&fit=crop&w=800&q=60",
    "devops": "https://images.unsplash.com/photo-1504639725590-34d0984388bd?auto=format&fit=crop&w=800&q=60",
    "full stack": "https://images.unsplash.com/photo-1523473827534-86c5af6d520a?auto=format&fit=crop&w=800&q=60",
    "blockchain": "https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=800&q=60",
    "ux": "https://images.unsplash.com/photo-1561070791-2526d30994b5?auto=format&fit=crop&w=800&q=60",
    "product": "https://images.unsplash.com/photo-1552664730-d307ca884978?auto=format&fit=crop&w=800&q=60",
    "network": "https://images.unsplash.com/photo-1582719478248-7e0ec3965d92?auto=format&fit=crop&w=800&q=60",
}

def obtener_imagen_carrera(carrera_nombre):
    """Obtiene la URL de imagen para una carrera"""
    key = carrera_nombre.strip().lower()
    for palabra_clave, url in IMAGENES_CARRERA.items():
        if palabra_clave in key:
            return url
    return "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?auto=format&fit=crop&w=800&q=60"
