cpf = input("CPF: ")

cpf = cpf.replace(".","").replace("-","")

if len(cpf) == 11 and cpf.isdigit():
    print("Formato válido")
else:
    print("CPF inválido")