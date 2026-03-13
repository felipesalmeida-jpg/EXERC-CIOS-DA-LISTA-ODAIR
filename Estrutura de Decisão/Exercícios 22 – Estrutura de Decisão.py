n = input("Número: ")

if n == "":
    print("Entrada inválida")

else:
    n = int(n)

    if n % 2 == 0:
        print("Par")
    else:
        print("Ímpar")