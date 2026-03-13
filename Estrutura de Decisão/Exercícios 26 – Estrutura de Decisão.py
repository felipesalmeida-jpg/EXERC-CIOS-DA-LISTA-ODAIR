litros = input("Litros: ")
tipo = input("Tipo (A/G): ")

if litros == "":
    print("Entrada inválida")

else:
    litros = float(litros)

    if tipo.upper() == "A":

        preco = 1.9

        if litros <= 20:
            desconto = 0.03
        else:
            desconto = 0.05

    elif tipo.upper() == "G":

        preco = 2.5

        if litros <= 20:
            desconto = 0.04
        else:
            desconto = 0.06

    total = litros * preco
    total = total - (total * desconto)

    print("Total:", total)
