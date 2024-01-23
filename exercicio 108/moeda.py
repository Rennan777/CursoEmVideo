def aumentar(valor=0, percent=0):
    percent = (percent / 100) * valor
    return valor + percent


def diminuir(valor=0, percent=0):
    percent = (percent / 100) * valor
    return valor - percent


def dobro(valor=0):
    return valor * 2


def metade(valor=0):
    return valor / 2


# exercicio 108

def moeda(valor=0, moeda='R$'):
    formata = str(f'{moeda}{valor:.2f}').replace('.', ',')
    return formata

