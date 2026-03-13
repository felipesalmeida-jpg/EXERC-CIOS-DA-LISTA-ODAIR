s1 = input("String 1: ")
s2 = input("String 2: ")

print("Tamanho 1:", len(s1))
print("Tamanho 2:", len(s2))

if len(s1) == len(s2):
    print("Mesmo tamanho")

if s1 == s2:
    print("Conteúdo igual")
else:
    print("Conteúdo diferente")