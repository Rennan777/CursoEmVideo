# funções - parte 2

### ajudas python
# help()
# help(print)
# print(input.__doc__)  .__doc__ exibe documentação interna


#### inserindo docstrings nas funções

def contador(i, f, p):
    '''
        -> Faz uma contagem e  mostra na tela.
        :param i: inicio da contagem
        :param f: fim da contagem
        :param p: passo da contagem
        :return: sem retorno
    '''
    c = i
    while c <= f:
        print(f'{c}', end='..')
        c += p
    print('Fim')


# contador(2, 10, 2)
# help(contador)


####parametros opcionais

def somar(a, b, c=0):  # declara o valor padrao da variavel, o tornando opcional na chamada da função
    s = a + b + c
    print(f'A soma vale {s}')


# somar(3, 2, 5)
# somar(8, 4)


##### escopo de variaveis
'''
def teste():
    x = 8
    print(f'Na funcao teste, n = {n}')
    print(f'Na funcao teste, x = {x}')

n = 2
print(f'No programa principal n = {n}')
teste()
print(f'No programa principal x = {x}') # variavel x nao existe no escopo global, somente no local (funcao teste)
'''
'''
# variavel em 2 escopos
def funcao():
    n1 = 4
    print(f'N1 dentro vale {n1}') #mesma variavel em escopo local


n1 = 2
funcao()
print(f'N1 fora vale {n1}') #mesma variavel em escopo global
'''
'''
def funcao(b):
    global a        #ao chamar o comando global, a variavel dentro da funcao é tratada como global
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')


a = 5
funcao(a)
print(f'A fora vale {a}')
'''

### retorno de valores
'''
def somar(a, b=0, c=0):
    s = a + b + c
    return s


r1 = somar(3, 2, 5)
r2 = somar(8, 4)
r3 = somar(6)

print(f'Os resultados foram {r1}, {r2}, {r3}')

'''


### exemplos
'''
def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


n = int(input('Digite um numero: '))
print(f'O fatorial de {n} e igual a {fatorial(n)}')
'''
'''
def epar(n=0):
    if n % 2 == 0:
        return True     ### pode retornar booleano
    else:
        return False


num = int(input('Digite um numero: '))
if epar(num):
    print('É par.')
else:
    print('Não é par.')
'''


