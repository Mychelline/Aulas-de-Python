
from datetime import date
data_atual = date.today()
ano_atual = data_atual.year
nome = input('Digite seu nome completo: ')
inicio = True

while inicio==True:
    ano_nasc = input('Digite o ano do seu nascimento:')

    try:
        
        if ano_nasc >= 1922 and ano_nasc <= 2021:
            print(nome,'a sua idade é: ', ano_atual - ano_nasc)
            inicio = False
        
        elif ano_nasc == "":
            raise Exception
        else:
            raise Exception
        
    except:
        print ('ERRO, digite um numero entre 1922 a 2022:')


    