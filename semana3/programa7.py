"""
    Programa7
    Nombre: Danae Barqueras A
    Fecha: 01/02/2023
    Descripcion:Comparar 2 numeros enteros e imprimir el numero mayor
"""
#El proposito es comparar dos numeros enteros y obtener el mayor de ellos
print(" Este programa logra comparar dos numeros enteros para saber cual es el numero mayor ") #Indicaciones sobre que puede hacer nuestro programa

print("Bienvenido humano :)")#Introduccion de bienvenida

n1 =input("Coloca el primer numero entero: ")#Colocar un numero
n2 =input("Coloca el segundo numero: ")#Colocar un segundo numero

if n1 > n2:
    print(f"Humano el numero {n1} es mayor que {n2}")#Primer desicion si el numero dos es mayor

elif n2 > n1 :
    print(f"Humano el numero {n2} es mayor que {n1}")#Segunda eleccion si el numero dos es menor.
else:
    print(None) #Ultima eleccion 

#A continuacion se presentan formas diferentes de obtener resultados.
#PRIMERA FORMA

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
        
            
    







