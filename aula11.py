'''
print('\033[0;30;41mOla mundo!\033[m')

print('\033[7;33mOla Mundo!\033[m')

print('\033[7mOla Mundo!\033[m')


a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a, b))
'''


nome = 'Rennan'
#print('Ola {}{}{}, muito prazer te conhecer!'.format('\033[4;34m', nome, '\033[m'))
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7;30;41m'}
print('Olá {}{}{}, prazer em te conhecer!'.format(cores['pretoebranco'], nome, cores['limpa']))


