a = input("Primeiro número: ")
b = input("Segundo número: ")

if a == "" or b == "":
    print("Entrada inválida")
else:
    a = float(a)
    b = float(b)

    if a > b:
        print("Maior:", a)
    else:
        print("Maior:", b)