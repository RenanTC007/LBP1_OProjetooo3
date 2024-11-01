from flask import Flask, request
from controllers.controller_login import cad_controller
from controllers.controller_compras import carro

app = Flask(__name__)
app.secret_key = 'sua-chave-secreta'
app.register_blueprint(cad_controller)
app.register_blueprint(carro)


@app.before_request
def before():
    if request.path == '/login':
        return

if __name__ == '__main__':
    app.run(debug=True)

