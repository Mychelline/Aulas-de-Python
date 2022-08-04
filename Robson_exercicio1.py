nome = str(input('Qual o nome do aluno?'))
nota1  = float(input('Qual a primeira nota do aluno ?'))
nota2 = float(input('Qual a segunda nota do aluno ?'))
faltas = int (input(' Qual o numero de Faltas do aluno ?'))

media = (nota1 + nota2) / 2

print(' A média desse Aluno foi :' , media)

if media < 7 or faltas > 3:
    print('O Aluno' , nome , 'Foi Reprovado')

elif media >= 7:
    print (' O Aluno ' , nome , ' Foi Aprovado')