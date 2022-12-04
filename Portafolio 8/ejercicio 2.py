punto = 0
coma = 0
espacio= 0
texto = input("Introduzca su texto:")
for a in texto:
    if a == ".":
        punto += 1
    elif a == ",":
        coma += 1
    else:
        espacio += 1

print("Su texto posee "+ str(punto) + " puntos")
print("Su texto posee "+ str(coma) + " comas")
print("Su texto posee "+ str(espacio) + " espacios")