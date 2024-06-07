from flask import Flask, jsonify, render_template, request, redirect, url_for
import random
import os

app = Flask(__name__)

# Usuarios y contraseñas de ejemplo (deberías cambiar esto en un entorno real)
usuarios = {
    "usuario1": "contraseña1",
    "usuario2": "contraseña2"
}

quotes = [
    "La mejor forma de predecir el futuro es creandolo. - Peter Drucker",
    "El unico limite para nuestra realizacion de manana son nuestras dudas de hoy. - Franklin D. Roosevelt",
    "Haz lo que puedas, con lo que tienes, donde estes. - Theodore Roosevelt",
    "La unica forma de hacer un gran trabajo es amar lo que haces. - Steve Jobs",
    "Cree que puedes y ya estaras a mitad de camino. - Theodore Roosevelt",
    "El exito no es la clave de la felicidad. La felicidad es la clave del exito. - Albert Schweitzer",
    "La vida es lo que hacemos de ella. Siempre lo ha sido, siempre lo sera. - Grandma Moses",
    "No cuentes los dias, haz que los dias cuenten. - Muhammad Ali",
    "El unico lugar donde el exito viene antes del trabajo es en el diccionario. - Vidal Sassoon",
    "No esperes. Nunca sera el momento perfecto. - Napoleon Hill",
    "La accion es la clave fundamental para todo exito. - Pablo Picasso",
    "La mejor manera de empezar es dejar de hablar y comenzar a hacer. - Walt Disney",
    "Tu tiempo es limitado, no lo desperdicies viviendo la vida de alguien mas. - Steve Jobs",
    "La vida es 10% lo que me ocurre y 90% como reacciono a ello. - Charles Swindoll",
    "El exito es la suma de pequenos esfuerzos repetidos dia tras dia. - Robert Collier"
]

@app.route('/')
def index():
    if 'username' in session:
        quote = random.choice(quotes)
        return jsonify({"quote": quote})
    else:
        return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in usuarios and usuarios[username] == password:
            session['username'] = username
            return redirect(url_for('index'))
        else:
            return render_template('login.html', message='Credenciales inválidas. Por favor, inténtalo de nuevo.')
    return render_template('login.html')

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'  # Clave secreta para la sesión (deberías cambiar esto en un entorno real)
    app.run(debug=True, port=os.getenv("PORT", default=5000))
