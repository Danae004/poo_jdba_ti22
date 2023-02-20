class Persona:
    __email = None
    __nombre = None
    def __init__(self):
        print("Persona")
    def setNombre(self,nombre):
        self.__nombre = nombre

    def getNombre(self):
        return self.__nombre
    
    def getEmail(self):
        self.__email = email

    def setEmail(self,email):
        return self.__email

dejah = Persona()
dejah.setNombre("Dejah")
dejah.setEmail("@hola.com")
print(dejah.getNombre())
print(dejah.getEmail)