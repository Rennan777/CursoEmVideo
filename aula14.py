#estrutura de repetição while
'''
for c in range(1,11):
    print(c)
print('Fim')
'''
'''
c = 1
while c <= 10:
    print(c)
    c += 1
print('Fim')
'''
'''
n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('Fim')
'''
'''
r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Continuar? [S/N] ')).upper()
print('Fim')
'''
#quantidade de numeros pares e impares, enquanto não digitar 0

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 ==0:
            par += 1
        else:
            impar += 1
print('Voce digitou {} numeros pares e {} numeros impares.'.format(par, impar))
