'''
nome = str(input('Qual seu nome?'))
if nome == 'Rennan':
    print('Que nome legal voce tem!')
else:
    print('Seu nome é ok.')
print('Bom dia, {}!'.format(nome))
'''

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
'''
print('Sua média foi de {:.1f}'.format(m))
if m >= 6.0:
    print('Sua media foi boa!')
else:
    print('Sua media foi ruim..')
'''
print('Sua media foi boa' if m >= 6 else 'Sua media foi ruim.')
