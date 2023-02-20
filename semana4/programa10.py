"""
    Programa10
    Nombre: Danae Barqueras A
    Fecha: 01/02/2023
    Descripcion:comparar y obtener un numero mayor
"""
#Primero definimos cada variable y asignacion

def mayor(numero1,numero2) :
    if numero1 > numero2 :
         print(numero1)
    elif numero2 > numero1 :
         print(numero2)
    else:
         print(None)
       #Colocamos las formas en las que nuestro programa debe responder
mayor(10,5)#3
mayor(5,10)#3
mayor(5,5)#None
#Asignamos valores para ejecutar nuestro codigo


#Colocamos las variables con las asignaciones
def mayor(numero1:int,numero2:int)->int :
    mayor= None
    if numero1 > numero2 :
        mayor = numero1
        mayor=numero1
    elif numero2 > numero1 :
        mayor= numero2
    else:
         mayor=None
       #Damos las decisiones (o posibles) que puede tomar
    return mayor


print(mayor(8,4))#3
print(mayor(8,4))#3
print(mayor(4,4))#None
#Asignamos los valores he imprimimos