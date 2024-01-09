#estruturas compostas - dicionarios - identificados por {}
'''
dados = {}
dados = dict()
dados = {'nome':'Pedro', 'idade':25}

dados['sexo']='M' #adicionar itens

del dados['idade'] #remover itens

#################

filme = {'titulo': 'Star Wars',
         'ano': 1947,
         'diretor': 'George Lucas'
        }

print(filme.values()) #somente os valores
print(filme.keys()) #somente as chaves
print(filme.items()) #chaves e valores

for k, v in filme.items():
    print(f'O {k} é {v}')

########################

pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}

print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
#del pessoas['sexo']
pessoas['peso'] = 98.5 #adicionando
for k in pessoas.keys():
    print(k)

for k, v in pessoas.items():
    print(f'{k} = {v}')

###################

brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'Sao Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil[0]['uf'])
print(brasil[1]['sigla'])


#####################
estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla Estado: '))
    brasil.append((estado.copy()))
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()

'''



