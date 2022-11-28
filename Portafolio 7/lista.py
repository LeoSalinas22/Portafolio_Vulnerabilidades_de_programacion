lista = []

primera_cosa = None

while primera_cosa != "Q":
    primera_cosa = input("¿Qué deseas añadir a tu lista? [Q para salir]:")

    if primera_cosa == "Q":
        print("Tu lista es:\n"
              "{}".format(lista))
        exit()

    if primera_cosa in lista:
        print(primera_cosa + " ya está en tu lista.")

    else:
        s_n = input("¿Estas seguro que deseas añadir " + primera_cosa + " a tu lista? [S/N]")

        if s_n == "S":
            print("Has añadido " + primera_cosa + " a tu lista.")
            lista.append(primera_cosa)

        elif s_n == "N":
            print("No has añadido " + primera_cosa + " a tu lista.")