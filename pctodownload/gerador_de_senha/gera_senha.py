from funsenha import *
from arquivo import *


arq = 'senhas.txt'

if not arquivoexiste(arq):
    criaarquivo(arq)

while True:
    cabecalho('GERADOR AUTOMATICO DE SENHA!')
    opcao = menu(['Criar senha', 'Senhas criadas', 'Deletar senha', 'Sair'])
    if opcao == 1:
        cabecalho('CRIAR NOVA SENHA!')
        nome = input('Nome: ').strip().title()
        qtd = int(input(f'Quantos caracteres tem que ter a senha? '))
        senha = criarsenha(arq, nome, qtd)
        print(senha)

    elif opcao == 2:
        print('-' * 40)
        print(f'SENHAS CRIADAS'.center(40))
        print('-' * 40)
        senhascriadas(arq)

    elif opcao == 3:
        nome = input('Qual senha quer deletar? ').strip().title()
        deletarsenha(nome)
        print(f'Senha {nome} deletada com sucesso')

    elif opcao == 4:
        print(f'\033[35mObrigado por usar o sistema. Até logo\033[m.')
        break

    else:
        print(f'\033[31mOPCAO INVALIDA.\033[m')

