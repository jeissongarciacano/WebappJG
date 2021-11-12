from math import sqrt, pi
def fibonacci(a):
    if a >=0:
        array = [0,1,1]
        if a==1:
            print(0)
        elif a==2:
            print([0,1])
        elif a==3:
            print(array)
        else:
            for i in range(3,a):
                aux=array[i-1]+array[i-2]
                array.append(aux)
            print(array)
    else:
        print("numero negativo")
def factorial(a):
    if a >=0:
        ans = 1
        while a>1:
            ans *= a
            a -= 1
        print(ans)
    else:
        print("numero negativo")
def APtriangulo(lado1,lado2,lado3):
    if lado1+lado2>lado3 and lado2+lado3>lado1 and lado3+lado1>lado2 and lado1>0 and lado2>0 and lado3>0:
        s = (lado1+lado2+lado3)/2
        area=sqrt(s*(s-lado1)*(s-lado2)*(s-lado3))
        perimetro=lado1+lado2+lado3
        print(area)
        print(perimetro)
    else:
        print("el triangulo no existe, la suma de dos de sus lados debe ser mayor que el otro lado o lado negativo")
def APcirculo(r):
    if r >= 0:
        area = pi*r*r
        perimetro = 2*pi*r
        print(area)
        print(perimetro)
    else:
        print("radio negativo")
def APrectangulo(ladoa,ladob):
    if ladoa>0 and ladob>0:
        area = ladoa*ladob
        perimetro = 2*(ladob+ladoa)
        print(area)
        print(perimetro)
    else:
        print("lados negativos")

