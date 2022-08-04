def soma():
    num1 = float(input('1) Digite o número: '))
    num2 = float(input('2) Digite o número: '))
    print('Resultado da soma: ', num1 + num2)

def subtracao():
    num1 = float(input('1) Digite o número: '))
    num2 = float(input('2) Digite o número: '))
    print('Resultado da subtração: ', num1 - num2)

def multiplicacao():
    num1 = float(input('1) Digite o número: '))
    num2 = float(input('2) Digite o número: '))
    print('Resultado da multiplicação: ', num1 * num2)

def divisao():
    num1 = float(input('1) Digite um número: '))
    num2 = float(input('2) Digite um número: '))
    print('Resultado da divisão: ', num1 / num2)

op = 1
     
while op != 0:
    print('\n1 = Somar ', '\n2 = Subtrair', '\n3 = Multiplicação','\n4 = Divisão',"\n0= Sair" )
    op = int(input('Escolha uma opção: '))
    
    
    if op == 1:
        soma()

    elif op == 2:
     
        subtracao()

    elif op == 3:
    
        multiplicacao()

    elif op == 4:
       
        divisao()

    elif op == 0:
         print('Programa finalizado com sucesso.')
         break
    else:
        print ("Essa opção não existe, escolha outra ")
