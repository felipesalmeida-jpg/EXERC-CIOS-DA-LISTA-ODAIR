n = input("Número: ")

if n == "":
    print("Entrada inválida")

else:
    n = float(n)

    if n == int(n):
        print("Inteiro")
    else:
        print("Decimal")