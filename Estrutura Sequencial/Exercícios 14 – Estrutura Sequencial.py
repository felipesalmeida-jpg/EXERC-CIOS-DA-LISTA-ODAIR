peso = float(input("Informe o peso de peixes (kg): "))

limite = 50
valor_multa = 4

if peso > limite:
    excesso = peso - limite
    multa = excesso * valor_multa
else:
    excesso = 0
    multa = 0

print(f"Peso informado: {peso} kg")
print(f"Excesso: {excesso} kg")
print(f"Multa a pagar: R$ {multa:.2f}")