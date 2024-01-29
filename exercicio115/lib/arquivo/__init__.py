from exercicio115.lib.interface import *

def arquivoexiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criararquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Erro na criação do arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso.')


def lerarquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler arquivo')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arquivo, nome='Nao informado', idade=0):
    try:
        a = open(arquivo, 'at')
    except:
        print('Erro na abertura do arquivo.')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Erro na escrita de dados.')
        else:
            print(f'Novo registro de {nome} adicionado')
            a.close()

