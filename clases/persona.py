class Persona(object):
    "Calse Persona"

    def __init__(self, pNombre, pEdad, pSueldo):
        self.setNombre(pNombre)
        self.setEdad(pEdad)
        self.__setSueldo(pSueldo)

    def setEdad(self, pEdad):
        self.__edad = pEdad

    def getEdad(self):
        return self.__edad

    def setNombre(self, pNombre):
        self.__nombre = pNombre

    def getNombre(self):
        return self.__nombre

    def __setSueldo(self, pSueldo):
        self.__sueldo = pSueldo

    def getSueldo(self):
        return self.__sueldo
    nombre = property(getNombre, setNombre)
    edad = property(getEdad, setEdad)


class Gerente(Persona):

    def __init__(self, pNombre, pEdad):
        Persona.__init__(self, pNombre, pEdad, 5000)


class Secretaria(Persona):

    def __init__(self, pNombre, pEdad):
        Persona.__init__(self, pNombre, pEdad, 500)

if __name__ == '__main__':
    g = Gerente("Juan", 56)
    s = Secretaria("Rocio", 33)
    print "El Gerente es", g.nombre, " gana ", g.getSueldo()
    print "La Secretaria es ", s.getNombre(), " gana ", s.getSueldo

Zavaleta Sanchez
Ramirez Gonzalez
Muñiz Trejo
Espinosa Beltran
