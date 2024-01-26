from lib import interface as i
from time import sleep

while True:
    resposta = i.menu(['Ver cadastros', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resposta == 1:
        i.cabecalho('opcao 1')
    elif resposta == 2:
        i.cabecalho('opcao 2')
    elif resposta == 3:
        i.cabecalho('Saindo do sistema..')
        break
    else:
        print('\033[31mDigite uma opção valida\033[m')
    sleep(0.5)

