from flask import Flask, Blueprint, make_response, request, render_template
from models.modelos_produtos import *

carro = Blueprint('compra', __name__)

@carro.route('/compras')
def comprar():
    return render_template('index4.html')

@carro.route('/carrinho', methods = ['POST', 'GET'])
def set_cookie():
    pass
        



