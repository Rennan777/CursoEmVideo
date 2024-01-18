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
# import random

# from time import sleep

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

# exercicio 20
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

# exercicio 21
'''
import pygame
pygame.init()
pygame.mixer.music.load('back.mp3')
pygame.mixer.music.play()
pygame.event.wait()
'''

# exercicio 22
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

# exercicio 23
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

# exercicio 24
'''
cid = str(input('Em que cidade voce nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')
'''

# exercicio 25
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

# exercicio 26
'''
frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira aparição da letra A é na posição {}'.format(frase.find('A')+1))
print('A ultima aparição da letra A é na posição {}'.format(frase.rfind('A')+1))
'''

# exercicio 27
'''
nome = str(input('Digite seu nome completo: ')).strip()
listnome = nome.split()
print('Seu primeiro nome é {}'.format(listnome[0]))
print('Seu ultimo nome é {}'.format(listnome[-1]))
## print('Seu ultimo nome é {}'.format(listnome[len(listnome)-1]))
'''

# exercicio 28
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

# exercicio 29
'''
vel = float(input('Qual a velocidade do veiculo? '))
multa = (vel-80)*7
if vel < 81:
    print('Voce esta dentro do limite de velocidade. Continue assim. Boa viagem')
else:
    print('Voce esta acima do limite de 80 km/h! Voce será multado em R$ {:.2f}'.format(multa))
'''

# exercicio 30
'''
num = int(input('Me diga um numero qualquer: '))
result = num % 2
if result == 0:
    print('O numero {} é PAR.'.format(num))
else:
    print('O numero {} é IMPAR.'.format(num))
'''

# exercicio 31
'''
dist = float(input('Qual a distancia da sua viagem? '))

if dist > 200:
    preco = dist * 0.45
else:
    preco = dist * 0.5

#preco = dist * 0.45 if dist <= 200 else dist * 0.5
print(('O preço da passagem é de R$ {:.2f}'.format(preco)))
'''
# exercicio 32
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

# exercicio 33
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

# exercicio 34
'''
sal = float(input('Qual o salário do funcionário? '))
if sal <= 1250:
    nsal = sal + ((sal/100) * 15)
else:
    nsal = sal + ((sal/100) * 10)
print('O funcionário recebia R$ {:.2f}. O novo salário será de R$ {:.2f}'.format(sal, nsal))
'''

# exercicio 35
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

# exercicio 36
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

# exercicio 37
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

# exercicio 38
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

# exercicio 39
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

# exercicio 40
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

# exercicio 41
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

# exercicio 43
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

# exercicio 44
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

# exercicio 45
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

# exercicio 46
'''
from time import sleep
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('kabum!!!')
'''

# exercicio 47
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

# exercicio 48
'''
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        soma += c
print('A soma de todos os {} valores é de {}.'.format(cont, soma))
'''

# exercicio 49
'''
n = int(input('Digite um numero inteiro: '))
print('=*' * 8)
for c in range(1, 11):
    print('{} x {} = {}'.format(c, n, c * n))
print('=*' * 8)
'''

# exercicio 50
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

# exercicio 51
'''
p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
dec = p +(10 - 1 ) * r      #calculo decimo termo da razão
for c in range(p, dec + r, r):
    print(p, end='- ')
    p += r
print('Fim')
'''

# exercicio 52
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

# exercicio 53
# com 'for'
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
# sem 'for'
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

# exercicio 54
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

# exercicio 55
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

# exercicio 56
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

# exercicio 57
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

# exercicio 58
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

# exercicio 59
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

# exercicio 60
'''
numx = 1
num = int(input('Digite o numero para descobrir o fatorial: '))
print('Calculo {}! = '.format(num),end='')
while num > 0:
    print(num, end='')
    print(' x ' if num > 1 else ' = ', end='')
    numx *= num
    num -= 1
print(numx)
'''
'''
from math import factorial
num = int(input('Digite o numero para descobrir o fatorial: '))
f = factorial(num)
print('O fatorial de {} é {}.'.format(num, f))
'''

# exercicio 61
'''
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} - '.format(termo),end='')
    termo += razao
    cont += 1
print('Fim')
'''

# exercicio 62
'''
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razao: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} - '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Mostrar mais quantos termos? '))
print('Progressão finalizada com {} termos mostrados'.format(total))
'''

# exercicio 63
'''
n = int(input('Quantos termos voce quer mostrar? '))
t1 = 0
t2 = 1
print('{} - {}'.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' - {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' - Fim')
'''

# exercicio 64
'''
cont = 0
total = 0
num = int(input('Digite um valor: [999 para sair]: '))
while num != 999:
    total += num
    cont += 1
    num = int(input('Digite um valor: [999 para sair]: '))
print('Foram digitados {} numeros e a soma de todos é de {}'.format(cont, total))
'''

# exercicio 65
'''
r = 'S'
cont = 0
soma = 0
maior = 0
menor = 0
while r in 'Ss':
    num = int(input('Digite um numero: '))
    cont += 1
    soma += num
    if cont == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    r = str(input('Continuar? [S/N]')).upper().strip()[0]
media = soma / cont
print('Foram digitados {} numeros. A media é de {}, o menor foi {} e o maior foi {}.'.format(cont, media, menor, maior))
'''

# exercicio 66
# break
'''
cont = 0
soma = 0
while True:
    valor = int(input('Digite um valor: [999 Sair] '))
    if valor == 999:
        break
    cont += 1
    soma += valor
print(f'Foram digitados {cont} e o a soma total é de {soma}')
'''

# exercicio 67
'''
while True:
    print('--' * 10)
    num = int(input('Tabuada de: [Negativo para finalizar] '))
    if num < 0:
        break
    for t in range(1, 11):
        prod = t * num
        print(f'{num} x {t} = {prod}')
print('Finalizado')
'''

# exercicio 68
'''
from random import randint
cont = 0
while True:
    pc = randint(1, 10)
    jog = int(input('Digite um numero: '))
    tot = (pc + jog)
    if tot % 2 == 0:
        game = 'PAR'
    else:
        game = 'IMPAR'
    escolha = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    if escolha == 'I' and game == 'IMPAR':
        cont += 1
        print(f'Voce jogou {jog} e o pc jogou {pc}. Total {tot}. Deu IMPAR. Voce GANHOU.')
    elif escolha == 'P' and game == 'PAR':
        cont += 1
        print(f'Voce jogou {jog} e o pc jogou {pc}. Total {tot}. Deu PAR. Voce GANHOU.')
    else:
        print(f'Voce jogou {jog} e o pc jogou {pc}. Total {tot}. Deu {game}')
        print('PERDEU')
        break
print(f'Fim do jogo! Voce venceu {cont} vezes.')
'''

# exercicio 69
'''
mais18 = 0
homem = 0
mulher20 = 0
while True:
    sex = str(input('Qual o sexo: [H/M]')).strip().upper()[0]
    if sex in 'HM':
        idade = int(input('Qual a idade: '))
        if idade > 18:
            mais18 += 1
        if sex in 'Hh':
            homem += 1
        if sex in 'Mm' and idade < 20:
            mulher20 += 1
        continua = str(input('Continuar? [S/N]')).upper().strip()[0]
        if continua == 'N':
            print('Saindo.')
            break
    else:
        print('Escolha Invalida. Tente novamente')
print(f'Fim do programa. {mais18} pessoas tem mais de 18 anos. {homem} são homens. {mulher20} mulher(es) tem menos de 20 anos.')
'''
'''
mais18 = 0
homem = 0
mulher20 = 0
while True:
    sex = ' '
    while sex not in 'HM':      #adicionado while curso, para testar resposta certa
        sex = str(input('Qual o sexo: [H/M]')).strip().upper()[0]
    if sex in 'HM':
        idade = int(input('Qual a idade: '))
        if idade > 18:
            mais18 += 1
        if sex in 'H':
            homem += 1
        if sex in 'M' and idade < 20:
            mulher20 += 1
        continua = ' '
        while continua not in 'SN': #adicionado while curso, para testar resposta certa
            continua = str(input('Continuar? [S/N]')).upper().strip()[0]
        if continua == 'N':
            print('Saindo.')
            break
    else:
        print('Escolha Invalida. Tente novamente')
print(f'Fim do programa. {mais18} pessoas tem mais de 18 anos. {homem} são homens. {mulher20} mulher(es) tem menos de 20 anos.')
'''

# exercicio 70
'''
total = 0
mais1k = 0
barato = ''
pbarato = 0
while True:
    produto = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o valor do produto: '))
    total += preco
    if preco > 1000:
        mais1k += 1
    if barato == '':
        barato = produto
        pbarato = preco
    if preco < pbarato:
        pbarato = preco
        barato = produto
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continua == 'N':
        print('Finalizando.')
        break
print(f'O total da compra foi de R${total:.2f}, {mais1k} produtos valem mais de R$ 1000. O produto mais barato é {barato}.')
'''

# exercicio 71
'''
saque = int(input('Qual valor a ser sacado: '))
ced = 50
totced = 0
while True:
    if saque >= ced:
        saque -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cedulas de {ced}')
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if saque == 0:
            break
print('Finalizado')
'''

# exercicio 72
'''
nums = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
        'onze', 'doze', 'treza', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
continua = 'S'
while continua == 'S':
    escolha = int(input('Digite um numero de 0 a 20: '))
    while escolha < 0 or escolha > 20:
        print('Numero invalido.')
        escolha = int(input('Digite um numero de 0 a 20: '))
    print(f'numero digitado foi', nums[escolha])
    continua = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    while continua not in 'SN':
        print('Escolha invalida.')
        continua = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if continua == 'N':
        break
print('Fim')
'''

# exercicio 73
'''
times = ('Botafogo', 'Red Bull Bragantino', 'Grêmio',
         'Palmeiras', 'Flamengo', 'Fortaleza', 'Fluminense',
         'Athletico-PR', 'Atlético-MG', 'São Paulo', 'Cuiabá',
         'Inter', 'Corinthians', 'Santos', 'Cruzeiro', 'Bahia',
         'Vasco', 'Goiás', 'Coritiba', 'América-MG')
print('==' * 15)
print('Os 20 times são: ', times)
print('==' * 15)
print('Os 5 primeiros colocados são: ', times[:5])
print('==' * 15)
print('Os cinco ultimos colocados são: ', times[-4:])
print('==' * 15)
print('Os times em ordem alfabetica: ', sorted(times))
print('==' * 15)
print('Goiás esta na posição: ', times.index('Goiás')+1)
print('==' * 15)
'''

# exercicio 74
'''
from random import randint
nums = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
for n in nums:
    print(n, end='')
print(f'\nO maior valor é: {max(nums)}')
print(f'O menor valor é: {min(nums)}')
'''

# exercicio 75
'''
nums = (int(input('Digite um numero: ')),
        int(input('Digite outro numero: ')),
        int(input('Digite mais um numero: ')),
        int(input('Digite o ultimo numero: ')))
nove = nums.count(9)
print(f'Voce digitou os seguintes numeros: {nums}')
print(f'O numero 9 se repete {nove} vezes.')
if 3 in nums:
    tres = nums.index(3)
    print(f'O numero 3 aparece pela primeira vez na posição {tres + 1}')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')
print('Os Valores pares são: ', end='')
for n in nums:
    if n % 2 == 0:
        print(f'{n}', end=' ')
print('\nFim')
'''

# exercicio 76
'''
lista = ('Lapis', 1.75,
         'Borracha', 2,
         'Caderno', 15.90,
         'Estojo', 25,
         'Transferidor', 4.20,
         'Compasso', 9.99,
         'Mochila', 120.32,
         'Canetas', 22.30,
         'Livro', 34.90)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for i in range(0, len(lista)):
    if i % 2 == 0:
        print(f'{lista[i]:.<30}', end='')
    else:
        print(f'R${lista[i]:>7.2f}')
print('-' * 40)
'''

# exercicio 77
'''
tupla = ('Abacate', 'Teclado', 'Copo', 'Mesa', 'Arroz', 'Chafariz', 'Carro', 'Porta')
indice = 'AEIOUaeiou'
for palavra in tupla:
        print(f'\nA palavra {palavra} tem: ', end='')
        for vogal in palavra:
            if vogal in indice:
                print(vogal, end=' ')
'''

# exercicio 78
'''
lista = []
for c in range (0, 5):
    n = int(input(f'Digite um valor para posição {c}: '))
    lista.append(n)
print(f'Voce digitou os numeros: {lista}')
maior = max(lista)
menor = min(lista)
print(f'O maior valor é {maior} e está nas posições: ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}... ', end='')
print(f'\nO menor numero é {menor} e está nas posições: ', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}... ', end='')
'''

# exercicio 79
'''
r = 'S'
lista = list()
while r in 'S':
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
    else:
        print('Valor ja foi incluido.')
    r = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while r not in 'SN':
        print('Escolha invalida')
        r = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
print(f'Valores digitados: {sorted(lista)}')
'''

# exercicio 80
'''
lista = list()
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
    else:
        pos = 0
        while pos <len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1
print(f'Valores digitados: {lista}')
'''

# exercicio 81
'''
r = 'S'
c = 0
lista = []
while r == 'S':
    n = int(input('Digite um valor: '))
    lista.append(n)
    c += 1
    r = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while r not in 'SN':
        print('Resposta invalida.')
        r = str(input('Deseja continuar: [S/N]')).strip().upper()[0]
print(f'Foram digitados {c} numeros.')
print(f'Lista ordenada decrescente: {sorted(lista, reverse=True)}')
if 5 in lista:
    print('O numero 5 está na lista.')
else:
    print('O numero 5 não está na lista')
'''
'''
valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
print('*==' * 10)
print(f'Voce digitou {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print('O valor 5 está na lista')
else:
    print('O valor 5 não está na lista.')
'''
# exercicio 82
'''
lista = []
par = []
impar = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    resp = str(input('Deseja continuar? [S/N] '))
    if resp in 'Nn':
        break
print(f'Sua lista: {lista}')
print(f'Pares: {sorted(par)}')
print(f'Impares: {sorted(impar)}')
'''
# exercicio 83
'''
abre = 0
fecha = 0
exp = str(input('Digite sua expressao: '))
for i in exp:
    if i == '(':
        abre += 1
    elif i == ')':
        fecha += 1
print(f'Sua expressao: {exp}')
if abre == fecha:
    print('Sua expressao esta correta')
else:
    print('Sua expressao tem um problema')
'''

'''
expr = str(input('Digite a expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha. append ('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha. append(') ')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
'''
# exercicio 84
'''
geral = list()
pessoa = list()
maior = menor = 0
while True:
    pessoa.append(str(input('Digite o nome: ')))
    pessoa.append(float(input('Digite o peso: ')))
    if len(geral) == 0:
        maior = menor = pessoa[1]
    else:
        if pessoa[1] > maior:
            maior = pessoa[1]
        if pessoa[1] < menor:
            menor = pessoa[1]
    geral.append(pessoa[:])
    pessoa.clear()
    continuar = str(input('Deseja inserir mais pessoas: [S/N]'))
    if continuar in 'Nn':
        break
print(f'Foram cadastradas {len(geral)} pessoas.')
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for p in geral:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {menor}Kg. Peso de ', end='')
for p in geral:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
print()

'''

# exercicio 85
'''
listpar = list()
listimpar = list()
lista = [listpar, listimpar]
for x in range(7):
    n = int(input(f'Digite o {x + 1}o valor: '))
    if n % 2 == 0:
        listpar.append(n)
    else:
        listimpar.append(n)
print(f'Pares: {sorted(listpar)}')
print(f'Impares: {sorted(listimpar)}')
'''

# exercicio 86
'''
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(3):
    for coluna in range(3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
print('*=' * 10)
for linha in range(3):
    for coluna in range(3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
'''

# exercicio 87
'''
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = 0
terceira = 0
maior = 0

for linha in range(3):
    for coluna in range(3):
        x = int(input(f'Digite um valor para {linha}, {coluna}: '))
        maior = x
        matriz[linha][coluna] = x
        if x % 2 == 0:
            pares += x
#soma terceira coluna
for linha in range(3):
    terceira += matriz[linha][2]
#maior segunda linha
for coluna in range(3):
    if coluna == 0:
        maior = matriz[1][coluna]
    elif matriz[1][coluna] > maior:
        maior = matriz[1][coluna]

print('*=' * 15)
for linha in range(3):
    for coluna in range(3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
print('*=' * 15)
print(f'A soma dos valores pares é de: {pares}')
print(f'A soma dos valores da terceira coluna é: {terceira}')
print(f'O maior valor da segunda linha é: {maior}')
'''

# exercicio 88
'''
from random import randint
from time import sleep
listao = list()

qtd = int(input('Quantos jogos? '))

for jogo in range(qtd):
    lista = []
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    listao.append(lista)

for i, l in enumerate(listao):
    print(f'{i + 1}o jogo: {sorted(l)}')
    sleep(1)
print('Fim')
'''

# exercicio 89
'''
alunos = list()
continua = 'S'

print('** Digite o nome e 2 notas dos alunos. **')
while continua in 'Ss':
    aluno = list()
    aluno.append(str(input('Nome: ')))
    aluno.append(float(input('Nota 1: ')))
    aluno.append(float(input('Nota 2: ')))
    alunos.append(aluno)
    continua = str(input('Deseja continuar? [S/N]'))[0]

print('**' * 15)
print('No. NOME      MEDIA')
print('--' * 10)
for i, a in enumerate(alunos):
    print(f'{i:<2} {a[0]:<10} {(a[1] + a[2]) / 2:>5.2f}')
print('--' * 10)
while True:
    notas = int(input('Exibir notas de qual aluno? (999 para sair): '))
    if notas == 999:
        print('Programa Finalizado')
        break
    else:
        if notas < len(alunos):
            print(f'Notas de {alunos[notas][0]}: {alunos[notas][1]}, {alunos[notas][2]}')
            print('--' * 11)
        else:
            print('Digite um numero de aluno valido')
'''

# exercicio 90
'''
aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Media de {aluno["nome"]}: '))
if aluno['media'] <= 5:
    aluno['status'] = 'Reprovado'
if aluno['media'] <= 7:
    aluno['status'] = 'Recuperacao'
else:
    aluno['status'] = 'Aprovado'

print('=-' * 10)
#print(f'- Nome é {aluno["nome"]}\n- Media é {aluno["media"]}\n- Situação é {aluno["status"]}')
for k, v in aluno.items():
    print(f'{k} é {v}')
'''

# exercicio 91
'''
from random import randint
from time import sleep
from operator import itemgetter
jogadores = {'jogador1': randint(1, 6),
             'jogador2': randint(1, 6),
             'jogador3': randint(1, 6),
             'jogador4': randint(1, 6)}
rank = list()
print('*-' * 15)
for k, v in jogadores.items():
    print(f'O {k}, tirou {v} no dado.')
    sleep(0.5)
rank = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('*-* RANKING *-*')
for i, v in enumerate(rank):
    print(f'{i + 1}o lugar: {v[0]}, com {v[1]} pontos.')
    sleep(0.5)
'''

# exercicio 92
'''
from datetime import date #datetime
#hoje = datetime.now().year
hoje = date.today()
anoatual = hoje.year
pessoa = dict()
pessoa['nome'] = str(input('Nome: '))
pessoa['nascimento'] = int(input('Ano de nascimento: '))
pessoa['idade'] = anoatual - pessoa['nascimento']
if pessoa['idade'] >= 18:
    pessoa['ctps'] = int(input('CTPS (0 para nao possui): '))
    if pessoa['ctps'] != 0:
        pessoa['contratacao'] = int(input('Ano de contratação: '))
        pessoa['salario'] = float(input('Salário: '))
        pessoa['aposentadoria'] =  (35 - (anoatual - pessoa['contratacao'])) + pessoa['idade']
for k, v in pessoa.items():
    print(f'- {k} é {v}')
'''

# exercicio 93
'''
jogador = dict()
jogador['nome jogador'] = str(input('Nome do jogador: '))
jogador['total_partidas'] = int(input('Quantidade de partidas jogadas: '))
golstotais = 0
for partida in range(1, jogador['total_partidas'] + 1):
    golpartida = int(input(f'Quantos gols na partida {partida}? '))
    jogador[f'partida{partida}'] = golpartida
    golstotais += golpartida
jogador['total de gols'] = golstotais
for k, v in jogador.items():
    print(f'{k} = {v}')
    
#############################

jogador = {}
jogador['nome'] = str(input('Nome do jogador: '))
jogador['partidas'] = int(input('Quantidade de partidas jogadas: '))
gols = []
total_gols = 0
for partida in range(1, jogador['partidas'] + 1):
    tot_partida = int(input(f'Quantos gols na partida {partida}? '))
    gols.append(tot_partida)
    total_gols += tot_partida
jogador['gols'] = gols
jogador['total'] = total_gols
print('=-' * 15)
print(jogador)
print('=-' * 15)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('=-' * 15)
print(f'O jogador {jogador["nome"]}, jogou {jogador["partidas"]} partidas')
for i, g in enumerate(jogador['gols']):
    print(f'Na partida {i + 1}, o jogador fez {g} gols.')
print(f'Foi um total de {jogador["total"]} gols.')

'''

# exercicio 94
'''
pessoas = []
continuar = 'S'
while 'S' in continuar:
    pessoa = {}
    pessoa['nome'] = str(input('Digite o nome: '))
    while True:
        pessoa['sexo'] = str(input('Digite o sexo [M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Favor, digite somente [M ou F]:')
    pessoa['idade'] = int(input('Digite a idade: '))
    pessoas.append(pessoa)
    while True:
        continuar = str(input('Deseja adicionar outra pessoa? [S/N]')).upper()[0]
        if continuar in 'SN':
            break
        print('Favor selecionar opção correta. [S/N]')
print('-=-=' * 10)
print(f'{len(pessoas)} pessoas foram cadastradas.')
totidades = 0
for i in pessoas:
    totidades += i['idade']
mediaidade = (totidades / len(pessoas))
print(f'A media das idades é {mediaidade:.0f}.')
print(f'As mulheres são: ', end='')
for i in pessoas:
    if i['sexo'] == 'F':
        print(f'{i["nome"]}, ', end='')
print()
print(f'As pessoas com idade acima da media são: ', end='')
for i in pessoas:
    if i['idade'] > mediaidade:
        print(f'{i["nome"]}, com {i["idade"]} anos. ', end='')
print('-=-=' * 10)
'''

# exercicio 95
'''
jogadores = []
continuar = 'S'
while continuar == 'S':
    jogador = {}
    jogador['nome'] = str(input('Nome do jogador: '))
    jogador['partidas'] = int(input('Quantidade de partidas jogadas: '))
    gols = []
    total_gols = 0
    for partida in range(1, jogador['partidas'] + 1):
        tot_partida = int(input(f'Quantos gols na partida {partida}? '))
        gols.append(tot_partida)
        total_gols += tot_partida
    jogador['gols'] = gols
    jogador['total'] = total_gols
    jogadores.append(jogador)
    while True:
        continuar = str(input('Deseja adicionar outra pessoa? [S/N]')).upper()[0]
        if continuar in 'SN':
            break
        print('Favor selecionar opção correta. [S/N]')

print('=-' * 15)
print('cod   ', end='')
for i in jogadores[0].keys():
    print(f'{i:<15}', end='')
print()
for i, j in enumerate(jogadores):
    print(f'{i:<5} ', end='')
    for d in j.values():
        print(f'{str(d):<15}', end='')
    print()
print('=-' * 15)

while True:
    exibir = int(input('Exibir dados de qual jogador? [999 para encerrar] '))
    if exibir == 999:
        break
    elif exibir > len(jogadores) or exibir < 0:
        print('Valor invalido')
    else:
        print(f'-- Dados do jogador {jogadores[exibir]["nome"]}: ')
        for i, g in enumerate(jogadores[exibir]['gols']):
            print(f'--- No jogo {i + 1} fez {g} gols.')
    print('=-' * 15)
print('Encerrando...')
'''

# exercicio 96
'''
def area(largura, comprimento):
    area = largura * comprimento
    print(f'A área de um terreno {largura}x{comprimento} é de {area} metros quadrados.')


l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l, c)
'''

# exercicio 97
'''
def escreva(frase):
    tamanho = len(frase) + 4
    print('~' * tamanho)
    print(f'  {frase}  ')
    print('~' * tamanho)


f = str(input('Digite sua frase: '))
escreva(f)
'''

# exercicio 98
'''
from time import sleep


def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print(f'Contagem de {inicio} a {fim} de {passo} em {passo}: ')
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont} ', end='')
            cont += passo
            sleep(0.5)
        print('Fim')
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont} ', end='')#
            cont -= passo
            sleep(0.5)
        print('Fim')

def espaco():
    print('=-' * 20)

espaco()
contador(1, 10, 1)
espaco()
contador(10, 0, 2)
espaco()
print('Contagem personalizada')
i = int(input('Digite o numero inicial: '))
f = int(input('Digite o numero final: '))
p = int(input('Digite o passo: '))
contador(i, f, p)
'''

# exercicio 99
'''
from time import sleep

def espaco():
    print('=-' * 20)


def maior(* valores):
    espaco()
    print('Analisando os valores passados...')
    m = 0
    cont = 0
    for i, valor in enumerate(valores):
        sleep(0.5)
        print(f'{valor} ', end='')
        if i == 0:
            m = valor
        else:
            if valor > m:
                m = valor
        cont += 1
    sleep(0.5)
    print(f'\nForam passados {cont} valores ao todo')
    sleep(0.5)
    print(f'O maior valor foi {m}.')


maior(5, 7, 4, 7, 9, 8, 3)
maior(1, 5, 8, 7, 10, 5)
maior(1, 2)
maior(0)
maior(6)
maior()
espaco()
'''

# exercicio 100
'''
from random import randint
from time import sleep

def espaco():
    print('-=' * 20)


def sorteia():
    espaco()
    print('Sorteando 5 valores: ', end='')
    lista = []
    for n in range(0, 5):
        sort = randint(0, 10)
        lista.append(sort)
        print(f'{sort} ', end='')
        sleep(0.2)
    print()
    return lista



def soma(valores):
    espaco()
    somando = 0
    cont = 0
    for n in valores:
        if n % 2 == 0:
            somando += n
            cont += 1
    print(f'Somando os {cont} valores pares, o resultado é {somando}.')


soma(sorteia())

#x = sorteia()
#soma(x)
'''

# exercicio 101
"""

def voto(nascimento):
    '''
    ->  Informe o ano de nascimento e receba informação sobre obrigatoriedade de voto.
    :param nascimento: ano de nascimento
    :return: printa na tela sobre a obrigatoriedade de voto
    '''
    from datetime import datetime
    anoatual = datetime.now().year
    idade = anoatual - nascimento
    print(f'Com {idade} anos: ', end='')
    if idade < 16:
        return 'Não pode votar ainda..'
    elif 16 <= idade < 18 or idade >= 65:
        return 'Voto opcional.'
    else:
        return 'Voto obrigatório.'


nascimento = int(input('Digite o ano de nascimento: '))
print(voto(nascimento))

#help(voto)
"""

# exercicio 102

"""
def fatorial(num=1, show=False):
    '''
    -> Função para calculo de fatorial
    :param num: Numero inteiro a ser calculado
    :param show: Exibir os calculos [True/False]
    :return: retorna o fatorial do valor informado
    '''
    print('--' * 20)
    f = 1
    for c in range(num, 0, -1):
        f *= c
        if show:
            print(f'{c} ', end='')
            if c > 1:
                print('x ', end='')
            else:
                print('= ', end='')
    return f


print(fatorial(5, True))
print(fatorial(5))
help(fatorial)

"""

# exercicio 103