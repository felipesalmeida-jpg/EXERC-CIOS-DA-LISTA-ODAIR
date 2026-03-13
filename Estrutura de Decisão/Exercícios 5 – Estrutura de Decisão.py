n1 = input("Nota 1: ")
n2 = input("Nota 2: ")

if n1 == "" or n2 == "":
    print("Entrada inválida")
else:
    n1 = float(n1)
    n2 = float(n2)

    media = (n1 + n2) / 2

    if media == 10:
        print("Aprovado com distinção")
    elif media >= 7:
        print("Aprovado")
    else:
        print("Reprovado")
