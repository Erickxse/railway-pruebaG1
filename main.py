from flask import Flask, jsonify
import random
import os

app = Flask(__name__)

# List of quotes
quotes = [
    "The best way to predict the future is to create it. - Peter Drucker",
    "The only limit to our realization of tomorrow is our doubts of today. - Franklin D. Roosevelt",
    "Do what you can, with what you have, where you are. - Theodore Roosevelt",
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Believe you can and you're halfway there. - Theodore Roosevelt"
]

@app.route('/')
def index():
    # Select a random quote
    quote = random.choice(quotes)
    return jsonify({"quote": quote})

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
