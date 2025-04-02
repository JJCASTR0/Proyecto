from flask import Flask, jsonify
from flask_cors import CORS   
import math as mt

app=Flask(__name__)
CORS(app)

## Suma
@app.route('/')
@app.route('/<float:n1>/<float:n2>')
@app.route('/<int:n1>/<int:n2>')
@app.route('/<int:n1>/<float:n2>')
@app.route('/<float:n1>/<float:n2>')
def suma(n1=0, n2=0):
    resultado = n1+n2
    data = {
        'Resultado' : resultado,
        'Operacion' : 'Suma',
    }
    return jsonify(data)

## Resta
@app.route('/resta/<float:n1>/<float:n2>')
@app.route('/resta/<int:n1>/<int:n2>')
@app.route('/resta/<int:n1>/<float:n2>')
@app.route('/resta/<float:n1>/<float:n2>')
def resta(n1=0, n2=0):
    resultado = n1-n2
    data = {
        'Resultado' : resultado,
        'Operacion' : 'Resta',
    }
    return jsonify(data)

## Multiplicacion
@app.route('/multiplicacion/<float:n1>/<float:n2>')
@app.route('/multiplicacion/<int:n1>/<int:n2>')
@app.route('/multiplicacion/<int:n1>/<float:n2>')
@app.route('/multiplicacion/<float:n1>/<float:n2>')
def multiplicacion(n1=0, n2=0):
    resultado = n1*n2
    data = {
        'Resultado' : resultado,
        'Operacion' : 'Multiplicacion',
    }
    return jsonify(data)

## Division
@app.route('/division/<float:n1>/<float:n2>')
@app.route('/division/<int:n1>/<int:n2>')
@app.route('/division/<int:n1>/<float:n2>')
@app.route('/division/<float:n1>/<float:n2>')
def division(n1=0, n2=0):
    resultado = n1/n2
    data = {
        'Resultado' : resultado,
        'Operacion' : 'Division',
    }
    return jsonify(data)

## Potenciacion
@app.route('/potenciacion/<float:n1>/<float:n2>')
@app.route('/potenciacion/<int:n1>/<int:n2>')
@app.route('/potenciacion/<int:n1>/<float:n2>')
@app.route('/potenciacion/<float:n1>/<float:n2>')
def potenciacion(n1=0, n2=0):
    resultado = n1**n2
    data = {
        'Resultado' : resultado,
        'Operacion' : 'Potenciación',
    }
    return jsonify(data)

## Seno
@app.route("/seno/<int:n1>")
@app.route("/seno/<float:n1>")
def seno(n1=0):
    resultado = mt.sin(n1)
    data = {
        'Resultado' : resultado,
        'Operacion' : "Seno"    
    }
    return jsonify(data)

## Coseno
@app.route("/coseno/<int:n1>")
@app.route("/coseno/<float:n1>")
def coseno(n1=0):
    resultado = mt.cos(n1)
    data = {
        'Resultado' : resultado,
        'Operacion' : "Coseno"    
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)