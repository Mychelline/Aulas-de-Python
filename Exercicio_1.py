nome = str(input('Digite o seu nome?'))
nota1 = float(input('Escreva sua primeira nota: '))
nota2 = float(input('Escreva sua segunda nota: '))
nota3 = float(input('Escreva sua terceira nota: '))

falta = int(input('Quantas vezes você faltou? '))

media: float = (nota1 + nota2 + nota3) / 3
print(f'A Media: {media:.2f}') 

if media < 7 or falta > 3: 
    print('Infelizmente', nome, 'você foi reprovado')
elif media >= 7:
    print('Parabéns,', nome, 'você foi aprovado com sucesso !!!')


