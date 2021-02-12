from funsenha import *
from random import randint, choice, shuffle


def arquivoexiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except:
        return False
    else:
        return True


def criaarquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print(f'Houve um erro na criação do arquivo.')
    else:
        print(f'Arquivo {nome} criando com sucesso.')


def criarsenha(arq, nome, qtd):
    tipo = input('Qual tipo? Numeros ou Alphanumerica?[N/A] ').strip().title()[0]
    senha = []
    letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
              'T', 'U', 'V', 'W', 'Y', 'X', 'Z']
    letrasenumeros = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'l', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'y', 'x', 'z', 1, 2, 3, 4, 5, 6, 7, 8, 9]
    char = ['!', '@', '?', '&', "$"]
    if tipo == 'N':
        for n in range(0, qtd):
            senha.append(randint(1, 9))
    elif tipo == 'A':
        caracter = input(f'Precisa de caracteres especiais? [S/N] ').strip().upper()[0]
        if caracter == 'S':
            senha.append(choice(letras))
            senha.append(randint(1, 9))
            senha.append(choice(char))
            for n in range(0, qtd-3):
                senha.append(choice(letrasenumeros))
        elif caracter == 'N':
            senha.append(choice(letras))
            senha.append(randint(1, 9))
            for n in range(0, qtd-2):
                senha.append(choice(letrasenumeros))
    shuffle(senha)
    try:
        a = open(arq, 'at')
    except:
        print(f'Houve um erro na abertura do arquivo')
    else:
        try:
            a.write(f'{nome};{senha}\n')
        except:
            print('Houve um erro na hora de escrever os dados.')
        else:
            print(f'Novo registro de {nome} adicionado')
            a.close()
    return senha


def senhascriadas(nome):
    try:
        a = open(nome, 'rt')
    except:
        print(f'Houve uma falha na leitura do arquivo.')
    else:
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<20}{dado[1]:>3}')
    finally:
        a.close()


def deletarsenha(nome):
    with open('senhas.txt', 'r') as f:
        lines = f.readlines()
        with open('senhas.txt', 'w') as escre:
            for n in lines:
                dado = n.split(';')
                if dado[0] != nome:
                    escre.write(n)
