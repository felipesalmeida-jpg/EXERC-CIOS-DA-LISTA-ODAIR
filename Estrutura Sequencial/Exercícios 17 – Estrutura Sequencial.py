import math

area = float(input("Área em m²: "))

area = area * 1.10
litros = area / 6

latas = math.ceil(litros / 18)
galoes = math.ceil(litros / 3.6)

preco_latas = latas * 80
preco_galoes = galoes * 25

print("Apenas latas:", latas, "Preço:", preco_latas)
print("Apenas galões:", galoes, "Preço:", preco_galoes)