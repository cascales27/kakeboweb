from flask import Flask  #Importacion de la clase flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hola, mundo!!'

@app.route('/adios')
def bye():
    return 'Hasta luego, cocodrilo'

