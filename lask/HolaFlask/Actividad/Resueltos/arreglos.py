from flask import Flask
import numpy as np
app=Flask(__name__)

@app.route("/arreglos")
@app.route("/arreglos/<int:valores>/<int:columns>")
@app.route("/arreglos/<int:valores>/<int:columns>/<int:rows>")

def arreglos(valores=0,columns=0,rows=0):
    if rows == 0:
        array = np.random.randint(valores, size=columns)
    else:
        array = np.random.randint(valores, size=(rows,columns))
    return f"<h1>El arreglo aleatorio es: {array} </h1> <hr>"

if __name__=="__main__":
    app.run(debug=True)