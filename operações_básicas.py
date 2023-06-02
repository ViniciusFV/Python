# tipos de valores 

# int = valores numéricos inteiros

A = 4
B = 2

print(type(A))
print(type(B))

# float =  valores numéricos com casas decimais

C = 1.5
D = 3.5

print(type(C))
print(type(D))

# string = valores de texto, interpretados como padrao em uma variavel de input
# por convenção usamos aspas simples para definir uma string

E = 'Jeff'
F = 'Mascaico'

print(type(E))
print(type(F))

# boolean = valores que só podem ser 2, mais conhecidos como binarios 1 e 0, ou True e False
# representam respsota de condições

G = C == D

print(type(G))
print(G)


# operações basicas de contas, soma, subtração, divisão e multiplicação

# são operações usando os 4 comandos basicos de contas  + - / * respectivamente 

# então usando as variáveis de A e B para fazermos as opeçãoes seria assim

soma = A + B
subtracao = A - B
divisao = A / B
multiplicacao = A * B

print(soma, subtracao, divisao, multiplicacao)


mensagem = 'A rápida raposa marrom salta sobre o cachorro preguiçoso'
m1 = mensagem[:2]
m2 = mensagem[9:15]
m3 = mensagem[33:]
mensagem2 = m1 + m2 + m3
print(mensagem2)
print(m1)
print(m2)
print(m3)

for variavel in mensagem2:
    count = count + 1

print(count)
print("quantidade de caracteres na mensagem :" , count)


A = 'bom'
B = ' Dia'

C = A + B

print (C)

# operações intermediárias usando // ** % 

# onde // corresponde ao valos queé dividido porem se existe numero após a virgula esse numero n é contado

# ** é uma multiplicação exponencial , então o valor antes é o que corresponde ao numero que quer 
# fazer a exponencial e o segundo o valor que sera quantas vezes o numero se multiplicara

# % corresponde a divisões com resto, entao o numero que for dividido varias vezes por outro se tiver resto sera exibido 
# por essa operação

A = 37
B = 2

divisaoSemVirgula = A // B
multiplicacaoExpo = A ** B
divisaoComResto = A % B

print(divisaoSemVirgula,multiplicacaoExpo,divisaoComResto)

# condições = condições são absurdamente usadas para fazer comparações de todos os tipos, os mais primitivos
# são >  <  ==  !=
# que correspondem a maior menor, menor maior , igualdade , e diferente

A = 4
B = 3
C = 7

D = A > B 
E = A < B
F = A == C
G = A != C

# todas essas comdições tem como resutado valores de boolean, ou seja, 1 ou 0, true ou false

print(D, E, F, G)

# condições com respostas = naturalmente a resposta é dada como true e false mas se colocadas em uma estrutura
# de condição é possivel receber respota de todos os tipos, basta cumprir uma condição

# a estrutura ultilizada é o IF ELIF e ELSE
# if e a condição que inicia o a estutura podendo ou não só ter ela

# elif é a condição  que pode complementar ou não o If caso necessite de mais de uma condição 
# ou se a primeira condição não e você quer colocar em outra para fazer por exemplo mais de uma verificação

# else é o fim da condição, se todas acima não foram cumpridas, irá terminar nessa

# if elif e else podem abrigar todos os tipos de comparação possiveis, usando string numeros e variaveis


if(A > B):
    print('A é maior que B')



if(A < B):
    print('A é menor que B')
elif(A < C):
    print('A é menor que C')


if(A < B):
    print('A é menor que B')
else:
    print('nenhuma condição aprovada')

# para valores string a comparação pode ser feita de varias maneiras, usando o len() é possivel pegar 
# o valor do tipo int do tamanho da palavra e usar isso como comparação para determinadas operação
# no quisito de escrita o > < não se aplicam, porem o == e o != se aplicão a string

A = 'shampo'
B = 'batata'
C = 'batata'
 
if(A == B):
    print('shampo é igual a batata')
elif(B == C):
    print('batata é igual a batata')
else:
    print('nada é igual a nada')

# condições que tem como validação mais de uma requisição = validações que necessitam de mais de 1 condição
# são explicadas por  E e o OU , and e o or, podem ser um complemento pra uma validação seja ela qual for 
# para ficar mais completo, tem como resultado true ou false, valores boolean

if(A == B) and ( B == C):
    print('shampo é igual a batata')
elif(B == C) or (A == B):
    print('batata é igual a batata')


cond1 = (True and (True and not False)) and not (not False)
cond1 = not((not(not(not False)) and True))
cond3 = (not (2 != 4) and (3 < 6)) or True
cond4 = (2 > (2 < 3)) or not True
cond5 = ((True or True) or True ) and False

if cond1 :
    print('segunda feira')

if cond1 == True :
    print('terça feira')

    if cond3 :
        print('quarta feira')

if cond4 :
    print('quinta feira')
    
    if cond5 :
        print('sexta feira')
    

count =  0

# quando tratamos do and as 2 condições tem que ser verdadeiras para cumprir a requisição

# quando tratamos do or apenas uma das condições tem que ser verdadeira

# ambas podem ter mais de uma condição podendo a chegar a mais de 5 condições em 1 if para fazer determinada coisa

# em geral fazemos de tras pra frente para polparmos processamento, então começamos do errado para evitar o processamento 

# um exemplo simples para o de baixo

A = 30
B = 15
C = 2
D = 1


# suponhamos que essas são as resposta trazidas de uma váriavel que alocou esses valores

if(A == 0) and (B == 0) and (C == 0) and (D == 0):
    print('sem valores')
elif((A / C) == B) and (A == B):
    print('15 é igual a 15 e 15 é igual a 30')
elif((A /C) == B) and ((A * D) == A):
    print('15 é igual a 15 e 30 é igual a 30')

# em questão de achar problemas no sistema começar com a falha é o ideal por te pouca o processamento 
# desnecessario de algumas coisas

# for e for loops = for e foor loops sao condições de repetição que são usadas para repetir uma condição varias vezes 
# té conseguir o que se quer, ou até cumprir alguma outra condição

for i in range(0, 10):
    print(i)

# perceba que nesse codigo ele começa em 0 e vai até 9, ele mostra o 10 por convenção, a sintax esse codigo sempre é o
# valor maximo -1 ou seja, n ira mostrar até o numero que vc queira a menos que vc defina isso

for i in range(0, 20 + 2 , 2):
    print(i)

x = [[ j for j in range(5)] for i in range(10)]

print(x)

var = int(input('digite um numero: '))
x = [i for i in range(var + 2) if i % 2 == 0]

print(x)

# o parametro 2 que foi passado depois da virgula nesse caso é de quantos step em steps ele vai percorrer o tamanho definido
# ou seja ele começa no 0 vai até o valor 20 fazendo de 2 em 2, esses valores podem mudar obviamente e consequentemente 
# podendo começar ou terminar de varios modos

# pode ser resolvido com imputs tambem

numero = int(input('digite o numero do tamanho do for:'))
numero2 = int(input('dgite qual o valor do percurso do for:'))

for i in range(0, numero + numero2, numero2):
    print(i)

# usando variaveis de input é possivel fazer um pequeno programa para fazer a sequencia que vc quer 
# em um loop for


# while loop, o while assi como o for é uma estrutura de repetição, porem ela execulta 
# pelo menos 1 vez sempre e até ter uma condição de parada

loop = True
erros = 1

while loop:
    senha = input('password:')
    if (senha == 'mateus'):
        print('sucess')
        break
    elif(erros == 3):
        print('vc errou 3 vezes animal de teta')
        break
    else:
        print('senha errada')
        erros = erros + 1

# while assim como o for e tambem o if precisa que uma condição seja verdade para iniciar o loop
# e o loop só ira quebrar com o break se a condição onde estiver o break for saciada, é muito usado 
# verificação de senhas em geral, enquanto a senha n for verdadeira, o loop ira continuar

# Listas, tuplas = listas e tuplas sao variaveis que recebem uma sequencia de itens, a diferença de ambas é que
# a lsita é mutavel e a tupla nmão, muito simples

lista = ['macaco', 3, 47, 'primata']
tupla = ([3, 5, 'triangulo'], 4 , 1 , 'quadrado')

# uma lista pode conter todo tipo de tipo, confuso mas é essa a explicação, tipo no sentido de int 
# string e bool a tupla pode receber tambem e tambem ambas podem receber elas mesmas
# como listas dentro de listas e tuplas dentro de tuplas

print(type(lista[0]), type(lista[1]), type(lista[3]))
print(type(tupla[0]), type(tupla[1]), type(tupla[3]))

lista.append(1)
 
print(lista[4])
print(lista)

# podemos mudar elementos da lista assim como foi dito, mas de tuplas isso não funciona
# só é possivel mudar elementos da tupla que estão dentro de uma lista

tupla[0][1] = 4

print(tupla)

# elementos da tupla sem ser uma lista não sao modificaveis, ou seja, elementos string e numericos

# é possivel usar o tamanho da lista ou da tupla em uma estrutura for usando o tamanho da lista 
# os elementos dessa lista

for listas in (lista):  # in range(len(lista))
    print(listas)

# podemos tambem fazer comparaçoes dentro do for com elementos da lista para ver os elementos da lista 

for listas in lista:
    if listas == 'macaco':
        print(listas)
    elif listas == 'primata':
        print('orangotango')
    else:
        print('mico leao dourado')

print(lista)

# é possivel percorrer a lista baseandosse no tamanho dela, em certas ocasiões isso é muito util

for listas in range(len(lista)):
    if lista[listas] == 'macaco':
        print('macaco 1')
    elif lista[listas] == 'primata':
        print('macaco 3')
    else:
        print('macaco 2')

# string methods =  os metodos de string é manipulação da string em uma lista ou simplemente em
# uma variavel normal

palavra = input('digite uma palavra: ')

print(len(palavra))
print(palavra.lower())
print(palavra.upper())
print(palavra.strip())
print(palavra.split('.'))

# slice operator = em certas ocadiões é possivel particionar sua lista ou simplesmente 
# deparar palavras em string


frase = 'Eu amo python seloco ze, bao demai'
lista = ['tetris','moba','rpg','terror']

print(lista[1:])
print(frase[2::2])

lista[2:2] = 'mascaico'

print(lista)

# function - as funçoes no python sao definidas como Def e o nome da variavel, funções sao 
# um conjunto de linhas que tem como finalidade executar uma sequencia de comandos, e se quiser usalos
# novamente é só chamar o nome da variavel

def addtwo(z):
    return z + 2

def subtwo(x):
    return x - 2

print(addtwo(3))

# podemos tambem reaproveitar essas funções para usar repetidas vezes sem ter que fazer uma
# logica novamente, podendo poupar linhas do codigo e tambem deixalo mais nitido

def printnome(string):
    return print(string)

printnome('macaco')
printnome('avestruz')

# podemos ler arquivos de texto tambem sem uso de frameworks especificos

file = open('texto.txt', 'r')

f = file.readlines()

print(f)

# note que no final de cada palavra tem um \n, isso é uma caracteristica basica em programação que 
# significa quebra de linha, podemos remover essas quebras de linha lendo o arquivo e para cada linha remover 
# os ultimos 2 caracteres 

newlist = []

for lines in f:
    if lines[-1] == '\n':
        newlist.append(lines[:-1])
    else:
        newlist.append(lines)

print(newlist)


# podemos tambem escrever em um arqquivo de texto, assim como podemos ler ele, 
# tambem podemos excrever nele

file = open('texto2.txt', 'w')

file.write('gulira\n')
file.write('mucaco\nprimata')

file.close()

# podemos procurar e contar letras e numeros dentro de uma sequencia de caracteres em texto tambem

string = 'hello my name is vinicius from araraquara'

print(string.find('i'))
print(string.count('ci'))

# podemos usar uma estrutura de condição para descobrir se em algum lugar tem certas palavras 

palavra = input('digita algo ai: ')

if palavra.count('_') > 0:
    print('not good')
else:
    print('good')

# biblioteca math = a biblioteca math tem varias funcionalidade de matemática como numero de pi
# dar o radiente do numero, quantas casas depois da virgula, dentre outros

import math

print(math.degrees(math.pi))


# import function = dentro do mesmo diretorio podemos importar funções de outros arquivos 
# usando o comando import + nome do arquivo, e para chamar a função só usar o nome do 
# arquivo importado . nome da função

import function

print(function.myFuncSum(60))
print(function.myFuncSub(6))
print(function.myFuncMul(25))
print(function.myFuncDiv(25))


# Parametros opcionais - quando criamos uma função podemos passar parametros por ela, parametros esses
# que são pasados quando criamos uma variavel essa variavel ira chamar a função e passar o parametro por ele
# e então execultar a linha do código

def basicfunc(x = 3, text ='2'):
    print(x)
    if text == '1':
        print('text is 1')
    else:
        print(text)

basicfunc('5')

# try e execept = na tradução literal é tente e escessão, nesse caso try ele tenta fazer uma coisa
# se ele consegue acaba ali mesmo, se ele n funciona ou deu algo de errado, ele entra no except
# e execulta o que esta dentro do except

# basicamente uma if else mas no caso n é um sim e não ele vai tentar o sim e o não antes de dar 
# o não

text =  input('username: ')
try:
    number = int(text)
    print(number)
except:
    print('invalid username')

# variável global e local = variaveis globais são definidas foras do escopo de uma função
# e variaveis locais são aquelas que só podem ser chamadas dentro da função para execultar 
# um comando dentro dessa função

# a variável local n consegue ser vista de fora porem a global pode ser vista de todos os
# lugares, ou seja, é possivel usar variaveis globais dentro de uma função local com variaveis
# locais e as variaveis locais n podem ser usadas fora de seu escopo

var = 9
loop = True
newVar = 5

def func(x):
    newVar = 7

    if x == 5:
        return newVar

def newFunc(x):
    newVar = 8

    if x == 7:
        return newVar

print(newFunc(7), newVar)


# uma variavel criada dentro de uma função pode conter o mesmo nome de uma variavel global
# e como a variavel global pode entrar em uma função, ela tecnicamente mantem o valor da variavel
# global, ela só será alterada se uma linda de codigo for execultada dentro da função chamada
# "global"


var = True

def func2():
    global var

    var = 2

func2()
print(var)

# object e classes = os objetos se referencião ao tipo de variavel, como foi dito no começo 
# desse arquivo, atributos podem ser int, float, bool, e string, tres tipos distintos um dos outros
# e cada um desses objetos tem uma classe onde os métodos só podem funcionar nessas classes

# por exemplo, o objeto string possue metodos pra classes do tipo string que são .count. find . split
# dentre outros, cada objeto tem sua classe e seus metodos para se trabalhar com o tipo de variavel

x = 'string'
y = 23

print(type(x))
print(type(y))

class number():
    def __init__(self):
        self.var = 24   

    def display(self, x):
        print(x)


def get_largest_numbers(numbers, n):
    numbers.sort()

    return numbers[-n:]

nums = [2,3,4,1,34,123,321,1]

print(nums)
largest = get_largest_numbers(nums, 2)
print(nums)


# optional parameter - quando fazemos funções podemos passar parametros como base
# como tambem nenhum tipo de parametro, quando passamos um parametro é esperado que quando
# chamar essa função seja passado esse parametro, ou na criação da função, ele ja tenha
# o valor do parametro

def func1(word, add = 5,freq=1):
    print(word * (freq + add))

call = func1('hello',0)




class carro(object):
    def __init__(self, make, model , year, condition, kms):
        self.make = make
        self.model = model
        self.year = year
        self.condition = condition
        self.kms = kms

    def display(self, showall):
        if showall:
            print('this car is a %s %s from %s, it is %s and as %s kms.' %(self.make, self.model, self.year, self.condition, self.kms) )
        else:
            print('this car is a %s %s from %s' %(self.make, self.model, self.year))

whip = carro('ford', 'fusion', 2022, 'new', 0)
whip.display(True)

# static and class methods

class person(object):
    population = 50
    def __init__(self, name , age) :
        self.name = name
        self.age = age
    
    #class method
    def getPopulation(cls):
        return cls.population
    
    #static method
    def isAdult(age):
        return age >= 18
    
    def display(self):
        print(self.name, 'is', self.age ,'years old')   

newPerson = person('tin', 19)

print(person.getPopulation())



#map funcition

li = [1,2,3,4,5,6,7,8,9,10]

def func(x):
    return x**x

print (list(map(func,li)))
print([func(x) for x in li if x%2==0])