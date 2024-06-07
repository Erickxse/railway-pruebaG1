from flask import Flask, jsonify
import random
import os

app = Flask(__name__)

quotes = [
    "La mejor forma de predecir el futuro es creándolo. - Peter Drucker",
    "El único límite para nuestra realización de mañana son nuestras dudas de hoy. - Franklin D. Roosevelt",
    "Haz lo que puedas, con lo que tienes, donde estés. - Theodore Roosevelt",
    "La única forma de hacer un gran trabajo es amar lo que haces. - Steve Jobs",
    "Cree que puedes y ya estarás a mitad de camino. - Theodore Roosevelt",
    "El éxito no es la clave de la felicidad. La felicidad es la clave del éxito. - Albert Schweitzer",
    "La vida es lo que hacemos de ella. Siempre lo ha sido, siempre lo será. - Grandma Moses",
    "No cuentes los días, haz que los días cuenten. - Muhammad Ali",
    "El único lugar donde el éxito viene antes del trabajo es en el diccionario. - Vidal Sassoon",
    "No esperes. Nunca será el momento perfecto. - Napoleon Hill",
    "La acción es la clave fundamental para todo éxito. - Pablo Picasso",
    "La mejor manera de empezar es dejar de hablar y comenzar a hacer. - Walt Disney",
    "Tu tiempo es limitado, no lo desperdicies viviendo la vida de alguien más. - Steve Jobs",
    "La vida es 10% lo que me ocurre y 90% cómo reacciono a ello. - Charles Swindoll",
    "El éxito es la suma de pequeños esfuerzos repetidos día tras día. - Robert Collier"
]

@app.route('/')
def index():
    quote = random.choice(quotes)
    return jsonify({"quote": quote})

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
