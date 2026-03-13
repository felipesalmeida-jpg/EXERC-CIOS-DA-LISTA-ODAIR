import math

area = float(input("Área em m²: "))

litros = area / 3
latas = math.ceil(litros / 18)

preco = latas * 80

print("Latas necessárias:", latas)
print("Preço total:", preco)