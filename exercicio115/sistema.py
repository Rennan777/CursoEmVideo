from exercicio115.lib.arquivo import *
from exercicio115.lib.interface import *
from time import sleep

arquivo = 'cursoemvideo.txt'

if not arquivoexiste(arquivo):
    criararquivo(arquivo)


while True:
    resposta = menu(['Ver cadastros', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resposta == 1:
        # listar conteudo de um arquivo
        lerarquivo(arquivo)
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arquivo, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do sistema..')
        break
    else:
        print('\033[31mDigite uma opção valida\033[m')
    sleep(0.5)

