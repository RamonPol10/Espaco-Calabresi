from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def Homepage():  # put application's code here
    return render_template("Homepage.html")
@app.route("/contatos")
def contatos():
    return render_template("contatos.html")
@app.route("/usuarios/<Ramon>")
def usuarios(Ramon):
    return render_template("usuarios.html",nome_usuario=Ramon)
if __name__ == '__main__':
    app.run(debug=True)
