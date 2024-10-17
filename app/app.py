from flask import Flask
from controllers.c_1 import cad_controller

app = Flask(__name__)
app.secret_key = 'sua-chave-secreta'
app.register_blueprint(cad_controller)

@app.before_request
def aviso_before():
    print("Executa antes da requisição")

@app.after_request
def aviso_after(response):
    print("Depois da requisição e antes da resposta")
    return response

if __name__ == '__main__':
    app.run(debug=True)

