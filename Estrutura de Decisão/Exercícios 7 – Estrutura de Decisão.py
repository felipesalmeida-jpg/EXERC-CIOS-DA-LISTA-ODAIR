a = input("Primeiro número: ")
b = input("Segundo número: ")
c = input("Terceiro número: ")

if a == "" or b == "" or c == "":
    print("Entrada inválida")
else:
    a = float(a)
    b = float(b)
    c = float(c)

    maior = max(a,b,c)
    menor = min(a,b,c)

    print("Maior:", maior)
    print("Menor:", menor)