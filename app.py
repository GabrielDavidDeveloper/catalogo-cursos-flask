from flask import Flask, render_template

app = Flask ('teste')

LISTA = [
    'Item 1',
    'Item 2',
    'Item 3',
    'Item 4'
]

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/ola')
def ola():
    resposta = '<h1>Olá mundo no Flask!</h1>'

    respota = '<ul>'
    for item in LISTA:
        resposta += '<li>'+item+'</li>'
    resposta += '</ul>'

    return resposta

app.run(debug=True)