data = input("Data (dd/mm/aaaa): ")

try:

    dia, mes, ano = data.split("/")

    meses = [
    "Janeiro","Fevereiro","Março","Abril","Maio","Junho",
    "Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"
    ]

    print(dia,"de",meses[int(mes)-1],"de",ano)

except:
    print("Data inválida")
