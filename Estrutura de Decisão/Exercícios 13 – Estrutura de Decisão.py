dia = input("Dia (1-7): ")

if dia == "":
    print("Entrada inválida")
else:
    dia = int(dia)

    dias = ["Domingo","Segunda","Terça","Quarta","Quinta","Sexta","Sábado"]

    if 1 <= dia <= 7:
        print(dias[dia-1])
    else:
        print("Valor inválido")