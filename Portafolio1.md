Curso: Aprende a programar con Python 
MasterMind Módulo 1 Primeros pasos:

La programación es una forma en la que nos podemos comunicar con las máquinas y esto lo podemos llegar a hacer con lenguajes como python, los cuales nos sirven como interpretes para poder comunicarnos con esta.

Programa 1:

print("Programa que te diga cual numero es el mayor y el menor")

num1 = int(input("Introduce el numero 1: ")) num2 = int(input("Introduce el numero 2: ")) num3 = int(input("Introduce el numero 3: "))

print("De los numeros {}, {} y {} el numero mas grande es {} y el numero mas pequeño es {}".format(num1, num2, num3, max(num1, num2, num3), min(num1, num2, num3)))

Programa 2:

print("Programa que convierta los grados fahrenheit a celsius: ")

gradosf = float(input("Introduzca los grados fahrenheit: "))

print("{} grados fahrenheit son: {} celsius ".format(gradosf, (gradosf - 32)/1.8))

print("Programa que convierta de pesos a dolares: ")

pesos = float(input("Introduzca los pesos: "))

print("{} pesos son {} dolares".format(pesos, (pesos*20.12)))
