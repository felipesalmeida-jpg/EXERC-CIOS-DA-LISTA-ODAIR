import random

palavra = "python"

lista = list(palavra)

random.shuffle(lista)

print("".join(lista))