nome = input("Nome: ")

if nome == "":
    print("Entrada inválida")
else:
    print(nome[::-1].upper())
