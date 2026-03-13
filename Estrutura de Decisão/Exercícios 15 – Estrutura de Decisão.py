a = input("Lado A: ")
b = input("Lado B: ")
c = input("Lado C: ")

if a == "" or b == "" or c == "":
    print("Entrada inválida")
else:
    a = float(a)
    b = float(b)
    c = float(c)

    if a + b > c and a + c > b and b + c > a:

        if a == b and b == c:
            print("Triângulo equilátero")

        elif a == b or a == c or b == c:
            print("Triângulo isósceles")

        else:
            print("Triângulo escaleno")

    else:
        print("Não forma triângulo")