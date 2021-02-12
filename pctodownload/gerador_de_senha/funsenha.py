from time import sleep
from arquivo import *


def leiaint(txt):
    while True:
        try:
            num = int(input(f'{txt}'))
            break
        except:
            print(f'\033[31mErro. Digite um numero inteiro valido\033[m')
    return num


def cabecalho(msn):
    print('-'*40)
    print(msn.center(40))
    print('-'*40)


def menu(lista):
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print('-' * 40)
    while True:
        try:
            opcao = int( input( '\033[33mQual sua opção?\033[m '))
        except:
            print(f'\033[31mERRO. Digite um numero inteiro valido\033[m')
        else:
            return opcao

