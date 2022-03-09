arquivo = int(input('Digite o tamanho do arquivo em MB: '))
velocidade = float(input('Qual a velocidade da internet em Mbps: '))
tempo = (arquivo/velocidade)/60
print(f'Tempo aproximado de download: {tempo:.2f} minutos')
