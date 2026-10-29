from app import app
from flask import url_for, redirect, render_template, request

@app.route('/', methods=["GET"])
def inicio():
    return render_template('inicio.html')

@app.route('/cadastrar')
def cadastrar():
    return render_template('cadastrar.html')

@app.route('/criar', methods=['POST'])
def criar():
    return redirect(url_for('inicio'))


    
