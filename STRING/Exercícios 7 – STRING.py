frase = input("Frase: ").lower()

espacos = frase.count(" ")

vogais = 0

for v in "aeiou":
    vogais += frase.count(v)

print("Espaços:", espacos)
print("Vogais:", vogais)