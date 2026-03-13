n = input("Número menor que 1000: ")

if n == "":
    print("Entrada inválida")

else:
    n = int(n)

    c = n // 100
    d = (n % 100) // 10
    u = n % 10

    print(c, "centenas,", d, "dezenas e", u, "unidades")