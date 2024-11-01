from flask import Flask, request, session, redirect, url_for
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

if __name__ == '__main__':
    app.run(debug=True)

