#!/usr/bin/env python
# -*- coding: utf-8 -*-


def superior(interna):
    def f1():
        print "Función 1"

    def f2():
        print "Funcion 2"
    funcion = {"uno": f1, "dos": f2}
    return funcion[interna]


def f11():
    print "Función 1"


def f22():
    print "Funcion 2"


def superior1(funcion):
    funcion()

superior(f11)
superior(f22)

cuadrado = lambda x: x ** 2

print cuadrado(2)

lista = range(10)
for numero in lista:
    print cuadrado(numero)


def make_incrementor(n): return lambda x: x + n

f = make_incrementor(2)
g = make_incrementor(6)
print f(42), g(42)
print make_incrementor(22)(33)

nums = range(2, 50)
for i in range(2, 8):
    nums = filter(lambda x: x == i or x % i, nums)
print nums

[numero ** 2 for numero in range(10)]

[numero for numero in range(20) if numero % 2 == 0]

[[0 for i in range(3)] for j in range(3)]

oracion = "El zorro café salta rápidamente sobre el perro perezoso."
palabra_longitud = [len(palabra)
                    for palabra in oracion.split() if palabra.upper() != "EL"]


def recorre(lista):
    while True:
        for n in lista:
            yield n

gen = recorre([1, "a", 2, "hola"])

gen.next()

gen_pares = (p for p in range(20) if p % 2 == 0)

gen_pares.next()

##########
# Primos #
##########


def es_primo(numero):
    if numero > 1:
        if numero == 2:
            return True
        if numero % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(numero) + 1), 2):
            if numero % current == 0:
                return False
        return True
    return False


def obten_primos(numero=0):
    while True:
        if es_primo(numero):
            yield numero
        numero += 1

f = obten_primos()

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

lista_nueva = map(lambda x: x ** 3, lista)

print lista_nueva

import commands
from functools import reduce
mount = commands.getoutput('mount -v')
lines = mount.splitlines()
points = map(lambda line: line.split()[2], lines)
print points


def foo(x):
    return x.split()[2]

print map(foo, commands.getoutput('mount -v').splitlines())

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
suma = reduce(lambda x, y: x + y, lista)
print suma

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
pares = filter(lambda x: x % 2 == 0, lista)
print pares

animal = ["conejo", "gato", "liebre", "oruga", "pajaro"]
nombre = ["blanco", "de chesire", "de marzo", "azul", "dodo", "Foo"]
personajes = zip(animal, nombre)
print personajes
