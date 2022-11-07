print ("Adivina el número oculto")
import random
numero_oculto = random.randint(1, 10)
numero_usuario = int(input("Ingresa un número del 1 al 10: "))
if numero_usuario > 10 or numero_usuario < 1:
    print("El número debe ser entre 1 y 10")
else:
    if numero_usuario == numero_oculto :
        print("Felicidades, encontraste el número oculto")
    else:
        print("Ese no era l número oculto, el correcto era ", numero_oculto)
print("Fin")