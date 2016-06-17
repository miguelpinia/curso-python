#!/usr/bin/env python
# -*- coding: utf-8 -*-

print "Bienvenido a la calculadora de Índice de Masa Corporal\n"
estatura = float(raw_input("Dame tu estatura en metros: "))
masa = float(raw_input("Dame tu peso en kilogramos: "))

imc = masa / (estatura ** 2)

if imc < 18.5:
    print "Tu imc es: {0} y tienes bajo peso\n".format(imc)
elif 18.5 <= imc <= 24.99:
    print "Tu imc es: {0} y tienes peso normal\n".format(imc)
elif 25 <= imc <= 30:
    print "Tu imc es: {0} y tienes sobrepeso\n".format(imc)
else:
    print "Tu imc es: {0} y tienes obesidad\n".format(imc)
