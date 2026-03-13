valor = input("Valor do saque: ")

if valor == "":
    print("Entrada inválida")

else:
    valor = int(valor)

    if valor < 10 or valor > 600:
        print("Valor fora do limite")

    else:

        n100 = valor // 100
        valor = valor % 100

        n50 = valor // 50
        valor = valor % 50

        n10 = valor // 10
        valor = valor % 10

        n5 = valor // 5
        valor = valor % 5

        n1 = valor

        print("Notas de 100:", n100)
        print("Notas de 50:", n50)
        print("Notas de 10:", n10)
        print("Notas de 5:", n5)
        print("Notas de 1:", n1)