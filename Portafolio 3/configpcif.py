titulo = print("\n" + "Elíge que configuración para tu PC quieres" + "\n" )

opcion_cpu = input("Elíge que marca de procesador quieres (Intel / AMD)" "\n")

#Texto para modificar las preguntas y respuestas
texto = "Elíge la gama (A = Muy alta / B = Alta / C = Media / D = Baja)" + "\n"
texto2 = "Elíge la gama (A = Extrema / B = Muy alta / C = Alta / D = Media / E = Baja)" + "\n"
texto_sin_elegir = "Elíge entre A / B / C / D"
texto_sin_elegir2 = "Elíge entre A / B / C / D / E"

#Opción de procesador Intel
if opcion_cpu == "Intel":
    opcion_cpu = input(texto)

    if opcion_cpu == "A":
        opcion_cpu = "I9 13900k"
    elif opcion_cpu == "B":
        opcion_cpu = "I7 13700k"
    elif opcion_cpu == "C":
        opcion_cpu = "I5 13600"
    elif opcion_cpu == "D":
        opcion_cpu = "I3 13100f"
    else:
        print(texto_sin_elegir)

#Opción de procesador AMD
elif opcion_cpu == "AMD":
    opcion_cpu = input(texto)

    if opcion_cpu == "A":
        opcion_cpu = "Ryzen 9 7900X"
    elif opcion_cpu == "B":
        opcion_cpu = "Ryzen 7 7800X"
    elif opcion_cpu == "C":
        opcion_cpu = "Ryzen 5 7600X"
    elif opcion_cpu == "D":
        opcion_cpu = "Ryzen 7 7300"
    else:
        print(texto_sin_elegir)

#Opción de Tarjeta Gráfica
opcion_gpu = input("Elíge que marca de tarjeta gráfica quieres (Nvidia / AMD)" "\n")

#Opción de Gráfica Nvidia
if opcion_gpu == "Nvidia":
    opcion_gpu = input(texto2)

    if opcion_gpu == "A":
        opcion_gpu = "RTX 4090"
    elif opcion_gpu == "B":
        opcion_gpu = "RTX 4080"
    elif opcion_gpu == "C":
        opcion_gpu = "RTX 4070"
    elif opcion_gpu == "D":
        opcion_gpu = "RTX 4060"
    elif opcion_gpu == "D":
        opcion_gpu = "RTX 4050"
    else:
        print(texto_sin_elegir2)


#Opción de Gráfica AMD
elif opcion_gpu == "AMD":
    opcion_gpu = input(texto)

    if opcion_gpu == "A":
        opcion_gpu = "RX 7950"
    elif opcion_gpu == "B":
        opcion_gpu = "RX 7800"
    elif opcion_gpu == "C":
        opcion_gpu = "RX 7700"
    elif opcion_gpu == "D":
        opcion_gpu = "RX 7600"
    elif opcion_gpu == "E":
        opcion_gpu = "RX 7500"
    else:
        print(texto_sin_elegir2)


print("\n" + "Esta es la configuración de PC que te recomendamos: " + "\n" + format(opcion_cpu) + "\n" + format(opcion_gpu))