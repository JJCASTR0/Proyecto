from flask import Flask
app=Flask(__name__)

@app.route("/notas")
@app.route("/notas/<float:nota1>/<float:nota2>/<float:nota3>")

def notas(nota1=0,nota2=0,nota3=0):
    r = nota1*0.30 + nota2*0.30 + nota3*0.40
    return f"<h1>El resultado es: {r} </h1> <hr>"

if __name__=="__main__":
    app.run(debug=True)