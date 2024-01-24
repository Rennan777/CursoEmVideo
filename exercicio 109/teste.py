# exercicio 109
import moeda as m

valor = float(input('Digite um valor: R$'))

print(f'A metade de {m.moeda(valor)} é {m.metade(valor, True)}.')
print(f'O dobro de {m.moeda(valor)} é {m.dobro(valor, True)}')
print(f'Aumentando 10%, temos {m.aumentar(valor, 10, True)}')
print(f'Diminuindo 10%, temos {m.diminuir(valor, 10, True, "¢")}')  # teste outra moeda


print(m.aumentar(50, 10, True, 'US$'))
print(m.aumentar(50,15, True))


print(m.diminuir(50, 10, True, 'US$'))
print(m.diminuir(50,15, True))

#
# print(m.metade(50, True, 'U$'))
# print(m.metade(45, True))
#
