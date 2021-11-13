from flask import flash
from math import sqrt, pi

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
        flash('Número negativo o cero', category='error')
def factorial(a):
    if a >=0:
        ans = 1
        while a>1:
            ans *= a
            a -= 1
        return ans
    else:
        flash('Número negativo', category='error')
def APtriangulo(lado1,lado2,lado3):
    if lado1+lado2>lado3 and lado2+lado3>lado1 and lado3+lado1>lado2 and lado1>0 and lado2>0 and lado3>0:
        s = (lado1+lado2+lado3)/2
        area=sqrt(s*(s-lado1)*(s-lado2)*(s-lado3))
        perimetro=lado1+lado2+lado3
        return area,perimetro
    else:
        flash('El triángulo no existe, la suma de dos de sus lados debe ser mayor que el otro lado o lado negativo', category='error')
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