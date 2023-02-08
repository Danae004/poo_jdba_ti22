"""
    Programa8
    Nombre: Danae Barqueras A
    Fecha: 01/02/2023
    Descripcion:Formas de comparar dos numeros y obtener el numero mayor
"""

#PRIMERA FORMA
n1 =input("Coloca el primer numero entero: ")#Colocar un numero
n2 =input("Coloca el segundo numero: ")#Colocar un segundo numero

if n1 > n2 :
    print(n1)
    if n2 > n1 :
        print(n2)
if n1 == n2 :
    print(None)

#SEGUNDA FORMA
    if n2 > n1 :
        print(n2)
        if n1 > n2 :
            print(n1)
    if n2 == n1 :
        print(None)
#TERCERA FORMA
    if n1 > n2 :
        print(n1)
    elif n2 > n1 :
        print(n2)
    else:
        print(None)
#CUARTA FORMA
    if n1 < n2 :
        print(n2)
    elif n2 < n1 :
        print(n1)
    else:
        print(None)
#QUINTA FORMA
    if n2 < n1 :
        print(n1)
    if n1 < n2 :
        print(n2)
    if n1 == n2 :
        print(None)
#SEXTA FORMA
    if n1 >= n2 :
        if n1 > n2 :
            print(n1)
    else:
        print(None)
 
#SEPTIMA FORMA
    if n1 <= n2 :
        if n1 < n2:
          print(n2)
else:
    print(None)

#OCTABA FORMA
    if n1 <= n2 :
      if n1 == n2 :
       print(n1)
      else:
          print(None)
    else:
            print(n2)
#NOVENA FORMA
if n1 == n2:
    print(None)
elif n1 > n2 :
    print(n1)
else:
    print(n2)
#DECIMA FORMA
    if n2 == n1:
        print(None)
    elif n1 > n2:
        print(n2)
    else:
        print(n1)

#ONCEABA FORMA