#Ejercicio final

import random

titulo = "Escapa de la Prisión"

numero = random.randint(1,100)

resultado = 13 * numero

print("\n" + titulo + "\n")

start = input("Presiona intro para empezar....")

print("Has sido capturado en una prisión desconocida")

print("Logras escapar y encuentras un pasillo por el cual puedes ir")

camino_1= input("Encuentras un cámino que lleva a un depósito, pero hay un guardia armado, decides...""\n"

"\n""a- Correr e intentar perderlo""\n" # Camino correcto

"\n""b- intentar ocultarte""\n") # Muerte

if camino_1 == "a":

    print("Logras escapar del guardia, sigues tu cámino y ")

    Cam_1_2= input("Llegas a un callejón, por un lado vez un camino estrecho y largo hasta una puerta al final""\n"

    "En el otro lado hay una alcantarilla, qué cámino tomas?""\n"

    "a- Corres e intentas llegar a la puerta""\n" #camino facil.

    "b- Entras a la alcantarilla""\n") # camino dificil.

    if Cam_1_2 == "a":

        print("Intentas llegar al final de la puerta, pero eres capturado por el guardia")

        print("Eres capturado por el guardia""\n", "PERDISTE")

        exit()

    elif Cam_1_2 == "b":

        print("Logras entrar a la alcantarilla")

        palo = input("En la alcantarilla encuentras una palanca y a lo lejos vez un interruptor""\n"

        "a- colocas el palo en el interruptor?""\n"

        "b- Guardas el palo por si acaso y decides seguir""\n"

        ": ")

        if palo == "a":

            print("Logras encender las luces en todo el tunel")

            print("Caminas en el pasillo oscuro")

            print("------------------------------------------------------------------")

            print("Encuentras a un hombre en muy mal estado al final del pasillo oscuro""\n"

            "Al pasar alado del hombre, este se avalanza hacía amenazandote y te hace una pregunta""\n"

            "RESPONDE: CUANTO ES 13 *", numero )

            resp = int(input(": "))

            if resp == resultado:

                print("Al hombre no le gustó que hayas acertado su pregunta...""\n"

                "HAS MUERTO...")

                exit()

            else:

                print("El hombre te sonrie y te dice""\n"

                "sigueme...""\n"

                "El hombre te señala un camino""\n" "Observas una puerta que parece abierta al final de pasillo""\n"
                      
                "Abres la puerta, al entrar un guardia te ve y se abalanza hacia ti.. no tienes con que defenderte"
                      
                "\n""El guardia te da un fuerte golpe y...""\n"

                "PERDISTE")

        else:

            print("Caminas en el pasillo oscuro")

            print("------------------------------------------------------------------")

            print("Sientes que alguien esta detrás de ti...""\n" "El hombre te dice""\n"

            "RESPONDE: CUANTO ES 13 *", numero )

            resp = int(input(": "))

            if resp == resultado:

                print("Al hombre no le gustó que hayas acertado su pregunta...""\n"

                "HAS MUERTO...")

                exit()

            else:

                print("El hombre te sonrie y te dice""\n"

                "sigueme...""\n"

                "El hombre te señala el camino hasta el final..""\n" "Observas una puerta al final del tunel""\n"

                "Abres la puerta, al entrar un GUARDIA te ve y se abalanza hacia ti.. buscas algo para golpearlo,""\n" 

                "recuerdas que tienes el palo y logras noquearlo...""\n" "Logras encontrar una salida y...""\n"

                "GANASTE")

elif camino_1 == "b":

    print("Te intentaste ocultastar, sin embargo, el guardia te vio, te golpeo y te encerraron nuevamente...")

    print("PERDISTE")

    exit()