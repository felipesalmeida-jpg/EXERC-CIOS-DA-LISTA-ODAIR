morango = input("Kg morango: ")
maca = input("Kg maçã: ")

if morango == "" or maca == "":
    print("Entrada inválida")

else:
    morango = float(morango)
    maca = float(maca)

    if morango <= 5:
        pm = 2.5
    else:
        pm = 2.2

    if maca <= 5:
        pa = 1.8
    else:
        pa = 1.5

    total = morango * pm + maca * pa

    if morango + maca > 8 or total > 25:
        total = total * 0.9

    print("Total:", total)