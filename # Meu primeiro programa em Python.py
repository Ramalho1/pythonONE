print("\n\n\nOlá, mundo! 🐍") # python aceita emojis em forma de texto normal

# note que nesse print não tem "f" dentro do parênteses. O próximo terá
'''
esse é um comentário grande
com várias linhas... Se você escreve "\t", significará dar espaço
inclusive pode-se usar ele dentro do print, veja abaixo:
'''
name = "André Ramalho"
cargo = "Desenvolvedor Python"
email = "exatas@email.com"

print(f"""
================================
        Boas vindas ao sistema
================================
Nome:   {name}
Cargo:  {cargo}
Email:  {email}
================================
""")

'''f"texto {variavel}" → COM f-string

"texto" + variavel → SEM f-string

{ } dentro da f-string → local onde variáveis/expressões entram
'''

nome = input("Qual é o seu nome? \n")
idade1 = input("Qual sua idade? \n")
# o imput para o programa e aguarda a digitação. Ele vai receber e
# guardar como string


print(f"Prazer, {nome}! Você tem {idade1} anos. \n")


# para ler a idade como número, precisaríamos fazer:
constante = int(input("Digite mais um número pra somar"))

print(f"\n o número digitado foi: {constante} ")

'''se quisermos converter a idade1 para poder realizar operações 
matemáticas, precisaríamos fazer o exemplo abaixo:
'''
somaIdade=float(idade1) + constante
print(f"A soma das idade é: {somaIdade}")

import time
time.sleep(2)

# Operações matemáticas sem digitação
# Primeira coisa, devido a tipagem dinâmica do python, não precisamos
# evidenciar os tipos de variáveis de números

print (f"""\n Vamos trabalhar com dois números agora
       ======== :D ===== :D ======== :D ===========

       o primeiro número será '10' e o segundo o '5'

       ======== :D ===== :D ======== :D ===========\n""")
time.sleep(3)
numero1 = 8
numero2 = 5
resultado1 = numero1 + numero2
resultado2 = numero1 - numero2
resultado3 = numero1 * numero2
resultado4 = numero1 / numero2
resultado5 = numero1 ** numero2
resultado6 = numero1 ** (1/2)
resultado7 = numero1 ** (1/3)
resultado8 = numero1%numero2 
#Verificador de par ou ímpar
if numero1 % 2 ==0:
    print (f"o primeiro número que é {numero1} é par")
else: print (f"o primeiro número que é {numero1} é ímpar")
time.sleep(2)
print(f"""
operação de soma será: {resultado1}
operação de subtração será: {resultado2}
operação de multiplicação será: {resultado3}
operação de divisão será: {resultado4}
operação de potência será: {resultado5} 
operação de radiciação será: {resultado6}
operação de radiciação será: {resultado7}
      """) #rever os cálculos de potência
time.sleep(2)

#Operação com números digitados seguidos
n1, n2 = input("digite dois números seguidos, digitando espaço entre eles ").split()#dividir
n1 = float(n1)
n2 = float(n2)
n3 = n1 + n2 
print(f"A soma de {n1} + {n2} = {n3}") 
#Neste caso, o usuário precisa digitar clicando em 'espaço'
# entre os dois números
time.sleep(1)
# Lista da memória
frutas = ["maçã", "banana", "laranja"]
print(f"Minhas frutas favoritas: {frutas}")


# Lista digitada
print("Digite Cinco frutas separadas por vírgula")
frutas2=[]

for i in range(5):
    fruta = input(f"Digite a {i+1}° fruta ->")
    frutas2.append(fruta)  #método que adicionar elementos ao final da lista
print(f"As frutas são: {frutas2}")

print("Mais um teste memorizando números com declaração no início \n")
x = float(input("Digite um número: "))
y = float(input("Digite um número: "))

print("Vamos somar os números que você digitou")
resultado=x+y
print(f"O número: {x} mais o número: {y} é igual a {resultado}")


#outro exemplo de vetor para teste
print("Vamos preencher um vetor de número")
vetor=[]
for i in range(4):
   vetorN = input(f"Digite o vetor n° {i+1}  ")
   vetor.append(vetorN)
print (f"""O vetor na vertical será:
       V(1)= {vetor[0]}
       V(2)= {vetor[1]}
       V(3)= {vetor[2]}
       V(4)= {vetor[3]}
       """)