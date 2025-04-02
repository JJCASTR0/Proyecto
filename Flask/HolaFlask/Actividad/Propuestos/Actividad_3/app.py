from flask import Flask, render_template, request, jsonify
import math

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular_area', methods=['POST'])
def calcular_area():
    figura = request.form['figura']
    try:
        if figura == "circulo":
            radio = float(request.form['radio'])
            area = math.pi * (radio ** 2)
        elif figura == "cuadrado":
            lado = float(request.form['lado'])
            area = lado ** 2
        elif figura == "triangulo":
            base = float(request.form['base'])
            altura = float(request.form['altura'])
            area = (base * altura) / 2
        else:
            return jsonify({'error': 'Figura no válida'}), 400
        
        return jsonify({'figura': figura, 'area': round(area, 2)})
    
    except ValueError:
        return jsonify({'error': 'Valores inválidos'}), 400

if __name__ == '__main__':
    app.run(debug=True)