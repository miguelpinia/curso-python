#!/usr/bin/env python

booleano = True
booleano2 = "Algo"
booleano3 = ''
booleano4 = ()

# M-w copia el texto seleccionado
# C-w corta el texto seleccionado
# C-y pega el texto copiado/cortado

# C-c C-r : Evalua el texto seleccionado
print True and True

print True and False

print False and True

print False and False

print not True

print not False

print True or True

print True or False

print False or True

print False or False

print 1 < 2

print 2 < 1

print True < False

print False < True

cadena = "foobarbazfoobarbazfoobarbazfoobarbaz"

print cadena.endswith('bar')

print cadena.find('baz')

print "Primer elemento: {0}, segundo elemento: {1}, tercer elemento {2}".format(1, 2, 3)

print ",".join(['a', 'b', 'c'])

print cadena.replace('foo', 'abc')

print cadena

spl = "a,b,c,d,e,f,g"

print spl.split(",")

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

lista.append(10)

lista2 = [11, 12, 13, 14]

lista2.insert(5, 20)

# M - x package - list - packages


tupla = (1, 2, 3)

conjunto = set(['a', 1, 'FOO'])

##############################################
# Conjuntos de trabajadores (ingenieros      #
#                            , programadores #
#                            , managers)     #
##############################################

engineers = set(['Juan', 'Maria', 'Jonas', 'Andres'])
programmers = set(['Jonas', 'Samuel', 'Susana', 'Andres'])
managers = set(['Maria', 'Jonas', 'Susana', 'Pedro'])
employees = engineers | programmers | managers           # union
engineering_management = engineers & managers            # intersección
fulltime_management = managers - engineers - programmers  # diferencia
engineers.add('Marvin')                                  # Agrega
print engineers

employees.issuperset(engineers)     # prueba de superconjunto

employees.update(engineers)         # actualizando desde otro conjunto
employees.issuperset(engineers)

for group in [engineers, programmers, managers, employees]:
    group.discard('Susana')          # Eliminación incodicional
    print group

################
# Diccionarios #
################

a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})

a == b == c == d == e

print "La longitud de a es: ", len(a), " :D ", 4

print "La longitud de a es: " + str(len(a)) + " :D " + str(4)

print "La longitud de a es: {0} :D {1}".format(len(a), 4)
