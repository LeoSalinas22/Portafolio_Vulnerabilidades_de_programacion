from random import randint

vida_pikachu = 80
vida_squirtle = 90

vida_actual_pikachu = 80
vida_actual_squirtle = 90

while vida_actual_pikachu > 0 and vida_actual_squirtle > 0:

    #sigan peleando

    #turno pikachu
    print("turno de pikachu")
    ataque_pikachu = randint(1, 2)
    if ataque_pikachu == 1:
        #bola  voltio
        print("pikachu ataca con vola voltio")
        vida_actual_squirtle -= 10
    else:
        print("pikachu ataca con onda trueno")
        vida_actual_squirtle -= 15

    print("la vida de picachu es [{}], \n la vida de squirtle es [{}]".format(vida_pikachu* vida_actual_pikachu // 100 * "#" ,
                                                                          vida_squirtle * vida_actual_squirtle // 100 * "#"))

    input("enter para continuar...")

    #turno squirtle

    print("turno squirtle")

    ataque_squirtle = None

    while ataque_squirtle != "P" and ataque_squirtle != "A" and ataque_squirtle != "B":
        ataque_squirtle = input("que ataque deseas realizar? [P] placaje, [A]gua , [B]urbuj:")
    if ataque_squirtle == "P":
        print("Ataca con placaje")
        vida_actual_pikachu -= 10
    elif ataque_squirtle == "A":
        print("Ataca con agua")
        vida_actual_pikachu -= 12
    elif ataque_squirtle == "B":
        print("Ataca con burbuja")
        vida_actual_pikachu -= 20

    print("la vida de picachu es {}, \n la vida de squirtle es {}".format(vida_pikachu *vida_actual_pikachu // 100 * "#",
                                                                          vida_squirtle *vida_actual_squirtle // 100 * "#"
                                                                          ))
    input("enter para continuar...\n\n")

if vida_actual_pikachu > vida_actual_squirtle:
    print("pikachu gana!")

else:
    print("gana squirtle!")