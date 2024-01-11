# Passo a Passo Calculadora
import os

def clear_terminal():
        os.system('clear')
        os.system('cls')

def soma(pvalora, pvalorb):
    r = pvalora + pvalorb
    return(r)

def subtracao(pvalora, pvalorb):
    if pvalora > pvalorb:
        r = pvalora - pvalorb
        return(r)
    else:
        r = pvalorb - pvalora
        return(r)
    
def multipli(pvalora, pvalorb):
    r = pvalora * pvalorb
    return(r)

def exponenci(pvalora, pvalorb):
    r = pvalora ** pvalorb
    return(r)

def divisao(pvalora, pvalorb):
    r = pvalora / pvalorb
    return(r)

# 1 - Apresentação das opções
def calculadora():
    op = int(input('0 - Soma\n1 - Subtração\n2 - Divisão\n3 - Multiplicação\n4 - Potencialização\n\nQual operação você deseja fazer?'))

    while op not in range(-1, 5):
        print('Erro! Você não digitou um valor válido!')
        p = int(input('0 - Soma\n1 - Subtração\n2 - Divisão\n3 - Multiplicação\n4 - Potencialização\n\nQual operação você deseja fazer?'))

# 2 - Qual opção você escolheu

    if op == 0:
        opera = 'soma'
    elif op == 1:
        opera = 'subtração'
    elif op == 2:
        opera = 'divisão'
    elif op == 3:
        opera = 'multiplicação'
    elif op == 4:
        opera = 'potencialização'
        
    print(f'Você escolheu {opera}')

# 3 - Primeiro valor

    valora = float(input('Digite o primeiro valor: '))

    while type(valora) is not float:
        print('Erro! Você não digitou um valor válido!')
        valora = float(input('Digite o primeiro valor: '))

# 4 - Segundo valor

    valorb = float(input('Digite o segundo valor: '))

    while type(valorb) is not float:
        print('Erro! Você não digitou um valor válido!')
        valora = float(input('Digite o primeiro valor: '))

# 5 - Cálculo

    if op == 0:
        resultado = soma(valora, valorb)
    elif op == 1: 
        resultado = subtracao(valora, valorb)
    elif op == 2: 
        resultado = divisao(valora, valorb)
    elif op == 3: 
        resultado = multipli(valora, valorb)
    elif op == 4: 
        resultado = exponenci(valora, valorb)

# 6 - Resultado

    print(f'O resultado da operação foi {resultado}')

# 7 - Deseja continuar?

    cont = input('Deseja continuar?\n\nS - Sim\nN - Não')

    while cont.lower() not in ['sim', 'não']:
        print('Erro! Digite um valor válido!')
        cont = input('Deseja continuar?\n\nS - Sim\nN - Não')

    if cont.lower() == 'sim':
        clear_terminal()
        calculadora()
    elif cont.lower() == 'não':
        print('Até mais!')
        
        
# 8 - Execultando
calculadora()