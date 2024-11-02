from flask import Flask, Blueprint, make_response, request, render_template, redirect, url_for, flash
from models.modelos_produtos import *

carro = Blueprint('compra', __name__)


@carro.route('/compras/add', methods = ['POST', 'GET'])
def adicionar():
    id = request.args.get('id')
    resp = make_response(redirect(url_for('compra.cest')))
    cookie = request.cookies.get(str(id))
    if cookie:
        resp.set_cookie(str(id), str(int(cookie)+1))
    else:
        resp.set_cookie(str(id), '1', max_age=60*60*24)
    flash("Operação realizada com sucesso!", "success")
    return resp

@carro.route('/compras/del', methods = ['POST', 'GET'])
def deletar():
    id = request.args.get('id')
    resp = make_response(redirect(url_for('compra.cest')))
    cookie = request.cookies.get(str(id))
    if cookie:
        if int(cookie)-1 >= 0:
            resp.set_cookie(str(id), str(int(cookie)-1))
    else:
        resp.set_cookie(str(id), ' ', expires=0)
    flash("Operação realizada com sucesso!", "success")
    return resp

@carro.route('/compras')
def cest():
    cesto = []
    for i in produtos:
        cookie = request.cookies.get(str(i.id))
        if cookie:
            cesto.append({'nome': i.nome,'qtd': cookie,'total': int(cookie)*i.preco
            })
    return render_template('index4.html', cesto=cesto, produtos = produtos)
        



