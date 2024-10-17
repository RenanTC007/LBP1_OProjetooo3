from flask import Flask, render_template, request, Blueprint, session
from models.m_1 import *

cad_controller = Blueprint('logando', __name__)

@cad_controller.route('/')
def index():
    if 'username' in session:
        return render_template('index2.html', nome = session['username'])
    else:
        return render_template('index.html')

@cad_controller.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if verifc_senha(request.form['username'], request.form['senha']) == 1:
            session['username'] = request.form['username'] 
            return render_template('index2.html', nome = session['username'])
        else:
            return render_template('index.html', valor = 1)
    else:
        if 'username' in session:
            return render_template('index2.html', nome = session['username'])
        else:
            return render_template('index.html', fora = 1)
        
@cad_controller.route('/admin', methods = ['POST', 'GET'])
def admin():
    if 'username' in session:
        if verifc_admin(session['username']) == 1:
            return render_template('index3.html', admin = 1, nome = session['username'])
        else:
            return render_template('index3.html', admin = 0, nome = session['username'])
    else:
        return render_template('index.html', fora = 1)
    
@cad_controller.route('/user', methods = ['POST', 'GET'])
def usuar():
    if 'username' in session:
        return render_template('index3.html', user = 1, nome = session['username'])
    else:
        return render_template('index.html', fora = 1)

@cad_controller.route('/logout')
def logout():
    session.pop('username', None)
    return render_template('index.html')