# exercicio 108
import moeda as m

valor = float(input('Digite um valor: R$'))

print(f'A metade de {m.moeda(valor)} é {m.moeda(m.metade(valor))}.')
print(f'O dobro de {m.moeda(valor)} é {m.moeda(m.dobro(valor))}')
print(f'Aumentando 10%, temos {m.moeda(m.aumentar(valor, 10))}')
print(f'Diminuindo 10%, temos {m.moeda(m.diminuir(valor, 10), "¢")}') # teste outra moeda

