#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Foo:
    a = 1
    b = "Soy Foo"


class Gato:
    numero_de_patas = 0
    color = "negro"

    def __init__(self, nombre="Juan"):
        self.nombre = nombre

    def dormir(self):
        print "Zzzz..."

    def molestar_humano(self):
        while True:
            acariciar = raw_input("Acariciame ")
            if acariciar == "Acariciado":
                break

gato = Gato()
gato.numero_de_patas = 4
gato.color = "marron"

print "El gato tiene " + str(gato.numero_de_patas) + " patas y es de color " + gato.color

print "El gato " + gato.nombre + " tiene " + str(gato.numero_de_patas) + " patas y es de color " + gato.color

################################
# Implementación de la esfera. #
################################

from math import pi


class Esfera:
    """Implementación de una clase que representa una esfera en python. Define
los métodos:
  - getRadio(self) :: Regresa el radio de la esfera
  - superficie(self) :: Regresa el valor total de la superficie de la esfera
  - volumen(self) :: Regresa el volumen total de la esfera
    """

    def __init__(self, radio=1):
        """Método constructor, recibe el radio de la esfera. En caso de que no
        sea provisto, este va tomar el valor de 1 por defecto."""
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
        print "El perro " + self.nombre + " es de color: " + self.color


class Gato1(Animal):
    patas = 0

    def __init__(self, nombre, patas=4):
        self.nombre = nombre
        self.patas = patas

    def descripcion(self):
        print "El gato " + self.nombre + " tiene " + str(self.patas) + " patas"

################
# Polimorfismo #
################


class Persona(object):

    def __init__(self, identificacion, nombre, apellido):
        self.identificacion = identificacion
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return " %s: %s, %s" % (str(self.identificacion),
                                self.apellido, self.nombre)


class Alumno(Persona):

    def __init__(self, identificacion, nombre, apellido, padron):
        Persona.__init__(self, identificacion, nombre, apellido)
        self.padron = padron
    def __str__(self):
        return " %s: %s, %s" % (str(self.padron), self.apellido, self.nombre)


def imprimir(persona):
    print persona
