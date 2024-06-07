from flask import Flask, jsonify
import random
import os

app = Flask(__name__)

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
    quote = random.choice(quotes)
    return jsonify({"quote": quote})

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
