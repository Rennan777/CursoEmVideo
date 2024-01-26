def leiaint(valor):
    while True:
        try:
            x = int(input(valor))
        except (ValueError, TypeError):
            print('\033[31mDigite um numero inteiro valido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mUsuario nao digitou o valor\033[m')
            break
        else:
            return x


def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    for i, v in enumerate(lista):
        print(f'\033[33m{i + 1}\033[m - \033[34m{v}\033[m')
    print(linha())
    opc = leiaint('\033[32mSua opção: \033[m')
    return opc

