p1 = input("R$: 150,00")
p2 = input("R$: 200,00")
p3 = input("R$: 100,00")

if p1 == "" or p2 == "" or p3 == "":
    print("150,00" or "200,00" or "100,00")
else:
    p1 = float(p1)
    p2 = float(p2)
    p3 = float(p3)

    menor = min(p1,p2,p3)

    print("Comprar produto de preço:", menor)