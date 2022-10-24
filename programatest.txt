import random

titulo = "Bienvenido al test de primaria"
print("\n" + titulo + "\n" + "-" * len(titulo) + "\n")
print("Preguntas")

numero1 = (random.randint(1, 10))
numero2 = (random.randint(1, 10))

puntuacion = 0

opcion = input("Pregunta 1: Cuánto es {} multiplicado por {}?\n"
            "A - {}\n"
            "B - {}\n"
            "C - {}\n"
            .format((numero1), (numero2), (numero1 * numero2), (numero2 + numero1), (numero1 - numero2)))

if opcion == "A":
    puntuacion = puntuacion + 20
    print("respuesta correcta")
elif opcion == "B":
    puntuacion = puntuacion + 0
    print("respuesta incorrecta")
elif opcion == "C":
    puntuacion = puntuacion + 0
    print("respuesta incorrecta")
else:
    print("La opcion no es valida!")


opcion2 = input("Pregunta 2: Cuándo se descubrió america?\n"
            "A - 1490\n"
            "B - 1492\n"
            "C - 1501\n")

if opcion2 == "B":
    puntuacion = puntuacion + 20
    print("respuesta correcta")
elif opcion2 == "A":
    puntuacion = puntuacion + 0
    print("respuesta incorrecta")
elif opcion2 == "C":
    puntuacion = puntuacion + 0
    print("respuesta incorrecta")
else:
    print("La opcion no es valida!")
    exit()

opcion3 = input("Pregunta 3: Cuáles de estas no contiene partes de una célula?\n"
            "A - Lisosomas, Ribosomas y Citoplasma\n"
            "B - Ribosoma, Centriolos y Mitocondria\n"
            "C - Aparato de golgi, Ribosomas y Ateriola \n")

if opcion3 == "C":
    puntuacion = puntuacion + 20
    print("respuesta correcta")
elif opcion3 == "A":
    puntuacion = puntuacion + 0
    print("respuesta incorrecta")
elif opcion3 == "B":
    puntuacion = puntuacion + 0
    print("respuesta incorrecta")
else:
    print("La opcion no es valida!")
    exit()

if puntuacion == 0:
    print("No tuviste ninguna respuesta correcta")
if puntuacion == 20:
    print("Te falta repasar")
if puntuacion == 40:
    print("Obtuviste casi todas las respuestas correctas")
if puntuacion == 60:
    print("Tuviste todas las respuestas correctas")