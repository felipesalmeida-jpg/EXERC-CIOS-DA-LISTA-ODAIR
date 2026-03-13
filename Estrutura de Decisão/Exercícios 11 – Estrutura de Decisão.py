salario = input("Salário: ")

if salario == "":
    print("Entrada inválida")
else:
    salario = float(salario)

    if salario <= 280:
        p = 0.20
    elif salario <= 700:
        p = 0.15
    elif salario <= 1500:
        p = 0.10
    else:
        p = 0.05

    aumento = salario * p
    novo = salario + aumento

    print("Novo salário:", novo)