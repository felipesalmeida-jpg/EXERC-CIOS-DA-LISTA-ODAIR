a = input("5")
b = input("12")
c = input("90")

if a == "" or b == "" or c == "":
    print("5" or "12" or "90")
else:
    lista = [float(a), float(b), float(c)]
    lista.sort(reverse=True)

    print(lista)
