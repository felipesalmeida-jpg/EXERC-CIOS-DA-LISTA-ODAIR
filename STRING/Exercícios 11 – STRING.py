import random

palavras = ["python","dados","algoritmo"]

palavra = random.choice(palavras)

print("Adivinhe a palavra")

resp = input()

if resp == palavra:
    print("Acertou")
else:
    print("Errou. Era:", palavra)