n = input("Número: ")

if n == "":
    print("Entrada inválida")
else:
    n = float(n)

    if n >= 0:
        print("Positivo")
    else:
        print("Negativo")