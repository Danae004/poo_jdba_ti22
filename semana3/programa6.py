"""
    Programa6
    Nombre: Danae Barqueras A
    Fecha: 31/01/2023
    Descripcion: Area y perimetro del 
    circulo y cuadrado
"""
print("Este programa saca el area y perimetro de un circulo y cuadrado") #Descripcon de lo que nuestro programa realizara
PI= (3.1416) #Variable con los datos a ocupar
radio =input("Dame el valor del radio: ") #Insertar un valor
area_circulo= (PI) * (radio **2)
#Colocar los datos del circulo
print("El area del circulo con un radio de {} es {}: ",(area_circulo))

print("perimetro del circulo") #Calcula el perimetro del circulo

diametro= float(input("Dame el valor de tu diametro: "))
perimetro_circulo = (diametro * PI)
#Asignamos las variables a utilizar
print("Area del cuadrado")

lado= float(input("Dame el valor de tu lado: "))
area_cuadrado= (lado * lado)
#Asignamos los valores
print("El area del cuadrado es de: ",area_cuadrado)

print("Perimetro del cuadrado")
perimetro_cuadrado = (lado *4)

print("El perimetro del cuadrado es de: ",perimetro_cuadrado)
#Imprimimos resultados

















Circulo =input("El area del circulo con un radio de:{} es: ",area)