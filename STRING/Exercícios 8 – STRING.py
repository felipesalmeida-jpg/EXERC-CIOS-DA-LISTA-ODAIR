texto = input("Texto: ")

t = texto.replace(" ","").lower()

if t == t[::-1]:
    print("Palíndromo")
else:
    print("Não é palíndromo")