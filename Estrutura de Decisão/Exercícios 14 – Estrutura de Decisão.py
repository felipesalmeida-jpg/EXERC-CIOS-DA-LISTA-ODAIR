n1 = input("Nota 1: ")
n2 = input("Nota 2: ")

if n1 == "" or n2 == "":
    print("Entrada inválida")
else:
    n1 = float(n1)
    n2 = float(n2)

    media = (n1+n2)/2

    if media >= 9:
        conceito="A"
    elif media >= 7.5:
        conceito="B"
    elif media >= 6:
        conceito="C"
    elif media >= 4:
        conceito="D"
    else:
        conceito="E"

    print("Conceito:", conceito)