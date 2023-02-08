"""
    Programa7
    Nombre: Danae Barqueras A
    Fecha: 01/02/2023
    Descripcion:comparar y obtener un numero mayor
"""


def mayor(numero1,numero2) :
    if numero1 > numero2 :
         print(numero1)
    elif numero2 > numero1 :
      print(numero2)
    else:
      print(None)
       
mayor(10,5)#3
mayor(5,10)#3
mayor(5,5)#None




def mayor(numero1:int,numero2:int)->int :
    mayor= None
    if numero1 > numero2 :
        mayor = numero1
        mayor=numero1
    elif numero2 > numero1 :
        mayor= numero2
    else:
         mayor=None

    return mayor


print(mayor(8,4))#3
print(mayor(8,4))#3
print(mayor(4,4))#None
