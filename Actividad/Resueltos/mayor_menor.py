from flask import Flask
app=Flask(__name__)

@app.route("/suma/<int:a>/<int:b>")
@app.route("/edades/<int:edad>")

def suma(a=0,b=0):
    r = a +b
    if r//2 == 0:
        return f"<h1>El resultado de la suma de a y b es: {r} y es un numero par </h1> <hr>"
    else:
        return f"<h1>El resultado de la suma de a y b es: {r} y es un numero impar </h1> <hr>"

def edades(edad=0):
    if edad < 18:
        resultado = "Es menor de edad"
    elif edad < 60:
        resultado = "Es Mayor de edad"
    else:
        resultado = "Es un adulto mayor"
    return f"<h1>La persona <strong> {resultado} </strong></h1> <hr>"


if __name__=="__main__":
    app.run(debug=True)