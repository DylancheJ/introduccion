from flask import Flask, request
app = Flask(__name__)
@app.route("/")
def hello_world():
    return '<a href="/segundapagina">DAR CLIC AQUI</a>'
@app.route("/segundapagina")
def bienvenidos():
    return '''
        <form method="post" action="/formulario" >
        <label for="">Nombre</label>
        <input name="mensajero" type="text" placeholder="Ingresa nombre">
        <button type="submit">ENVIAR</button>
          '''
@app.route("/formulario",methods=["post"] )
def informacion():
    x=request.form.get('mensajero')
    return f'<h1>Hola bienvenido,{x} </h1>'
app.run(debug=True)
