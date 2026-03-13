n1 = input("Nota 1: ")
n2 = input("Nota 2: ")
n3 = input("Nota 3: ")

if n1 == "" or n2 == "" or n3 == "":
    print("Entrada inválida")

else:
    n1 = float(n1)
    n2 = float(n2)
    n3 = float(n3)

    media = (n1+n2+n3)/3

    if media == 10:
        print("Aprovado com distinção")

    elif media >= 7:
        print("Aprovado")

    else:
        print("Reprovado")
