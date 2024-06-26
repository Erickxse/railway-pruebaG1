from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['admin']
        password = request.form['password']
        # Verificar si el usuario y contraseña son correctos
        if username == 'admin' and password == 'password':
            return render_template('success.html')
        else:
            return render_template('error.html')
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)