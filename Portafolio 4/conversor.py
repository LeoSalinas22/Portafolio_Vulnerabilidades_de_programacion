titulo = "Conversor de moneda"
print("\n" + titulo + "\n" + "-" * len(titulo) + "\n")

# Valores de la moneda
valor_dolar_euro = 1.01
valor_euro_dolar = 0.99
valor_libra_euro = 1.14
valor_euro_libra = 0.88

opcion = input("Qué moneda quieres convertir?\n"
               "A = Dolar a Euro\n"
               "B = Euro a Dolar\n"
               "C = Libra a Euro\n"
               "D = Euro a Libra\n"
               "R/ ")

if opcion =="A":
    dolares_a_euros = float(input("\n""Qué cantidad de dolares quieres convertir a euros?\n"
                  "R/ "))
elif opcion == "B":
        euros_a_dolares = float(input("\n""Qué cantidad de euros quieres convertir a dolares?\n"
                  "R/ "))
elif opcion == "C":
        libras_a_euros = float(input("\n""Qué cantidad de libras quieres convertir a euros?\n"
                  "R/ "))
elif opcion == "D":
    euro_a_libra = float(input("\n""Qué cantidad de euros quieres convertir a libras?\n"
                               "R/ "))
else:
    print("Las respuestas posibles son a, b y c")
    exit()

if opcion == "A":
    print("\n""La cantidad de euros es {}".format(dolares_a_euros * valor_dolar_euro))
elif opcion == "B":
    print("\n""La cantidad de dolares es {}".format(euros_a_dolares * valor_euro_dolar))
elif opcion == "C":
    print("\n""La cantidad de euros es {}".format(libras_a_euros * valor_libra_euro))
elif opcion == "D":
    print("\n""La cantidad de libras es {}".format(euro_a_libra * valor_euro_libra))

print("\n" "Fin del programa")