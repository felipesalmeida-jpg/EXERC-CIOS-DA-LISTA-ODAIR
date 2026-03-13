sexo = input("Digite F ou M: ")

if sexo == "":
    print("Entrada inválida")
else:
    sexo = sexo.upper()

    if sexo == "F":
        print("Feminino")
    elif sexo == "M":
        print("Masculino")
    else:
        print("Sexo inválido")