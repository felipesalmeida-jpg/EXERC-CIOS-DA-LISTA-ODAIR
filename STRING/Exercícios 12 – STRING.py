tel = input("Telefone: ")

tel = tel.replace("-","")

if len(tel) == 7:
    tel = "3" + tel

print(tel[:4] + "-" + tel[4:])