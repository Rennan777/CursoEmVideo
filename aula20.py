# funçoes - parte 1
"""
def linha():
    print('--' * 20)


linha()
print(' ' * 10, 'CURSO EM VIDEO', ' ' * 10)
linha()


def titulo(txt):
    print('--' * 20)
    print(txt)
    print('--' * 20)


titulo('PYTHON TESTE')
"""
##################################
"""
# funcao
def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B = {s}')


# programa

soma(4, 5)
soma(8, 9)
soma(a=2, b=1)
soma(b=2, a=6)
"""
##################################
# recebe varios valores, e retorna em uma tupla
"""
def contador(* num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} numeros.')
    # for valor in num:
    #     print(f'{valor} ', end='')
    # print('Fim')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
"""

##################################
"""
# pode-se passar uma lista e retornar em lista

def dobra(lst):
    posicao = 0
    while posicao < len(lst):
        lst[posicao] *= 2
        posicao += 1


valores = [7, 2, 5, 0, 4]
print(valores)
dobra(valores)
print(valores)

"""
###################################
# desempacotar

def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


soma(5, 2)
soma(2, 9, 4)