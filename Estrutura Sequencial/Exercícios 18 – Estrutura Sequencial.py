tamanho = float(input("Tamanho do arquivo (MB): "))
velocidade = float(input("Velocidade da internet (Mbps): "))

tempo_segundos = (tamanho * 8) / velocidade
tempo_minutos = tempo_segundos / 60

print("Tempo aproximado em minutos:", tempo_minutos)