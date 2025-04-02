from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        x = float(request.form['x'])
        z = float(request.form['z'])
        y = x * z + z + x
        return jsonify({'result': y})
    except ValueError:
        return jsonify({'error': 'Valores inválidos'}), 400

if __name__ == '__main__':
    app.run(debug=True)