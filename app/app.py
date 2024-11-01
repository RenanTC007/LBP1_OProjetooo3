from flask import Flask, request, session, redirect, url_for, render_template
from controllers.controller_login import cad_controller
from controllers.controller_compras import carro

app = Flask(__name__)
app.secret_key = 'sua-chave-secreta'
app.register_blueprint(cad_controller)
app.register_blueprint(carro)


@app.before_request
def before():
    if request.path == "/static/css/styles.css":
        return
    if request.endpoint == 'logando.index':
        return
    if request.endpoint == 'logando.login':
        return
    if 'username' not in session:
        return redirect(url_for('logando.index'))
    else:
        return

@app.errorhandler(400)
def pageNotFound(e):
    return render_template("400.html"), 400

@app.errorhandler(401)
def pageNotFound(e):
    return render_template("401.html"), 401

@app.errorhandler(404)
def pageNotFound(e):
    return render_template("404.html"), 404

@app.errorhandler(403)
def pageNotFound(e):
    return render_template("403.html"), 403


@app.errorhandler(500)
def pageNotFound(e):
    return render_template("500.html"), 500

@app.errorhandler(Exception)
def handle_generic_error(e):
    return render_template("erro_gen.html"), 500


if __name__ == '__main__':
    app.run(debug=True)

