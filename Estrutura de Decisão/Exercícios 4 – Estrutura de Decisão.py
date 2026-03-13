letra = input("Digite uma letra: ")

if letra == "":
    print("Entrada inválida")
else:
    letra = letra.lower()

    if letra in "aeiou":
        print("Vogal")
    else:
        print("Consoante")