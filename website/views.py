from typing import Text
from flask import Blueprint, render_template, request, flash

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/Fibonacci', methods=['GET', 'POST'])
def Fibonacci():
    if request.method == 'POST':
        if request.form.get('number') != '':
            fibon = int(request.form.get('number'))
            if fibon >= 0:
                pass
            else:
                flash('Debe ser un numero mayor o igual a cero', category='error')
        else:
            flash('el espacio no puede estar en blanco', category='error')
    return render_template("Fibonacci.html")

@views.route('/Factorial', methods=['GET', 'POST'])
def Factorial():
    if request.method == 'POST':
        if request.form.get('number') != '':
            factn = int(request.form.get('number'))
            if factn >= 0:
                pass
            else:
                flash('Debe ser un numero mayor o igual a cero', category='error')
        else:
            flash('el espacio no puede estar en blanco', category='error')
    return render_template("Factorial.html")

@views.route('/APtriangulo', methods=['GET', 'POST'])
def APtriangulo():
    if request.method == 'POST':
        if request.form.get('lado1') != '' and request.form.get('lado2') != '' and request.form.get('lado3') != '':
            lado1 = int(request.form.get('lado1'))
            lado2 = int(request.form.get('lado2'))
            lado3 = int(request.form.get('lado3'))
            if lado1+lado2>lado3 and lado2+lado3>lado1 and lado3+lado1>lado2 and lado1>0 and lado2>0 and lado3>0:
                pass
            else:
                flash('el triangulo no existe, la suma de dos de sus lados debe ser mayor que el otro lado', category='error')
        else:
            flash('los espacios no pueden estar en blanco', category='error')
    return render_template("APtriangulo.html")

@views.route('/APrectangulo', methods=['GET', 'POST'])
def APrectangulo():
    if request.method == 'POST':
        if request.form.get('ladoa') != '' and request.form.get('ladob') != '':
            ladoa = int(request.form.get('ladoa'))
            ladob = int(request.form.get('ladob'))
            if ladoa>0 and ladob>0:
                pass
            else:
                flash('los lados deben ser positivos', category='error')
        else:
            flash('los espacios no pueden estar en blanco', category='error')
    return render_template("APrectangulo.html")

@views.route('/APcirculo', methods=['GET', 'POST'])
def APAPcirculo():
    if request.method == 'POST':
        if request.form.get('radio') != '':
            radio = int(request.form.get('radio'))
            if radio>0 and radio>0:
                pass
            else:
                flash('el radio debe ser positivo', category='error')
        else:
            flash('el espacio no puede estar en blanco', category='error')
    return render_template("APcirculo.html")


