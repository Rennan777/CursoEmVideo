frase = 'Curso em Video Python'
print(frase[9:21])      #intervalo
print(frase[9:21:2])    #pulando 2 caracteres
print(frase[:5])        #do inicio ate o 5o caractere
print(frase[9:])        #do 9o caractere ate o fim
print(frase[9::3])      #pulando 3 caracteres
print(len(frase))       #medida da variavel
frase.count('o')        #contagem letra 'o'
frase.count('o', 0, 13) #contagem letra 'o', no intervalo entre caracteres 0 e 13
frase.find('deo')       #exibe onde iniciou (posição) a cadeia de caracteres
frase.find('Android')   #exemplo de string nao encontrada
'Curso' in frase        #retorna true or false
frase.replace('Python', 'Android')  #substitui string
frase.upper()           #maiusculo
frase.lower()           #minusculo
frase.capitalize()      #apenas primeira em maiusculo
frase.title()           #todas iniciais em maiusculo
frase.strip()           #remove espaços inicio e fim
frase.rstrip()          #remove espaços direita/final
frase.lstrip()          #remove espaços esquerda/inicio

frase.split()           #divisão nos espaços, formando lista (lista = [1, 2, 3, 4])
'-'.join(frase)         #transforma lista em string unica
