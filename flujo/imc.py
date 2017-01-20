#!/usr/bin/env python3

print("Bienvenido a la calculadora de Índice de Masa Corporal\n")
estatura = float(input("Dame tu estatura en metros: "))
masa = float(input("Dame tu peso en kilogramos: "))
imc = masa / (estatura ** 2)

if imc < 18.5:
    print("Tu imc es: {} y tienes bajo peso\n".format(imc))
elif 18.5 <= imc <= 24.99:
    print("Tu imc es: {} y tienes peso normal\n".format(imc))
elif 25 <= imc <= 30:
    print("Tu imc es: {} y tienes sobrepeso\n".format(imc))
else:
    print("Tu imc es: {} y tienes obesidad\n".format(imc))


for x in range(1, 11):
    print("==================")
    for y in range(1, 11):
        print('{} * {} = {}'.format(x, y, x * y))

for x in range(10):
    print(x)
    if x == 1:
        break

for x in range(3):
    print(x)
else:
    print('Final x = {}'.format(x))

string = "Hello World"
for x in string:
    print(x)

collection = ['hey', 5, 'd']
for x in collection:
    print(x)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix_2 = matrix[:]

matrix_3 = []

for i in range(len(matrix)):
    matrix_3.append([])
    for j in range(len(matrix[i])):
        matrix_3[i].append(matrix[i][j] + matrix_2[i][j])
