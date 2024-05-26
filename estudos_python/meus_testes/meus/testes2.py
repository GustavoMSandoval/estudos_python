#fun

'''def teste(valor):
    global x
    x = valor + 4
    


y  = 7
teste(y)
print(x)'''

'''def teste(x):
    x += x
    return x



y = 7
u = teste(y)
print(u)'''
#matriz

'''linhas = int(input("Quantas linha? "))
colunas = int(input("Quantas colunas? "))
matriz = []

for l in range(linhas):
    linha = []#é necessário que fique aqui pela iteração
    for c in range(colunas):
        valor = input(f"Qual o valor para linha {l} e coluna {c}")
        linha.append(valor)
    matriz.append(linha)

for linha in matriz:
    for valor in linha:
        print(f"{valor:^5}",end='')
    print()'''

#matrizes

'''x  = [ 8 + 1]
y = [4 + 1]'''

'''for v in x:
    for u in y:
        continue

for v in y:
    for v in x:
        continue'''
        

'''print(x,y)'''


#valores para senha

'''char = '1234567890'

n = input("digite")
if n not in char:
    for x in n:
        if x not in char:
          print(f'ERRO valor {x} não passou')
else:
    print("passou")'''

'''from random import randint

n= randint(1,5)
op = int(input("Digite"))
if n == op:
    print("boa")
else:
    print("Errouuuuu o número era",n)'''

'''maior =0
menor =0
for p in range(1,6):
    peso = float(input("DIgite o peso"))

    if p == 1:
       maior = peso
       menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(maior,menor)'''


#maior e menor
'''pesos = [float(input('Peso da {}º pessoa: '.format(a))) for a in range(1, 6)]
print('O maior peso foi de {}Kg\n'
      'O menor foi de {}Kg!'.format(max(pesos), min(pesos)))'''

'''
row = int(input("Digite o valor"))
for c  in range(1,row + 1):
    print('*'*c,end='')
    print(' ')
'''

#nome capitalizado
'''nome = "gustavo moreira"
nome = nome.title()
print(nome)'''

#juntar
'''name = "bro code"
name = name.replace(" ",'')
print(name)
print(name.isalpha())'''

#abrir arquivo

'''with open("arquivo.txt","r") as arq:
    texto = arq.read()
lista_texto = texto.split("\n")

faturamento = 0
#excluir primeira linha
lista_texto = lista_texto[1:]

for linha in lista_texto:
    posicao_pv = linha.find(";")
    valor = float(linha[posicao_pv+1:])
    faturamento += valor
print(faturamento)'''

#arquivo
'''with open("arquivo.txt","r") as arquivo:
    texto = arquivo.read()
linhas_texto = texto.split("\n")
faturamento = 0
linhas_texto = linhas_texto[1:]

for linhas in linhas_texto:
    posicao_pontoVirgula = linhas.find(';')
    valor = float(linhas[posicao_pontoVirgula+1:])
    faturamento += valor
print(faturamento)
'''
#senha

senha = '1@23aA$3'
val = ' '
cn = clma = clmi = cc  = 0
if len(senha) < 5:
    print('senha inválida')
for v in senha:
    if v  in '1234':
       cn +=1
    elif v in '@#$%':
       cc += 1  
    elif v in 'ABCD':
       clma+=1
    elif v in 'abcd':
       clmi += 1

if cn == 0 or cc == 0 or clma == 0 or clmi == 0:
    print('f')
else:
    print('v')


#técnico
'''lista = [1,2,3,5,6,10]
contador = 0
for valores in range(1,lista[-1]+1):
    contador += 1
    if contador not in lista:
        print(f"Esse era o que faltava {contador}")'''

  