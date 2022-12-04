numero = int(input("Numero a multiplicar: "))

print("Tabla de multiplicar:")
for n in range (1, 11):
    #if n % 2 == 0:
        print("{} x {} = {}".format(numero, n, n * numero))

print("Tabla de divicion:")
for n in range (1, 11):
    print("{} / {} = {}".format(numero, n, n % numero))