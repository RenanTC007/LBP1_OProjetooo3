from flask import Flask, Blueprint, make_response, request, render_template
from models.modelos_produtos import *

carro = Blueprint('compra', __name__)


@carro.route('/compras')
def comprar():
    return render_template('index4.html')

@carro.route('/carrinho', methods = ['POST', 'GET'])
def set_cookie():
    if request.form['campo1']:
        resp = make_response("Cookie criado")
        resp.set_cookie(listProdutos[0].id, request.form['campo1'], max_age=60*60*24)
        username = request.cookies.get(listProdutos[0].id)
        if username:
            preco_final = listProdutos[1].preco * float(request.form['campo1'])
            return str(preco_final)
    if request.form['campo2']:
        resp = make_response("Cookie criado")
        resp.set_cookie(listProdutos[1].id, request.form['campo2'], max_age=60*60*24)
        username = request.cookies.get(listProdutos[1].id)
        if username:
            preco_final = listProdutos[1].preco * float(request.form['campo1'])
            return str(preco_final)
    if request.form['campo3']:
        resp = make_response("Cookie criado")
        resp.set_cookie(listProdutos[2].id, request.form['campo3'], max_age=60*60*24)
        username = request.cookies.get(listProdutos[2].id)
        if username:
            preco_final = listProdutos[2].preco * float(request.form['campo3'])
            return str(preco_final)
    else:
        return 'sem produtos'
        


@carro.route('/carrinho/add')
def get_cookie():
    for casa in listProdutos:
        username = request.cookies.get()
        if username:
            return username
        else:
            return 'sem cookie'
    

@carro.route('/carrinho/del')
def delete_cookie():
    resp = make_response('cookie deletado')
    resp.set_cookie('username', '', expires=0)
    return resp




