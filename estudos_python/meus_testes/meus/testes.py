#matriz
'''matriz = [[0,0,0],[0,0,0],[0,0,0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = input('digite')
print('-='*30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end='')
    print()'''

'''palavra = "cat"
reversed_palavra = ''.join(reversed(palavra))
print(reversed_palavra)'''

'''for c in range(10,-1,-1):
    print(c)'''

'''def fat(n):
    f = 1
    while n > 1:
        f *= n
        n -= 1
        print(n,f)

num = int(input('digite'))
fat(num)
'''
'''lista = ["a","i","b"]
lista.sort()
print(lista)'''

'''from random import randint
import os

player = {"nome":"python","x":0,"y":0}

def andar(direction):
    if direction == "d":
        player['x'] += 1
    elif direction == "a":
        player['x'] -=1
    elif direction == "w":
        player['y'] -=1
    elif direction == "s":
        player['y'] += 1

while True:
    os.system('clear')

    print("-"*30)
    for y in range(5):
        print("\n")
        for x in range(10):
            if player ['x'] == x and player ['y'] == y:
                print("J",end="")
            else:
                print("()",end="")
    print("-"*30)

    direction = input("Proxima direção")
    andar(direction)'''

'''matriz = [[0,0,0],[0,0,0],[0,0,0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = input('Digite um valor')
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end='')
    print()'''

#Quando declaramos uma lista Python com num = [3, 6, 4, 1] e executamos a estrutura for n1, n2 in enumerate(num): com o comando print(n1 + n2) dentro do bloco do laço, quais valores 
# serão exibidos?

'''num = [3,6,4,1]
for n1,n2 in enumerate(num):
    print(n1+n2)
'''
'''cont = 1
soma = 0
while cont < 11:
    user_input = input(f'digite o {cont}: ')

    if user_input.strip() == '':# para separar e achar o que falta 
        n = 0
    else:
        n = int(user_input)

    soma += n
    cont += 1

print(f'essa foi a soma {soma} e essa foi a média {soma/cont:.2f}')
'''
#matriz melhorada

'''linhas = int(input('Quantas linhas? '))
colunas = int(input('Quantas colunas? '))

matriz = []

for l in range(linhas):
    linha = []
    for c in range(colunas):
        valor = input(f'Digite o número para linha {l} e coluna {c}')
        linha.append(valor)
    matriz.append(linha)#deve ficar dessa maneira para que fique fora do laço C

for linha in matriz:
    for valor in linha:
        print(f"[{valor:^5}]",end='')
    print()# para que fique em forma de matriz'''
     

#Trava zap
'''import pyautogui as py
import random
import time

time.sleep(5)

mensagens = ["ta doidao","Qual foi ","idiotakkk","eae gordao","calabreso","pac man angolano"]

for i in range(500):
    MSG = random.choice(mensagens)
    py.write(MSG)
    py.press("Enter")'''

#soma impares
'''
r = 0
while True:
    num = int(input('digite um valor'))
    op = str(input('SN'))
     
    if num % 2 != 0:
        impares = []
        impares.append(num)
        for n in impares:
           r += n
           impar = []
           impar.append(n)
    else:
         par = [] 
         par.append(num)
    if op in 'Nn':
          break
   
print(f'ímpares {impar}e resultado{r}')   '''
 
'''arquivo = open('arquivo.txt','w')'''
'''num = int(input("numero "))
for c in range(10):
     c +=1
     n = num
     n *= c
     arquivo.write(str(n)+"\n")
'''
'''nomes = []
for c in range(3):
    nome = input("digite o nome")
    nomes.append(nome)
    arquivo.write(nome+"\n")
for nome in nomes:
    print(nome)


arquivo.close()
'''

'''def fatorial(n):
    f = 1
    for num in range(1,n+1):
        c = num
        f*=c
    return f



num = int(input("digite um número"))
fatorial(num)
print(fatorial(num))'''

#Binário
'''num = int(input("DIgite um número"))
while num != 1:
    num //= 2
    resto = num % 2
    print(resto)
print(num)'''

'''senha = input("digite senha")
if len(senha) < 8:
    print("inválido")'''




'''a = 0

def s(a,b):
   a == b + 1
   return a

r = s(5,6)
print(r)'''

#match

'''dia = "noite"
match dia:
    case "dia":
        print("bom dia")
    case "noite":
        print("eita")
'''

#dinheiro

'''din = 543.50

op = input("What do you want to buy").lower()


match op:
    case "pizza":
        din -= 5.78
    case "hamburguer":
        din -= 7.89
    case "chocolate":
        din -= 2.54
print(din)
'''
'''n = 0
meta = 500
demitido ="demitido"
for c in range(3):
    s = int(input("Digite um npuero"))
    n += s
if meta > n:
    print(demitido)
print(n)'''


#teste roupas
'''lista = []
while True:
       cad = input("Qual o número da roupa?")
       op= int(input("""
        1-Aprovado
        2-reprovado"""))
       
       lista.append(cad)
       if op == 1:
        ap = "aprovado"
        lista.append(ap)
        
       elif  op == 2:
        ap = "reprovado"
        lista.append(ap)
       else:
          lista.remove(cad[-1])
          break
print(lista)'''


#média dentro de um dcionário

'''lista = []
cad = {}

idades = 0
i = 0
for c in range(3):
       cad["nome"] = input("nome ")
       cad["idade"] = int(input("idade "))
       cad["sexo"] = input("sexo ")
       lista.append(cad.copy())


for val in lista:
       idades += val["idade"]
       i+=1
       media = idades/i
print(f"{media:.2f}")
'''

#média básico
'''i = 0
idades = 0
for c in range(0,3):
    idade = int(input("QUal a sua idade"))
    i +=1
    idades += idade
media = idades/i
print(media)'''

