valor = input("Valor hora: ")
horas = input("Horas: ")

if valor == "" or horas == "":
    print("Entrada inválida")
else:
    valor = float(valor)
    horas = float(horas)

    salario = valor * horas

    print("Salário bruto:", salario)