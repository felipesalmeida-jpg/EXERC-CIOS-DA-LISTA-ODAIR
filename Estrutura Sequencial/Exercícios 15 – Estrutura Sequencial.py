salario_bruto = float(input("Salário bruto: "))

ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05

total_descontos = ir + inss + sindicato
salario_liquido = salario_bruto - total_descontos

print("Salário Bruto:", salario_bruto)
print("IR:", ir)
print("INSS:", inss)
print("Sindicato:", sindicato)
print("Salário Líquido:", salario_liquido)
