a = input("Número 1: ")
b = input("Número 2: ")
op = input("Operação (+ - * /): ")

if a == "" or b == "":
    print("Entrada inválida")

else:
    a = float(a)
    b = float(b)

    if op == "+":
        r = a + b
    elif op == "-":
        r = a - b
    elif op == "*":
        r = a * b
    elif op == "/":
        r = a / b
    else:
        print("Operação inválida")
        r = None

    if r != None:

        print("Resultado:", r)

        if r % 2 == 0:
            print("Par")
        else:
            print("Ímpar")

        if r >= 0:
            print("Positivo")
        else:
            print("Negativo")

        if r == int(r):
            print("Inteiro")
        else:
            print("Decimal")
