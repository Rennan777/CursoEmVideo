#variaveis compostas - listas
#mutaveis, reconhecidas por [colchetes]
'''
.append()
.insert(0,'xxx')
del xxx[3]
.pop(3)
.remove('variavel')

xxx.sort()
xxx.sort(reverse=True)
len(xxxx)
'''
'''
num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)
num.pop(2)
if 4 in num:
    num.remove(4)
print(num)
'''
'''
valores = []
valores.append(5)
valores.append(9)
valores.append(4)
for c, v in enumerate(valores):
    print(f'posicao {c}: valor: {v}')
print('fim')
'''
a = [2, 3, 4, 7]
b = a #listas igualadas, ao alterar um valor, altera nas 2
c = a[:] # copia da lista, ao alterar a copia, original continua sem mudança
c[2] = 8
print(a,b,c)


