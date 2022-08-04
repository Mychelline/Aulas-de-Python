
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

opcao = 1
     
while opcao != 0:
    print('\n1 = Somar ', '\n2 = Subtrair', '\n3 = Multiplicação','\n4 = Divisão')
    opcao = int(input('Escolha uma opção: '))
    
    if opcao == 1:
        
        soma()

    elif opcao == 2:
       
        subtracao()

    elif opcao == 3:
       
        multiplicacao()

    elif opcao == 4:
      
        divisao()
    else:
        print ("Não existe essa operação")
        break
