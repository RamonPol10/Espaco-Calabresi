from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def Homepage():  # put application's code here
    return render_template("Homepage.html")
@app.route("/contatos")
def contatos():
    return render_template("contatos.html")
@app.route("/usuarios/<usuario>")
def usuarios(usuario):
    return render_template ("usuarios.html", usuario=usuario)
if __name__ == '__main__':
    app.run(debug=True)
