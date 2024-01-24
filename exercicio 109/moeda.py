# exercicio 109
def moeda(valor=0, moeda='R$'):
    """
    -> Formata um valor numerico para valor monetario - padão: R$
    :param valor: recebe o valor numerico
    :param moeda: recebe a string de moeda
    :return: valor formatado
    """
    formata = str(f'{moeda}{valor:.2f}').replace('.', ',')
    return formata


def aumentar(valor=0, percent=0, formata=False, moed='R$'):
    """
    -> Aumenta o valor recebido, com o percentual recebido. Pode-se formatar como valor monetario
    :param valor: recebe o valor numerico
    :param percent: recebe o percentual a cer aumentado
    :param formata: formata monetario (True ou False)
    :param moed: recebe a moeda a ser retornada
    :return: o valor aumentado (e formatado)
    """
    percent = (percent / 100) * valor
    result = valor + percent
    if formata:
        result = moeda(result, moed)
    return result


def diminuir(valor=0, percent=0, formata=False, moed='R$'):
    """
    -> Subtrai o valor recebido, com o percentual recebido. Pode-se formatar como valor monetario
    :param valor: recebe o valor numerico
    :param percent: recebe o percentual a cer aumentado
    :param formata: formata monetario (True ou False)
    :param moed: recebe a moeda a ser retornada
    :return: o valor aumentado (e formatado)
    """
    percent = (percent / 100) * valor
    result = valor - percent
    if formata:
        result = moeda(result, moed)
    return result


def dobro(valor=0, formata=False, moed='R$'):
    """
    -> Dobra o valor informado e formata em valor monetario
    :param valor: recebe um valor numerico
    :param formata: recebe a informacao se ira formatar o valor (True ou False)
    :param moed: recebe um formato monetario diferente (padrao = R$)
    :return: o valor dobrado (e formatado)
    """
    result = valor * 2
    if formata:
        result = moeda(result, moed)
    return result


def metade(valor=0, formata=False, moed='R$'):
    """
    -> subtrai a metade do valor informado e formata em valor monetario
    :param valor: recebe um valor numerico
    :param formata: recebe a informacao se ira formatar o valor (True ou False)
    :param moed: recebe um formato monetario diferente (padrao = R$)
    :return: a metade do valor informado (formatado)
    """
    result = valor / 2
    if formata:
        result = moeda(result, moed)
    return result


