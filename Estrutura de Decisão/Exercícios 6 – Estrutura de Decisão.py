a = input("Primeiro número: ")
b = input("Segundo número: ")
c = input("Terceiro número: ")

if a == "" or b == "" or c == "":
    print("Entrada inválida")
else:
    a = float(a)
    b = float(b)
    c = float(c)

    maior = a

    if b > maior:
        maior = b

    if c > maior:
        maior = c

    print("Maior:", maior)