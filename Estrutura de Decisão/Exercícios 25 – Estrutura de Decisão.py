respostas = 0

for i in range(5):

    r = input("Resposta (s/n): ")

    if r.lower() == "s":
        respostas += 1

if respostas == 2:
    print("Suspeita")

elif respostas == 3 or respostas == 4:
    print("Cúmplice")

elif respostas == 5:
    print("Assassino")

else:
    print("Inocente")