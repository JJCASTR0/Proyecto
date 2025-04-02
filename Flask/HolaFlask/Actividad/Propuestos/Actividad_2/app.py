from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/multiplicar', methods=['POST'])
def multiplicar():
    try:
        numero = int(request.form['numero'])
        tabla = {f"{numero} x {i}": numero * i for i in range(1, 11)}
        return jsonify(tabla)
    except ValueError:
        return jsonify({'error': 'Número inválido'}), 400

if __name__ == '__main__':
    app.run(debug=True)