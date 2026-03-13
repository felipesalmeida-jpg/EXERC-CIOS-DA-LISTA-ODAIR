data = input("Data (dd/mm/aaaa): ")

if data == "":
    print("Entrada inválida")

else:
    try:
        d, m, a = data.split("/")

        d = int(d)
        m = int(m)
        a = int(a)

        if 1 <= d <= 31 and 1 <= m <= 12:
            print("Data válida")
        else:
            print("Data inválida")

    except:
        print("Formato inválido")