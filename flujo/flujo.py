#!/usr/bin/env python
# -*- coding: utf-8 -*-

x = int(raw_input("Ingresa un entero: "))

if x < 0:
    x = 0
    print 'Número negativo cambiado a cero'
elif x == 0:
    print 'Cero'
elif x == 1:
    print 'Uno'
else:
    print 'Más'
