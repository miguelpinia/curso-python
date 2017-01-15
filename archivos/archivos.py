#!/usr/bin/env python
# -*- coding: utf-8 -*-

archivo = open("/tmp/lorem.txt", 'r+')
contenido = archivo.read()
print contenido

archivo = open("/tmp/lorem.txt", 'r+')
linea = archivo.readline()


archivo = open("/tmp/lorem.txt", 'r+')
for linea in archivo.readlines():
    print "---------------------"
    print linea
    print "---------------------"

archivo.seek(0)

archivo = open("/tmp/lorem.txt", 'r+')
linea1 = archivo.readline()
mas = archivo.read(archivo.tell() * 2)
print mas
if archivo.tell() > 20:
    archivo.seek(20)
    print archivo.readline()


archivo = open("/tmp/lorem.txt", "r+")
contenido = archivo.read()
final_de_archivo = archivo.tell()
archivo.write('Nueva linea')
archivo.seek(final_de_archivo)
nuevo_contenido = archivo.read()
print nuevo_contenido
