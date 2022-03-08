#Definição das funções para a calculadora
#Cada operação vai utilizar receber dois números
def soma(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    return x / y

def resto(x, y):
    return x % y

def potencia(x, y):
    return x ** y

#Cabeçalho do Menu de Operações
menu = ("Menu de operações:"
            "\n1 - Soma"
            "\n2 - Subtração"
            "\n3 - Multiplicação"
            "\n4 - Divisão"
            "\n5 - Resto"
            "\n6 - Potência")

continuar = 's'

#As condicionais para cada escolha do usuario
#TENTAR COMPILAR O CODIGO PARA NÃO REPETIR OS INPUTS
while continuar == 's':
    # Print do Menu de operações e o input para o usuario escolher a operação
    print(menu)
    escolha = (input(("Escolha o tipo de operação: ")))
    if escolha == '1':
        x = int(input("Entre com o primeiro número da soma: "))
        y = int(input("Entre com o segundo número da soma: "))
        print('\nA soma dos valores é: ', x, '+', y, '=', soma(x, y))
    elif escolha == '2':
        x = int(input("Entre com o primeiro número da subtração: "))
        y = int(input("Entre com o segundo número da subtração: "))
        print('\nA subtração dos valores é: ', x, '-', y, '=', subtracao(x, y))
    elif escolha == '3':
        x = int(input("Entre com o primeiro número da multiplicação: "))
        y = int(input("Entre com o segundo número da multiplicação: "))
        print('\nA nultiplicação dos valores é: ', x, 'x', y, '=', multiplicacao(x, y))
    elif escolha == '4':
        x = int(input("Entre com o primeiro número da divisão: "))
        y = int(input("Entre com o segundo número da divisão: "))
        print('\nA divisão dos valores é: ', x, '/', y, '=', divisao(x, y))
    elif escolha == '5':
        x = int(input("Entre com o primeiro número do resto: "))
        y = int(input("Entre com o segundo número do resto: "))
        print('\nO resto dos valores é: ', x, '%', y, '=',resto(x, y))
    elif escolha == '6':
        x = int(input("Entre com o primeiro número da potência: "))
        y = int(input("Entre com o segundo número da potência: "))
        print('\nA potência dos valores é: ', x, '^', y, '=', potencia(x, y))
    else:
        print('Opção inválida.'
            '\nEscolha uma opção do menu.')

    continuar = (input('Deseja fazer outra operação?'
                          '\ns ou n'
                          '\nEscolha: '))

