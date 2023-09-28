# exercicio 05
# num = int(input('Digite um numero inteiro: '))
# print('O numero anterior é {} e o proximo numero é {}'.format(num-1, num+1))

# exercicio 06
# num = int(input('Digite um numero: '))
# d = num * 2
# t = num * 3
# r = num ** 0.5
# rint('O dobro é {}, o triplo é {} e a raiz quadrada é {}.'.format(d, t, r))

# exercicio 07
# n1 = int(input('Digite a primeira nota: '))
# n2 = int(input('Digite a segunda nota: '))
# nota = (n1 + n2) / 2
# print('A media é {}.'.format(nota))

# exercicio 08
# m = float(input('Digite o valor em metros: '))
# c = m * 100
# mm = m * 1000
# print('O valor em centimetros é {:.0f}cm e em milimetros é {:.0f}mm.'.format(c, mm))

# exercicio 09
# n = int(input('Digite um numero inteiro: '))
# t0 = n * 0
# t1 = n * 1
# t2 = n * 2
# t3 = n * 3
# t4 = n * 4
# t5 = n * 5
# t6 = n * 6
# t7 = n * 7
# t8 = n * 8
# t9 = n * 9
# print('-' * 12)
# print('A tabuada do numero {} é: \n {}x0 = {} \n {}x1 = {} \n {}x2 = {} \n {}x3 = {} \n {}x4 = {} \n {}x5 = {} \n {'
#      '}x6 = {} \n {}x7 = {} \n {}x8 = {} \n {}x9 = {}'.format(n, n, t0, n, t1, n, t2, n, t3, n, t4, n, t5, n, t6, n,
#                                                           t7, n, t8, n, t9))
# print('-' * 12)


# exercicio 10
# real = float(input('Quantos reais voce tem na carteira? R$ '))
# dol = real / 3.27
# print('Voce pode comprar ate {:.3f} dolar(es)'.format(dol))

# exercicio 11
# lar = float(input('Qual a largura da parede? '))
# alt = float(input('Qual a altura da parede? '))
# area = lar * alt
# tint = area / 2
# print('A area a ser pintada é de {:.3f} metros quadrados, serão necessários {} litros de tinta'.format(area, tint))

# exercicio 12
# preco = float(input('Qual o preço do produto? '))
# desc = (preco /100) * 5  #pre * 0.05
# total = preco - desc
# print('O total de desconto é de {:.2f}, o valor do produto com desconto é de {:.2f}'.format(desc, total))

# exercicio 13
# sal = float(input('Qual o salario atual? '))
# add = (sal / 100) * 15
# nsal = sal + add
# print('O aumento será de {:.2f}, o novo salario sera de {:.2f}'.format(add, nsal))

# exercicio 14
# c = float(input('Qual a temperatura em ºC? '))
# f = c * 1.8 + 32       ##((9*c)/5)+32
# print('A temperatura em ºF é de {} '.format(f))

# exercicio 15
# kms = float(input('Quantos kms percorridos? '))
# dias = float(input('Quantos dias ficou alugado? '))
# vdia = dias * 60
# vkm = kms * 0.15
# print('O valor a ser pago referente aos dias é de R${:.2f} \nO valor a ser pago, referente aos kms rodados é de R$ {:.2f} \nO '
#      'valor total do aluguel é de R${:.2f}'.format(vdia, vkm, vdia+vkm))

# exercicio 16
'''from math import trunc
num = float(input('Digite um numero real! '))
print(trunc(num))

'''
#from time import sleep

# import math

'''num = float(input('Digite um valor: '))
print('O valor digitado foi {} e sua porção inteira é {}'.format(num, int(num)))'''

# exercicio 17
'''
from math import hypot
cat1 = float(input('Digite o valor do cateto oposto: '))
cat2 = float(input('Digite o valor do cateto adjacente: '))
hip = hypot( cat1, cat2)
#hip = ((cat1**2) + (cat2**2)) ** (1/2)
print('o valor da hipotenusa é de {:.2f}'.format(hip))
'''

# exercicio 18
'''
from math import radians, sin, cos, tan
num = float(input('Digite o angulo que voce deseja: '))
sen = sin(radians(num))
cos = acos(radians(num))
tan = tan(radians(num))
print('Seno = {:.2f} \nCosset = {:.2f} \nTangent = {:.2f}'.format(sen, cos, tan))
'''

# exercicio 19
'''
from random import choice
a1 = input('Digite o nome do primeiro aluno: ')
a2 = input('Digite o nome do segundo aluno: ')
a3 = input('Digite o nome do terceiro aluno: ')
a4 = input('Digite o nome do quarto aluno: ')
lista = [a1, a2, a3, a4]
alu = choice(lista)
print('O aluno sorteado foi {}!'.format(alu))
'''

#exercicio 20
'''
from random import shuffle
a1 = input('primeiro aluno: ')
a2 = input('segundo aluno: ')
a3 = input('terceiro aluno: ')
a4 = input('quarto aluno: ')
lista = [a1, a2, a3, a4]
shuffle(lista)
print(lista)
'''

#exercicio 21
'''
import pygame
pygame.init()
pygame.mixer.music.load('back.mp3')
pygame.mixer.music.play()
pygame.event.wait()
'''

#exercicio 22
'''
nome = str(input('Digite seu nome completo: ')).strip #strip remove espaços antes e depois
nomeint = ''.join(nome)
nomelist = nome.split() #dividindo nome em lista
tamnome = len(''.join(nome)) #removendo espaços e contando caracteres   #pode ser usado = len(nome) - nome.count(' ')
tampnome = len(nomelist[0]) #contando caracteres do objeto 0 da lista
print(nome.upper())
print(nome.lower())
print('Seu nome completo tem {} caracteres.'.format(tamnome))
print('Seu primeiro nome tem {} caracteres.'.format(tampnome))
'''

#exercicio 23
'''
num = int(input('informe um numero: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o numero {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
'''

#exercicio 24
'''
cid = str(input('Em que cidade voce nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')
'''

#exercicio 25
'''
nome = str(input('Digite seu nome completo: ')).strip().upper()
print('Seu nome tem Silva? {}'.format('SILVA' in nome))
'''
'''
nomelist = nome.split()
if 'SILVA' in nomelist:
    print('Seu nome tem Silva.')
else:
    print('Seu nome nao tem Silva')
'''

#exercicio 26
'''
frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira aparição da letra A é na posição {}'.format(frase.find('A')+1))
print('A ultima aparição da letra A é na posição {}'.format(frase.rfind('A')+1))
'''

#exercicio 27
'''
nome = str(input('Digite seu nome completo: ')).strip()
listnome = nome.split()
print('Seu primeiro nome é {}'.format(listnome[0]))
print('Seu ultimo nome é {}'.format(listnome[-1]))
## print('Seu ultimo nome é {}'.format(listnome[len(listnome)-1]))
'''

#exercicio 28
'''
from random import randint
from time import sleep
numpc = randint(0, 5)
print('=*=' * 20)
print('Tente adivinhar o numero que pensei (de 0 a 5).')
print('=*=' * 20)
numus = int(input('Em que numero pensei? '))
print('Processando...')
sleep(1)
if numpc == numus:
    print('O numero que pensei foi {}! Voce adivinhou!'.format(numpc))
else:
    print('O numero que pensei foi {}. Voce errou.'.format(numpc))
'''

#exercicio 29
'''
vel = float(input('Qual a velocidade do veiculo? '))
multa = (vel-80)*7
if vel < 81:
    print('Voce esta dentro do limite de velocidade. Continue assim. Boa viagem')
else:
    print('Voce esta acima do limite de 80 km/h! Voce será multado em R$ {:.2f}'.format(multa))
'''

#exercicio 30
'''
num = int(input('Me diga um numero qualquer: '))
result = num % 2
if result == 0:
    print('O numero {} é PAR.'.format(num))
else:
    print('O numero {} é IMPAR.'.format(num))
'''

#exercicio 31
'''
dist = float(input('Qual a distancia da sua viagem? '))

if dist > 200:
    preco = dist * 0.45
else:
    preco = dist * 0.5

#preco = dist * 0.45 if dist <= 200 else dist * 0.5
print(('O preço da passagem é de R$ {:.2f}'.format(preco)))
'''
#exercicio 32
'''
from datetime import date
ano = int(input('Que ano quer analisar? Digite 0 para ano atual:'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO.'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO.'.format(ano))
'''

#exercicio 33
'''
a = int(input('Digite o 1o numero: '))
b = int(input('Digite o 2o numero: '))
c = int(input('Digite o 3o numero: '))
#verificando menor num
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
#verificando maior num
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))
'''

#exercicio 34
'''
sal = float(input('Qual o salário do funcionário? '))
if sal <= 1250:
    nsal = sal + ((sal/100) * 15)
else:
    nsal = sal + ((sal/100) * 10)
print('O funcionário recebia R$ {:.2f}. O novo salário será de R$ {:.2f}'.format(sal, nsal))
'''

#exercicio 35
'''
print('**' * 20)
print('Analisador de triangulo')
print('**' * 20)
n1 = float(input('Digite o primeiro segmento: '))
n2 = float(input('Digite o segundo segmento: '))
n3 = float(input('Digite o terceiro segmento: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Os valores PODEM FORMAR triangulo.')
else:
    print('O valores NÃO PODEM FORMAR triangulo.')
'''

#exercicio 36
'''
print('##' * 20)
print('####### SIMULADOR DE EMPRESTIMO #######')
print('##' * 20)
vimov = float(input('Informe o valor do imóvel: '))
sal = float(input('Informe seu salário mensal: '))
tempo = int(input('Informe em quantos anos pretende pagar: '))
print('#### ANALISANDO OS DADOS FINANCEIROS ####')
prest = (vimov / (tempo * 12))
if (sal / 100 * 30) <= prest:
    print('Infelizmente, seu salário não se enquadra ao valor da prestação.\nSeu emprestimo não foi aprovado.')
else:
    print('Parabéns! Seu emprestimo no valor de R${:.2f} está pré-aprovado!\nO valor da prestação será de R${'
          ':.2f}.\nO prazo de pagamento será de {} anos.'.format(vimov, prest, tempo))
print('######### FIM DA SIMULAÇÃO #########')
'''

#exercicio 37
'''
print('####' * 10)
print('##### CONVERSOR DE BASES #####')
print('####' * 10)
num = int(input('Digite um numero inteiro: '))
base = int(input('Selecione a base de conversão: \n1 = Binário\n2 = Octal\n3 = Hexadecimal\nSeleção: '))
if base == 1:
    print('Binário selecionado. O valor é: {}'.format(bin(num)))
elif base == 2:
    print('Octal selecionado. O valor é: {}'.format(oct(num)))
elif base == 3:
    print('Hexadecimal selecionado. O valor é: {}'.format(hex(num)))
else:
    print('Valor inválido!')
print('##### FIM DA CONVERSÃO #####')
'''

#exercicio 38
'''
n1 = int(input('Digite um numero inteiro: '))
n2 = int(input('Digite mais um numero: '))
if n1 > n2:
    print('O numero {} é maior que {}'.format(n1, n2))
elif n2 > n1:
    print('O numero {} é maior que {}'.format(n2, n1))
elif n1 == n2:
    print('Voce digitou {} nas duas vezes'.format(n1))
'''

#exercicio 39
'''
from datetime import date
anoatual = date.today().year
nasc = int(input('Digite o ano de nascimento: '))
i = anoatual - nasc
if i == 18:
    print('Voce tem {} anos. Deve se alistar esse ano.'.format(i))
elif i > 18:
    t = i - 18
    print('Voce tem {} anos. Deveria ter se alistado a {} anos!'.format(i, t))
elif i < 18:
    t = 18 - i
    print('Voce tem {} anos. Ainda não esta na hora de se alistar. Ainda faltam {} anos.'.format(i, t))
'''

#exercicio 40
'''
n1 = float(input('D igite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('Sua média é de {:.2f}'.format(m))
if m < 5:
    print('Status: REPROVADO')
elif m >= 5 and m < 7:
    print('Status: RECUPERAÇÃO')
elif m >= 7:
    print('Status: APROVADO')
'''

#exercicio 41
'''
from datetime import date
atual = date.today().year
nasc = int(input('Digite o ano de nascimento: '))
i = atual - nasc
print('Suda idade é de {} anos.'.format(i))
if i <= 9:
    print('Sua categoria é MIRIM')
elif i <= 14:
    print('Sua categoria é INFANTIL')
elif i <= 19:
    print('Sua categoria é JUNIOR')
elif i <= 25:
    print('Sua categoria é SENIOR')
elif i > 25:
    print('Sua categoria é MASTER')
'''

# exercicio 42
'''
l1 = float(input('Digite o valor do primeiro lado: '))
l2 = float(input('Digite o valor do segundo lado: '))
l3 = float(input('Digite o valor do terceiro lado: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Os valores podem formar um triangulo ', end='')
    if l1 == l2 and l1 == l3: ## l1 == l2 == l3
        print('O triangulo é EQUILATERO')
    elif (l1 == l2 and l1 != l3) or (l2 == l3 and l2 != l1) or (l1 == l3 and l1 != l2):
        print('O triangulo é ISOSCELES')
    elif l1 != l2 and l1 != l3 and l2 != l3:
        print('O triangulo é ESCALENO')
else:
    print('Os valores não podem formar triangulo.')
'''

#exercicio 43
'''
p = float(input('Digite seu peso em quilos: '))
a = float(input('Digite sua altura em metros: '))
imc = p / (a ** 2)
print('Seu IMC é de {:.2f}'.format(imc))
if imc < 18.5:
    print('Voce está abaixo do peso recomendado')
elif imc < 25:
    print('Voce está no peso ideal')
elif imc < 30:
    print('Voce está sobrepeso')
elif imc < 40:
    print('Voce está obeso')
else:
    print('Voce esta com obesidade morbida')
'''

#exercicio 44
'''
print('{:=^40}'.format(' SIMULADOR DE PARCELAMENTO '))
val = float(input('Digite o valor da compra: '))
mei = int(input('Selecione o meio de pagamento: \n'
                '1 - Dinheiro/cheque.\n'
                '2 - Cartão.\n'
                'Meio: '))
if mei == 1:
    desc = val - (val * 0.1)
    print('O valor a ser pago é de R${:.2f}'.format(desc))
elif mei == 2:
    qtdparc = int(input('Digite em quantas vezes deseja parcelar: '))
    valparc = val / qtdparc
    if qtdparc == 1:
        desc = val - (val * 0.05)
        print('O valor a ser pago é de R${:.2f} '.format(desc))
    elif qtdparc == 2:
        print('O valor a ser pago é de {:.2f}, em {} parcelas de R${:.2f}'.format(val, qtdparc, valparc))
    elif qtdparc > 2:
        acres = val + (val * 0.2)
        print('O valor a ser pago é de {:.2f}, em {} parcelas de R${:.2f}'.format(acres, qtdparc, valparc))
else:
    print('Meio invalido.')
'''

#exercicio 45
'''
from random import choice
joga = str(input('Escolha pedra, papel ou tesoura?\n>>>> ')).upper()
print('Voce escolheu {}'.format(joga))
opc = ['PEDRA', 'PAPEL', 'TESOURA']
comp = choice(opc)
print('Computador escolheu {}'.format(comp))
if joga == comp:
    print('Empate!!')
elif joga == 'PEDRA':
    if comp == 'PAPEL':
        print('Voce perdeu.')
    else:
        print('Voce ganhou!!')
elif joga == 'PAPEL':
    if comp == 'TESOURA':
        print('Voce perdeu.')
    else:
        print('Voce ganhou!!')
elif joga == 'TESOURA':
    if comp == 'PEDRA':
        print('Voce Perdeu.')
    else:
        print('Voce ganhou!!')
else:
    print('VOCE PERDEU!! E o computador jogou {} no seu olho'.format(comp))
'''

#exercicio 46
'''
from time import sleep
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('kabum!!!')
'''

#exercicio 47
'''
for c in range(1, 51, 1):
    if c % 2 == 0:
        print(c, end=' ')
print('fim')
'''
'''
for c in range(2, 51, 2):
    print(c, end=' ')
print('fim')
'''

#exercicio 48
'''
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        soma += c
print('A soma de todos os {} valores é de {}.'.format(cont, soma))
'''

#exercicio 49
'''
n = int(input('Digite um numero inteiro: '))
print('=*' * 8)
for c in range(1, 11):
    print('{} x {} = {}'.format(c, n, c * n))
print('=*' * 8)
'''

#exercicio 50
'''
s = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digite o {}o valor: '.format(c)))
    if n % 2 == 0:
            s += n
            cont += 1 
print('voce informou {} valores pares e a soma deles é de {}'.format(cont, s))
'''

#exercicio 51
'''
p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
dec = p +(10 - 1 ) * r      #calculo decimo termo da razão
for c in range(p, dec + r, r):
    print(p, end='- ')
    p += r
print('Fim')
'''

#exercicio 52
'''
num = int(input('Digite um numero: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO numero {} foi divisível {} vezes.'.format(num, tot))
if tot == 2:
    print('E por isso é PRIMO')
else:
    print('E por isso, NÃO é PRIMO')
'''

#exercicio 53
#com 'for'
'''
frase = str(input('Digite uma frase: ')).strip().upper() ##remove espaços e deixa maiusculo
palavras = frase.split()                                 ##separa palavras
junto = ''.join(palavras)                                ##junta palavras (ao separar e juntar, remove espaços entre palavras
inverso = ''
for letra in range(len(junto) -1, -1, -1):               ##len(junto) -1 = pega a ultima letra, -1 = ate a primeira letra (0 menos 1), -1 = voltar caractere
    inverso += junto[letra]
if inverso == junto:
    print('É palíndromo!')
else:
    print('Não é palíndromo.')
print('Voce digitou a frase: {}'.format(inverso))
'''
        #sem 'for'
'''
frase = str(input('Digite uma frase: ')).strip().upper() ##remove espaços e deixa maiusculo
palavras = frase.split()                                 ##separa palavras
junto = ''.join(palavras)                                ##junta palavras (ao separar e juntar, remove espaços entre palavras
inverso = junto[::-1]
if inverso == junto:
    print('É palíndromo!')
else:
    print('Não é palíndromo.')
print('Voce digitou a frase: {}'.format(inverso))
'''

#exercicio 54
'''
from datetime import date
anocorrente = date.today().year
maior = 0
menor = 0
for pessoa in range(1,8):
    ano = int(input('Em que ano a {}a pessoa nasceu? '.format(pessoa)))
    if anocorrente - ano < 18:
        menor += 1
    else:
        maior += 1
print('{} pessoas são maiores de idade e {} são menores.'.format(maior, menor))
'''

#exercicio 55
'''
maior = 0
menor = 0
for pessoa in range(1,6):
    peso = float(input('Digite o peso da {}a pessoa: '.format(pessoa)))
    if pessoa == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print('maior {}, menor {}'.format(maior, menor))
'''

#exercicio 56
'''
idades = 0
idadehomem = 0
velho = ''
menor20 = 0
for pessoa in range(1,5):
    nome = str(input('Digite o nome da {}a pessoa: '.format(pessoa)))
    idade = int(input('Digite a idade da {}a pessoa: '.format(pessoa)))
    sexo = str(input('Digite o sexo da {}a pessoa (M/F): '.format(pessoa))).strip()
    idades += idade
    if pessoa == 1 and sexo in 'Mm':
        idadehomem = idade
        velho = nome
    elif sexo in 'Mm' and idade > idadehomem:
        idadehomem = idade
        velho = nome
    elif sexo in 'Ff' and idade < 20:
        menor20 += 1
mediaidades = idades / 4
print('A media das idades é de {}.'.format(mediaidades))
print('O homem mais velho tem {} anos e se chama {}.'.format(idadehomem, velho))
print('Tem {} mulheres menores de 20 anos'.format(menor20))
'''

#exercicio 57
'''
sex = str(input('Digite seu sexo [M/F]: ')).strip().upper()
opc = ['M', 'F']
while sex not in opc:
    sex = str(input('Opção invalida. Digite seu sexo [M/F]: ')).upper()
if sex == 'M':
    print('Voce selecionou MASCULINO')
else:
    print('Voce selecionou FEMININO')
'''
'''
sex = str(input('Digite seu sexo [M/F]: ')).strip().upper()
while sex not in 'mMfF':
    sex = str(input('Opção invalida. Digite seu sexo [M/F]: ')).strip().upper()
if sex == 'M':
    print('Voce selecionou MASCULINO')
else:
    print('Voce selecionou FEMININO')
'''

#exercicio 58
'''
from random import randint
numpc = randint(0,10)
tenta = 0
print('***' * 15)
print('Adivinhe o numero o aleatorio (0 a 5).')
print(('***' * 15))
numuser = int(input('Qual seu palpite? '))
while numuser != numpc:
    if numuser < numpc:
        numuser = int(input('Voce disse {}. Um pouco mais alto.. Outro palpite? '.format(numuser)))
    else:
        numuser = int(input('Voce disse {}. Um pouco mais baixo.. Outro palpite? '.format(numuser)))
    tenta += 1
print('Voce disse {}. Acertou em {} tentativas!'.format(numuser, tenta))
'''

#exercicio 59
'''
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
opc = 0
while opc != 5:
    print('1 - Somar')
    print('2 - Multiplicar')
    print('3 - Maior')
    print('4 - Novos numeros')
    print('5 - Sair')
    opc = int(input('>>>Selecione a opção: '))
    if opc == 1:
        print('A soma de {} + {} é de {}'.format(n1, n2, n1+n2))
    elif opc == 2:
        print('O produto de {} x {} é de {}'.format(n1, n2, n1*n2))
    elif opc == 3:
        if n1 == n2:
            print('Os numeros são iguais ({})'.format(n1))
        elif n1 > n2:
            print('O {} é maior que {}'.format(n1, n2))
        else:
            print('O {} é maior que {}'.format(n2, n1))
    elif opc == 4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif opc == 5:
        print('Até mais.')
    else:
        print('Opção invalida. Tente novamente.')
print('Fim.')
'''

#exercicio 60

num = int(input('Digite o numero para descobrir o fatorial: '))
