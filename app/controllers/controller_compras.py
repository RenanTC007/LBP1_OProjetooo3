from flask import Flask, Blueprint, make_response, request, render_template
from models.modelos_produtos import *

carro = Blueprint('compra', __name__)


@carro.route('/compras')
def comprar():
    return render_template('index4.html')

@carro.route('/carrinho', methods = ['POST', 'GET'])
def set_cookie():
    if request.form['campo1']:
        resp = listProdutos[0].id
        return resp


@carro.route('/carrinho/add')
def get_cookie():
    for casa in listProdutos:
        username = request.cookies.get(casa.id)
        if username:
            return username
        else:
            return 'sem cookie'
    

@carro.route('/carrinho/del')
def delete_cookie():
    resp = make_response('cookie deletado')
    resp.set_cookie('username', '', expires=0)
    return resp




