tamanho_gb = float(input('Digite o tamanho do arquivo em GBs: '))
tamanho_mb = tamanho_gb * 1_024
tamanho_kb = tamanho_gb * 1_024 * 1_024
print(f'O arquivo tem {tamanho_mb:.2f}MBs ou {tamanho_kb:.2f}KBs.')