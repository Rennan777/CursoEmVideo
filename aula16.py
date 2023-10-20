#variaveis compostas - tuplas
#tuplas sao imutaveis, reconhecidas por () ou sem parenteses.
'''
lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
print(lanche)
print(type(lanche)) #tipo do objeto
print(len(lanche)) #quantidade de itens
print(lanche[1:3]) #fatiamento por indice
print(lanche[:2]) #fatiamento por indice

print('#' * 20)
#incluido na repeticao
for c in lanche:
    print(f'eu comi {c}')

print('#' * 20)
#com medidas
for c in range(0, len(lanche)):
    print(f'eu comi {lanche[c]}')

print('#' * 20)
#enumerate
for pos, c in enumerate(lanche):
    print(f'{c} esta na posicao {pos}')


print('#' * 20)

#ordenado - transformou a tupla em lista, de () para []
print(sorted(lanche))

'''
'''
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a #contatena tupla
print(a)
print(b)
print(c)
print(len(c)) #quantitade de itens
print(c.count(5)) #contagem de determinado item
print(c.index(8)) #print indice do item solicitado
'''

pessoa = ('rennan', 34, 'M', 86.5) #tuplas aceitam tipos distintos
del(pessoa) #deleta tupla
print(pessoa)