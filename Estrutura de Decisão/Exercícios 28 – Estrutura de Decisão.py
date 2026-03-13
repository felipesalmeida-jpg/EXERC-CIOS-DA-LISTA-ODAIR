tipo = input("Tipo carne (F/A/P): ")
kg = input("Quantidade kg: ")

if kg == "":
    print("Entrada inválida")

else:
    kg = float(kg)

    if tipo.upper() == "F":
        preco = 4.9 if kg <= 5 else 5.8

    elif tipo.upper() == "A":
        preco = 5.9 if kg <= 5 else 6.8

    elif tipo.upper() == "P":
        preco = 6.9 if kg <= 5 else 7.8

    total = kg * preco

    cartao = input("Cartão Tabajara (s/n): ")

    desconto = 0

    if cartao.lower() == "s":
        desconto = total * 0.05

    pagar = total - desconto

    print("Total:", total)
    print("Desconto:", desconto)
    print("Valor a pagar:", pagar)