#!/usr/bin/python3

cadena = "((((()))((((((()))))((()))(()())))((()))))))))))))))))"
lista = list(cadena)
pila = []
numPI = lista.count('(')
numPD = lista.count(')')
if numPI != numPD:
    print("Los paréntesis no están bien balanceados")
else:
    for valor in lista:
        if valor == '(':
            pila.append(valor)
        elif valor == ')' and len(pila) > 0:
            pila.pop()

if len(pila) == 0:
    print("Los paréntesis están bien balanceados")
