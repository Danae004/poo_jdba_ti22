class Persona:

  __nombre= None #Declarr las variables
  __edad= None

  def__init__(self): #Indicar lo que va a imprimir
    print("Persona")

  def getNombre(self):
    return self.__nombre

  def setNombre(self,nombre):
     self.__nombre= nombre

  def__init__(self):
    print("Edad") 
 
  def getEdad(self):
    return self.__edad

  def setEdad(self):
    self.__edad= edad  

objeto_persona = persona()
#print(objeto_persona.nombre)
objeto_persona.nombre= "Hola"
print(objeto_persona.nombre)
objeto_persona.setNombre("Dejah")
print(objeto_persona.getNombre())

print(dir(objeto_persona))

#assert dir(objeto_persona) ==op

class Alumno:
