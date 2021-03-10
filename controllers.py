from app import app
from flask import render_template
from database.classes import Premio,Curso


@app.route('/')
def index():
    return render_template(
        'index.html',
        cursos=Curso.listar(),
        premios=Premio.listar()
        )

@app.route('/novo')
def novo():
    return render_template('nova.html')

@app.route('/ola')
def ola():
    return '<h1>Olá Mundo Flask!</h1>'
