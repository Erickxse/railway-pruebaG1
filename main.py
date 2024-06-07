from flask import Flask, jsonify, request, session
import random
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Secret key for session management

@app.route('/')
def index():
    return jsonify({"message": "Welcome to the Number Guessing Game API!"})

@app.route('/start', methods=['POST'])
def start():
    # Start a new game by generating a random number between 1 and 100
    session['number'] = random.randint(1, 100)
    session['attempts'] = 0
    return jsonify({"message": "New game started. Guess a number between 1 and 100."})

@app.route('/guess', methods=['POST'])
def guess():
    if 'number' not in session:
        return jsonify({"error": "Game not started. Use /start to begin a new game."}), 400
    
    data = request.get_json()
    guess = data.get('guess')

    if not isinstance(guess, int):
        return jsonify({"error": "Invalid input. Please provide an integer guess."}), 400

    session['attempts'] += 1
    number = session['number']

    if guess < number:
        return jsonify({"message": "Too low!", "attempts": session['attempts']})
    elif guess > number:
        return jsonify({"message": "Too high!", "attempts": session['attempts']})
    else:
        attempts = session['attempts']
        session.pop('number
