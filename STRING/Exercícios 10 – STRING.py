n = input("Número (0-9): ")

if n == "":
    print("Entrada inválida")

else:

    numeros = ["zero","um","dois","três","quatro","cinco","seis","sete","oito","nove"]

    n = int(n)

    print(numeros[n])