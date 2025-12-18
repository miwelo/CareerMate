from datetime import datetime
import os
from functools import wraps
from flask import Flask, render_template, request, redirect, url_for, session

from models.preguntas import contar_preguntas, obtener_todas_preguntas
from models.carreras import CARRERAS_OBJETIVO
from models.recomendador import calcular_estadisticas, recomendar_carreras
from utils.storage import agregar_al_historial, cargar_historial, guardar_historial, guardar_estadisticas

app = Flask(__name__)
app.secret_key = 'vocational-ai-secret-key-2024'
ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD', 'admin123')


def login_requerido(func):
    @wraps(func)
    def _decorated(*args, **kwargs):
        if not session.get('auth'):
            return redirect(url_for('login', next=request.path))
        return func(*args, **kwargs)

    return _decorated

@app.route('/')
def index():
    return redirect(url_for('test'))

@app.route('/test')
def test():
    preguntas = obtener_todas_preguntas()
    return render_template('test.html', preguntas=preguntas)

@app.route('/procesar-test', methods=['POST'])
def procesar_test():
    try:
        respuestas = []
        for i in range(contar_preguntas()):
            key = f'respuesta_{i}'
            if key in request.form:
                opcion = int(request.form[key])
                respuestas.append((i, opcion))

        if not respuestas:
            return redirect(url_for('test'))

        recomendaciones = recomendar_carreras(respuestas)
        historial = cargar_historial()
        carreras_recomendadas = [r['carrera'] for r in recomendaciones]
        compatibilidades = [r['compatibilidad'] for r in recomendaciones]
        historial = agregar_al_historial(historial, carreras_recomendadas, compatibilidades)

        return render_template('resultados.html', recomendaciones=recomendaciones, fecha=datetime.now())

    except Exception as exc:
        app.logger.error("Error procesando test: %s", exc)
        return redirect(url_for('test'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    destino = request.args.get('next') or url_for('estadisticas')

    if request.method == 'POST':
        password = request.form.get('password', '')
        if password == ADMIN_PASSWORD:
            session['auth'] = True
            return redirect(destino)
        error = 'Credenciales inválidas'

    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('auth', None)
    return redirect(url_for('test'))


@app.route('/estadisticas')
@login_requerido
def estadisticas():
    historial = cargar_historial()
    estadisticas_data = calcular_estadisticas(historial)
    guardar_estadisticas(estadisticas_data)
    return render_template('estadisticas.html', estadisticas=estadisticas_data, historial=historial, carreras=CARRERAS_OBJETIVO)

@app.route('/limpiar-historial', methods=['POST'])
@login_requerido
def limpiar_historial():
    guardar_historial([])
    return redirect(url_for('estadisticas'))

@app.errorhandler(404)
def not_found(error):
    return render_template('error.html', error_code=404, error_message='Página no encontrada'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('error.html', error_code=500, error_message='Error interno del servidor'), 500

@app.context_processor
def inject_config():
    return {
        'app_name': 'Vocational AI Recommender',
        'app_version': '3.0 (Python + Flask)',
        'carreras': CARRERAS_OBJETIVO,
        'total_preguntas': contar_preguntas()
    }

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
