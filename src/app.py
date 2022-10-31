from flask import Flask, render_template
from users import users

app = Flask(__name__)

@app.route('/', methods=['GET'])
def ping():
    return render_template('raiz.html', raiz = "hello world")

@app.route('/users')
def usersHandler():
    return render_template('usuarios.html', usuarios = users)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4000, debug=True)