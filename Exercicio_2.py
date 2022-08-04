#qtd_rodas = 4
#peso_bruto = 6001
#qtd_pessoas = 4

qtd_rodas = int (input('Quantas rodas do veículo tem?'))
peso_bruto = int (input('Qual o peso bruto do veículo?'))
qtd_pessoas = int (input('Quantidade de pessoas no veículo?'))

if  qtd_rodas == 2 or qtd_rodas == 3 :
    print('Veículos com duas ou três rodas - categoria A')
elif qtd_rodas == 4 and qtd_pessoas <= 8 and peso_bruto <= 3500:
    print('Veículos com quatro rodas, que acomodam até oito pessoas e seu peso é de até 3500 kg - categoria B')
elif qtd_rodas >= 4 and 3500 <= peso_bruto <= 6000:
    print('Veículos com quatro rodas ou mais e com peso entre 3500 e 6000 kg - categoria C')
elif qtd_rodas >= 4 and qtd_pessoas > 8:
    print('Veículos com quatro rodas ou mais e que acomodam mais de oito pessoas - categoria D')
elif qtd_rodas >= 4 and peso_bruto > 6000:
    print('Veículos com quatro rodas ou mais e com mais de 6000 kg - categoria E')
else:
    print('Esse veículo não existe')