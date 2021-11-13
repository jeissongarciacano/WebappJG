from typing import Text
from flask import Blueprint, render_template, request, flash
from math import sqrt, pi

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/Fibonacci', methods=['GET', 'POST'])
def Fibonacci():
    if request.method == 'POST':
        if request.form.get('number') != '':
            fibon = int(request.form.get('number'))
            if fibon > 0:
                mensaje=fibonacci(fibon)
                title='____________________________________________________________________________________'
                text='Resultado:'
                text2=  'La cantidad es: ' + str(fibon)
                return render_template("Fibonacci.html",titulo=title, numeroin=text2,resultado=text,result=mensaje)
            else:
                flash('Debe ser un numero mayor a cero', category='error')
        else:
            flash('El espacio no puede estar en blanco', category='error')
    return render_template("Fibonacci.html")

@views.route('/Factorial', methods=['GET', 'POST'])
def Factorial():
    if request.method == 'POST':
        if request.form.get('number') != '':
            factn = int(request.form.get('number'))
            if factn >= 0:
                mensaje=factorial(factn)
                title='____________________________________________________________________________________'
                text='Resultado:'
                text2=  'El numero es: ' + str(factn) + '!'
                return render_template("Factorial.html",titulo=title, numeroin=text2,resultado=text,result=mensaje)
            else:
                flash('Debe ser un numero mayor o igual a cero', category='error')
        else:
            flash('El espacio no puede estar en blanco', category='error')
    return render_template("Factorial.html")

@views.route('/APtriangulo', methods=['GET', 'POST'])
def APtriangulo():
    if request.method == 'POST':
        if request.form.get('lado1') != '' and request.form.get('lado2') != '' and request.form.get('lado3') != '':
            lado1 = int(request.form.get('lado1'))
            lado2 = int(request.form.get('lado2'))
            lado3 = int(request.form.get('lado3'))
            if lado1+lado2>lado3 and lado2+lado3>lado1 and lado3+lado1>lado2 and lado1>0 and lado2>0 and lado3>0:  
                m=APtriangulo(lado1,lado2,lado3)
                mensaje='Area= ' + str(m[0])
                mensaje2='Perimetro= ' + str(m[1])
                title='____________________________________________________________________________________'
                text='Resultado:'
                text2=  'El lado 1 mide: ' + str(lado1) 
                text3=  'El lado 2 mide: ' + str(lado2)
                text4=  'El lado 3 mide: ' + str(lado3)
                return render_template("APtriangulo.html",titulo=title, texti=text,texti1=text2,texti2=text3,texti3=text4,resultado=text,result=mensaje,result2=mensaje2)
            else:
                flash('El triangulo no existe, la suma de dos de sus lados debe ser mayor que el otro lado', category='error')
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
                m=APrectangulo(ladoa,ladob)
                mensaje='Area= ' + str(m[0])
                mensaje2='Perimetro= ' + str(m[1])
                title='____________________________________________________________________________________'
                text='Resultado:'
                text2=  'El lado A mide: ' + str(ladoa) 
                text3=  'El lado B mide: ' + str(ladob)
                return render_template("APrectangulo.html",titulo=title, texti=text,texti1=text2,texti2=text3,resultado=text,result=mensaje,result2=mensaje2)
            else:
                flash('Los lados deben ser mayores a cero', category='error')
        else:
            flash('Los espacios no pueden estar en blanco', category='error')
    return render_template("APrectangulo.html")

@views.route('/APcirculo', methods=['GET', 'POST'])
def APAPcirculo():
    if request.method == 'POST':
        if request.form.get('radio') != '':
            radio = int(request.form.get('radio'))
            if radio>0 and radio>0:
                m=APcirculo(radio)
                mensaje='Area= ' + str(m[0])
                mensaje2='Perimetro= ' + str(m[1])
                title='____________________________________________________________________________________'
                text='Resultado:'
                text2=  'El radio mide: ' + str(radio) 
                return render_template("APcirculo.html",titulo=title, texti=text,texti1=text2,resultado=text,result=mensaje,result2=mensaje2)
            else:
                flash('El radio debe ser positivo', category='error')
        else:
            flash('El espacio no puede estar en blanco', category='error')
    return render_template("APcirculo.html")


def fibonacci(a):
    if a >0:
        array = [0,1,1]
        if a==1:
            return 0
        elif a==2:
            return [0,1]
        elif a==3:
            return array
        else:
            for i in range(3,a):
                aux=array[i-1]+array[i-2]
                array.append(aux)
            return array
    else:
        flash('Numero negativo o cero', category='error')
def factorial(a):
    if a >=0:
        ans = 1
        while a>1:
            ans *= a
            a -= 1
        return ans
    else:
        flash('Numero negativo', category='error')
def APtriangulo(lado1,lado2,lado3):
    if lado1+lado2>lado3 and lado2+lado3>lado1 and lado3+lado1>lado2 and lado1>0 and lado2>0 and lado3>0:
        s = (lado1+lado2+lado3)/2
        area=sqrt(s*(s-lado1)*(s-lado2)*(s-lado3))
        perimetro=lado1+lado2+lado3
        return area,perimetro
    else:
        flash('El triangulo no existe, la suma de dos de sus lados debe ser mayor que el otro lado o lado negativo', category='error')
def APcirculo(r):
    if r >= 0:
        area = pi*r*r
        perimetro = 2*pi*r
        return area,perimetro
    else:
        flash('Radio negativo', category='error')
def APrectangulo(ladoa,ladob):
    if ladoa>0 and ladob>0:
        area = ladoa*ladob
        perimetro = 2*(ladob+ladoa)
        return area,perimetro
    else:
        flash('Lados negativos', category='error')




