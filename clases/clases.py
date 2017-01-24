#!/usr/bin/env python3

from math import pi


class Foo(object):
    a = 1
    b = "Soy Foo"


class Gato(object):
    numero_de_patas = 0
    color = "negro"
    cv = ""

    def __init__(self, nombre="Juan"):
        self.nombre = nombre

    def dormir(self):
        print("Yo el gato {} estoy durmiendo. Zzzz...".format(self.nombre))

    def molestar_humano(self):
        while True:
            acariciar = input(
                "Acariciame a mi, el gato {}".format(
                    self.nombre))
            if acariciar == "Acariciado":
                break

gato = Gato()
gato.numero_de_patas = 4
gato.color = "marron"

print(
    "El gato tiene {} patas y es de color {}".format(
        gato.numero_de_patas,
        gato.color))

print("El gato {} tiene {} patas y es de color {} ".format(
    gato.nombre, gato.numero_de_patas, gato.color))

################################
# Implementación de la esfera. #
################################


class Esfera(object):
    """Implementación de una clase que representa una esfera en
    python. Define los métodos:

    - getRadio(self) :: Regresa el radio de la esfera
    - superficie(self) :: Regresa el valor total de la superficie de
   la esfera
    - volumen(self) :: Regresa el volumen total de la esfera
    """

    def __init__(self, radio=1):
        """Método constructor, recibe el radio de la esfera. En caso
        de que no sea provisto, este va tomar el valor de 1 por
        defecto."""
        self.radio = radio

    def getRadio(self):
        """Regresa el radio de la esfera"""
        return self.radio

    def volumen(self):
        """Calcula el volumen de la esfera utilizando la formula
        (4*pi*radio**3)/3"""
        return (4 * pi * (self.radio ** 3)) / 3

    def superficie(self):
        """Calcula la superficie de la esfera utilizando la formula
        4*pi*radio**2"""
        return 4 * pi * (self.radio ** 2)


############
# Herencia #
############

class Animal(object):
    nombre = ""


class Perro(Animal):
    color = ""

    def __init__(self, nombre, color):
        self.color = color
        self.nombre = nombre

    def descripcion(self):
        print("El perro {} es de color {} ".format(self.nombre, self.color))


class Gato1(Animal):
    patas = 0

    def __init__(self, nombre, patas=4):
        self.nombre = nombre
        self.patas = patas

    def descripcion(self):
        print("El gato {} tiene {} patas ".format(self.nombre, self.patas))
################
# Polimorfismo #
################


class Persona(object):

    def __init__(self, identificacion, nombre, apellido):
        self.identificacion = identificacion
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return " {}: {} {} ".format(
            self.identificacion, self.apellido, self.nombre)


class Alumno(Persona):

    def __init__(self, identificacion, nombre, apellido, padron):
        Persona.__init__(self, identificacion, nombre, apellido)
        self.padron = padron

    def __str__(self):
        return "{}: {} {}".format(self.padron, self.apellido, self.nombre)


def imprimir(persona):
    print(persona)
