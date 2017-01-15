#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Programa que imprima los 25 primeros numeros naturales
n = 1
while n <= 25:
    print n,
    n += 1

# Imprimir los numeros impares desde el 1 al 25, ambos inclusive
n = 1
h = ''

while n <= 25:
    if n % 2 != 0:
        h += ' %i' % n
    n += 1

print h


# Introducir dos valores A y B:
# Si A>=B, calcular e imprimir la suma 10+14+18+...+50
# Si A/B<=30, calcular e imprimir el valor de (A^2+B^2)
try:
    a = int(raw_input('Primer valor: '))
    b = int(raw_input('Segundo valor: '))
    n = 10
    suma = 0
    sumas = 0
    if a >= b:
        while n <= 50:
            suma += n
            n += 4
            print suma
    if a / b <= 30:
        sumas = (a**2 + b**2)
        print sumas
except ValueError:
    print 'Número inválido'
