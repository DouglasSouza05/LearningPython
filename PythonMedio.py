import calculo  # Importando o módulo que eu criei (calculo.py)
from random import randint  # Fazendo isso não precisa colocar random.randint
import random
from calendar import c
from ctypes import Union
from random import randint
from re import L
import sys
from time import time, sleep
from itertools import permutations, product, zip_longest, count, combinations, groupby, tee
from types import GeneratorType
from functools import reduce
import math
import os
import json


def funcao(msg):
    print(msg)


funcao('Hello World!')


# Olá e Usuario sao valores padrões para caso não seja mandado anda ao chamar a função
def saudacao(msg='Olá', nome='Usuario'):
    nome = nome.replace('o', '8')  # Altera todos as letras 'o' por 8
    print(msg, nome)


saudacao()
saudacao(nome='Douglas')
saudacao('Hello', 'Doug')


def func(msg='Aoba'):
    return f'{msg}'  # Não passa pelos codigos que estão abaixo do return


variavel = func()
print(variavel)


def divisao(n1, n2):
    if n2 == 0:  # Caso seja True não roda o 'return n1 / n2'
        return

    return n1 / n2


divide = divisao(8, 0)

if divide:  # Caso de None (dividido por 0), ele não entra aqui
    print(divide)
else:
    print('Conta Inválida!')


def dumb():
    return [1, 2, 3]


print(dumb(), type(dumb()))


def tuplas():
    return ('Luiz', 'Otávio')


var = tuplas()

print(var, type(var))
print(var[1])

# Exercicio Proposto 3:


def calc(num, percent):
    return num + (num * (percent / 100))


result = calc(100, 50)
print(result)

# Exercicio Proposto 4:


def fb(n):
    if n % 3 == 0 and n % 5 == 0:
        return f'fizzbuzz, {n} e divisível por 3 e 5'
    if n % 5 == 0:
        return f'buzz, {n} é divisível por 5'
    if n % 3 == 0:
        return f'fizz, {n} é divisivel por 3'

    return n  # Caso não passe por nenhum if a função retorna 'n'


for i in range(10):
    random_num = randint(0, 100)
    print(fb(random_num))

lista = [1, 2, 3, 4, 5]
print(*lista)  # Desempacotamento de lista
print(*lista, sep='-')  # Separando por um '-'


def funcao(*args, **kwargs):
    # args = list(args)  # Transformando tuplas em lista
    # Não é possível mudar o valor armazenado em tupla, por isso é necessário transformar para lista
    # args[0] = 20
    # Não printa nome = 'Luiz' pois são argumentos nomeados -> para isso usa-se kwargs
    print(args)
    print(kwargs)
    print(kwargs['nick'])

    nick = kwargs.get('nick')
    print(nick)

    # idade = kwargs['idade'] -> Caso 'idade' não existir da erro
    idade = kwargs.get('idade')
    # usar .get quando não houver certeza que a variavel existe pois não da erro

    if idade is not None:
        print(idade)
    else:
        print('Idade não existe!')


lista = [1, 2, 3, 4, 5]
lista2 = [40, 50]
funcao(*lista, 10, 20, 30, *lista2, nome='Doug', nick='KCaF')

# global idade -> faz mudar o valor da variavel de nome 'idade' mesmo estando em um escopo local

variavel = 'valor'


def func(arg=None):
    arg = arg.replace('v', 'c')
    return arg


nova_variavel = func(arg=variavel)
print(variavel)
print(nova_variavel)

#######################################################################################################


def a(x, y): return x * y  # Faz o mesmo que uma função - Anônima


print(a(2, 2))

lista = [['P1', 13], ['P2', 6], ['P3', 50]]
print(lista)

lista.sort()  # Como são listas dentro de uma lista o Python não consegue interpretar sozinho como ordenar
print(lista)


def funcao(item):
    return item[1]  # Retorna um item com a chava que eu quero que ordene


# Passando a funcao que retorna o valor na posição 1 para "key". Como é lista.sort o Python entende
lista.sort(key=funcao)
# que é para pegar o valor de posição 1 de cada lista (preço - int) da lista e ordenar usando esse padrão
print(lista)

lista.sort(key=funcao, reverse=True)  # Inverte a ordem
print(lista)

# Faz o mesmo mas usando lambda e sem precisar criar uma função
lista.sort(key=lambda item: item[1])
print(lista)

# Mostra a lista ordenada usando o print diretamente
print(sorted(lista, key=lambda item: item[1]))

# A diferênça entre Tuplas e Listas é que não é possível editar os elementos de uma Tupla

t1 = (1, 2, 3, 'a')  # Tupla or t1 = 1, 2, 3, 'a'
# Para Tuplas com 1 elemento colocar virgula após o elemento. Exemplo: t1 = 1, or t1 = (1,)

print(t1, type(t1))

for v in t1:
    print(v)  # Imprimi cada valor da Tupla

print(t1[2:])  # Mostrando os valores da Tupla a partir do elemento '2'

t2 = 4, 5, 6, 'b'
t3 = t1 + t2
print(t3)  # Tuplas podem ser concatenadas

n1, n2, n3, n4, *resto = t3  # Tuplas podem ser descompactadas
print(n4)

t4 = (1, 2, 'Doug', 4, 5) * 2  # * 2 -> Faz repetir a Tupla 2 vezes
print(t4)
# Digitar t4[3] = 3 -> Da erro pois Tuplas não podem ser alteradas

t5 = (1, 2, 3, 4, 5)
t5 = list(t5)  # Transformo a Tupla em uma Lista
t5[2] = 3000
print(t5)
t5 = tuple(t5)  # Transformo Lista em Tupla
print(t5)

# Dicionarios

d1 = {'chave': 'valor da chave'}
print(d1)
d1['nova_chave'] = 'valor da nova chave'
print(d1)
print(d1['chave'])  # Mostra o valor que está associado a 'chave'

# Outra forma de criar um dicionario
d1 = dict(chave='valor da chave', chave_nova='valor da nova chave')
d1['chave3'] = 'valor da chave 3'
print(d1)
# Caso seja colocado indices de nomes iguais com valores diferentes, irá pegar o ultimo valor salvo
# Exemplo:
d1 = {'chave': 'chave1', 'chave': 'chave2',
      'chave': 'chave3'}  # Pega 'chave 3'
print(d1)

# É possível alterar o valor de uma chave em dicionarios usando d1['chave'] = 'chave 4' ou:
d1.update({'chave': 'chave4'})
print(d1)

# Deletando chaves de um dicionario
del d1['chave']  # or d1.pop('chave') or d1.pop.item() -> elemina o ultimo item
# É possivel concatenar dois dicionarios usando d1.update(d2) -> sendo d1 o dicionario que deseja incluir
# os valores de outro dicionario (d2)
print(d1)
# Verifica se a chave 'chave' existe no dicionario. Retorna True or False
print('chave' in d1)
d1 = {'DOTA': 'Brabo', 'LOL': 'Merda'}
print('DOTA' in d1.keys())  # Verifica se existe uma chave chamada 'DOTA' em d1
# Verifica se existe um valor chamado 'Brabo' em d1
print('Brabo' in d1.values())
print(len(d1))  # Mostra o tamanho, quantos 'pares'

for chave in d1:
    print(chave)  # Mostra as chaves do dicionario

for valor in d1.values():
    print(valor)  # Mostra os valores do dicionario

for tudo in d1.items():
    # Mostra as chaves e os valores. print(tudo[0], tudo[1]) -> Mostra sem as chaves
    print(tudo)

for k, v in d1.items():
    print(k, v)

# É possível colocar dicionarios em um dicionario

clientes = {
    'cliente1': {
        'nome': 'Luiz', 'sobrenome': 'Otávio'
    },
    'cliente2': {
        'nome': 'João', 'sobrenome': 'Moreira'
    }
}

for clientes_k, clientes_V in clientes.items():
    print(f'Exibindo {clientes_k}:')
    for dados_k, dados_v in clientes_V.items():
        print(f'\t{dados_k} = {dados_v}')

d1 = {1: 'a', 2: 'b', 3: 'c'}
v = d1  # Não está criando um novo dicionarios igual a d1 mas sim usando o mesmo dicionario

v[1] = 'Luiz'  # Muda o dicionario d1

print(d1)
print(v)

# Para poder mudar em v sem altera em d1 usar:
v = d1.copy()  # Não 'copia' realmente, cria-se referências
v[1] = 'Otávio'
print(d1)
print(v)

# Para uma lista dentro de um dicionario o d1.copy não funciona pois listas são mutaveis. Por isso é chamado
# de copia rasa or shallow copy
# Para realmente copiar um dicionario é necessário importar copy -> 'import copy' e usar o comando:
# v = copy.deepcopy(d1) -> copia funda or deep copy

# É possível transformar uma lista de listas ou uma lista de tuplas em dicionario usando d1 = dict(lista)

################################################################################################################

# Criandos Sets

# Parecido com dicionario mas não tem chave-valores e não tem indicies (Não da pra acessar)
# um valor especifico (somente iterando).
s1 = {1, 2, 3, 4, 5}
print(s1)
s2 = set()  # Criando um Set vazio
s2.add(1)
s2.add('Doug')
print(s2)
s2.discard(1)  # Eliminando o valor '1' do Set 2
print(s2)
s2.update('Python')  # Coloca letra por letra em ordem aleatória
# Só irá aparecer um '3' -> Não permite elementos iguais
s2.update([1, 2, 3], {3, 4, 5, 6})
print(s2)
# Sets são muito utilizados para tirar elementos repetidos de uma lista usando l1 = set(l1) e depois l1 = list(l1)
# Ao transformar set para lista os valores podem vir desorganizados

s1 = {1, 2, 3}
s2 = {1, 3, 4, 5}
s3 = s1 | s2  # Une dois Sets -> or union
print(s3)
s4 = s1 & s2  # Pega os valores iguais em ambos os Sets
print(s4)
s5 = s1 - s2  # Pega o elemento que está somente em s1
s6 = s2 - s1  # Pega o elemento que está somente em s2
print(s5)
print(s6)
s7 = s1 ^ s2  # Pega os elementos unicos de cada Set
print(s7)

# Comprehension em Python

l1 = [1, 2, 3, 4, 5]
ex1 = [variavel for variavel in l1]  # Igual a l1
print(ex1)
ex2 = [v * 2 for v in l1]  # Multiplicando cada elemento de l1 por 2
print(ex2)

# Crianco uma Tupla e colocando para cada elemento de v um valor de v2 in range(3), ou seja de 0 a 2
ex3 = [(v, v2) for v in l1 for v2 in range(3)]
print(ex3)

l2 = ['Luiz', 'Mauro', 'Maria']
# Para cada valor da lista, trocar 'a' por '@'  e colocando em maiusculo
ex4 = [v.replace('a', '@').upper() for v in l2]
print(ex4)

tupla = (
    ('chave', 'valor'), ('chave2', 'valor2')
)
ex5 = [(y, x) for (x, y) in tupla]  # troca as variaveis
print(ex5)

l3 = list(range(50))
# Pegando todos os valores pares entre 0 e 50
ex6 = [v for v in l3 if v % 2 == 0]
print(ex6)
# Pegando todos os valores divisiveis por 3 e 8 entre 0 e 50
ex7 = [v for v in l3 if v % 3 == 0 if v % 8 == 0]
print(ex7)

# Usando else
ex8 = [v if v % 3 == 0 and v % 8 == 0 else 0 for v in l3]
print(ex8)

# Comprehension de Dicionario

lista = [
    ('key', 'value'), ('key2', 'value2')
]

d1 = {x.upper(): y.upper() for x, y in lista}  # or d1 = dict(d1)
print(d1)

lista = [0, 1, 2, 3]
# Verifica se um objeto é iterave -> Return True or False
print(hasattr(lista, '__iter__'))
# Verifica se um objeto é um iterador -> Return True or False
print(hasattr(lista, '__next__'))

lista = iter(lista)  # Transforma uma lista iteravel em iterador
print(hasattr(lista, '__next__'))

# Geradores -> Usa se para otimizar o uso de memoria
lista = list(range(10))
print(sys.getsizeof(lista))  # Pega o quanto de memoria a lista esta ocupando


def gera():  # Gerador -> Retorna um valor de cada vez sem esperar que todos os outros estejam prontos
    for n in range(100):
        yield n
        # time.sleep(0.1)


g = gera()
for v in g:
    print(v)

print(type(g))  # Mostra o tipo dela, no caso um Gerador

print(hasattr(g, '__iter__'))
print(hasattr(g, '__next__'))

l1 = [x for x in range(1000)]  # -> Lista
print(type(l1))
print(sys.getsizeof(l1))
l2 = (x for x in range(1000))  # -> Gerador
print(type(l2))
print(sys.getsizeof(l2))  # O gerador usa bem menos memoria comparada a lista

# Lists, tuples, str -> Sequences -> Iteraveis

# Zip -> Unindo iteráveis; Zip_longest - Itertools

cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo']
estados = ['SP', 'MG', 'BA']

# Zip só une até a menor lista (Monte Belo não entra)
cidades_estados = zip(cidades, estados)
for x in cidades_estados:
    print(x[0], '-', x[1])

# Para que Monte Belo entre é necessário usar zip_longest (preenche com None)

# Zip só une até a menor lista (Monte Belo não entra)
cidades_estados = zip_longest(cidades, estados)
for x in cidades_estados:
    print(x[0], '-', x[1])

indice = count()

# Zip só une até a menor lista (Monte Belo não entra)
# fillvalue é usado para colocar alguma str por exemplo no lugar de 'None'
cidades_estados = zip_longest(cidades, estados, fillvalue='N/A')
for x in cidades_estados:
    print(x)

# Não usar indice = count() com zip_longest (lopp infinito)
cidades_estados = zip(indice, cidades, estados)
for x, y, z in cidades_estados:
    print(x, ':', y, '-', z)

variavel = zip('Alo', 'Alo')
# Verifica se 'variavel' é uma instancia de Gerador. True or False
print(isinstance(variavel, GeneratorType))
variavel = ((x, y) for x, y in zip('Alo', 'Alo'))
print(isinstance(variavel, GeneratorType))

###################################################################################

# Count -> Itertools

# Contador comeando em 10 e pulando de 5 em 5 (Para negativo só colocar -)
contador = count(start=10, step=5)
for v in contador:
    print(v)

    if v >= 100:
        break

# Combinações, Permutations e Product

# Para combinations a ordem não importa
pessoas = ['Luiz', 'André', 'Eduardo', 'Letícia', 'Rose']
for grupo in combinations(pessoas, 2):
    print(grupo)

# Ordem importa
pessoas = ['Luiz', 'André', 'Eduardo', 'Letícia', 'Rose']
for grupo in permutations(pessoas, 2):
    print(grupo)

# Permite por exemplo, Luiz e Luiz, André e André etc...
pessoas = ['Luiz', 'André', 'Eduardo', 'Letícia', 'Rose']
for grupo in product(pessoas, repeat=2):
    print(grupo)

# Agrupar eum varios Dicionarios -> groupby -> Dicionario precisa estar ordenado

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Doug', 'nota': 'A'},
    {'nome': 'Rose', 'nota': 'B'},
    {'nome': 'André', 'nota': 'C'},
]


def ordena(item): return item['nota']


alunos.sort(key=ordena)
for v in alunos:
    print(v)

alunos_agrupados = groupby(alunos, ordena)
# O FOR ABAIXO ESTÁ COMENTADO POIS COMO É UMA FUNÇÃO ITERADOR, ELE ESTÁ ESGOTANDO OS VALORES DA VARIAVEL ALUNOS
# AGRUPADOS, LOGO A OUTRA FUNÇÃO LOGO APÓS NÃO TINHA MAIS PARA MOSTRAR (NÃO ESTAVA ENTRANDO)
# for group, values in alunos_agrupados:
# Mostrando o agrupamento (no caso as notas)
#print(f'Agrupamento: {group}')
# for alunos in values:
# print(alunos)

for group, values in alunos_agrupados:
    va1, va2 = tee(values)  # FAZ DUAS COPIAS DO ITERADOR 'VALUES'
    # Mostrando o agrupamento (no caso as notas)
    print(f'Agrupamento: {group}')
    # Em 'alunos_agrupados' foi retornado um objeto pega groupby, por isso é necessários transforma-la em List
    # para usarmos a função len()
    # COMO ESSA FUNÇÃO É UM ITERADOR ELE ESGOTA TODOS OS VALORES POR ISSO NÃO É POSSÍVEL UTILIZAR OUTRO FOR COM ELA
    # RODA POIS FORAM CRIADAS DUAS COPIAS (va1 e va2) E SÓ A VA1 FOI ESGOTADA
    for aluno in va2:
        print(f'\t{aluno}')

    quantidade = len(list(va1))
    print(f'{quantidade} alunos tiraram nota: {group}')

    print()
    # NÃO RODA POIS OS VALORES DE VA1 FORAM ESGOTADAS
    for aluno in va1:
        print({aluno})

# Usando Map -> recebe uma função como primeiro argumento e retorna um iterador

lista = [1, 2, 4, 8]
# Para cada elemento da lista (x) -> Return x * 2
nova_lista = map(lambda x: x * 2, lista)
print(list(nova_lista))  # Passando Map para Lista

# Fazendo o mesmo que o Map (outra forma)
nova_lista_2 = [x * 2 for x in lista]
print(nova_lista_2)

produtos = [
    {'nome': 'p1', 'preco': 53},
    {'nome': 'p2', 'preco': 65},
    {'nome': 'p3', 'preco': 30.55},
    {'nome': 'p4', 'preco': 23.5}
]


def aumenta_preco(p):
    # 2 -> Duas casas decimais, 1.05 -> Aumentar o preço em 5 porcento
    p['preco'] = round(int(p['preco']) * 1.05, 2)
    return p


novos_produtos = map(aumenta_preco, produtos)

for produto in novos_produtos:
    print(produto)


# Filter -> Parecido com Map mas retorna True or False -> Retorna um iterator

# Os elementos maiores que 5 ficam, os que não saiem
nova_lista_3 = filter(lambda x: x > 5, lista)
print(list(nova_lista_3))

nova_lista_4 = [x for x in lista if x > 5]  # Outra forma
print(list(nova_lista_4))

produtos = [
    {'nome': 'p1', 'preco': 53},
    {'nome': 'p2', 'preco': 65},
    {'nome': 'p3', 'preco': 30.55},
    {'nome': 'p4', 'preco': 23.5}
]


def filtra(produto):
    if produto['preco'] > 50:
        return True


novos_produtos_2 = filter(lambda p: p['preco'] > 50, produtos)

for produto in novos_produtos_2:
    print(produto)

# Reduce -> função acumuladora (acumula valores)

# Para cada valor de i, pega esse valor, soma com ac e guarda em ac e repete o processo. Começa com ac = 0
soma_lista = reduce(lambda ac, i: i + ac, lista, 0)
print(soma_lista)  # 1 + 2 + 4 + 8 = 15

soma_precos = reduce(lambda ac, p: p['preco'] + ac, produtos, 0)
print(soma_precos)
print(round(soma_precos / len(produtos), 2))  # Média

# Try & Exceptions

# try:
#     print(numero)
# except:
#     print('Variavel não declarada!')  # Não é bom utilizar assim

# try:
#     print(numero)
# except Exception as e:  # Mostra qual é o erro
#     print(e)

numero = 5

try:
    print(numero)
except Exception as e:
    print(e)
else:
    print('BOA!')  # Executa sempre que o Try não sobre Exception (Error)
finally:
    print('End.')  # É sempre executada


def divide(n1, n2):
    try:
        return n1 / n2
    except Exception as e:
        print(f'log: {e}')
        raise  # Permite capturas a mesma Exception (relançar Exception)


try:
    print(divide(2, 1))
except Exception as e:
    print(e)

# Criando uma Exception
# Site para Exception Erros: https://docs.python.org/3/library/exceptions.html


def divide2(n1, n2):
    if n2 == 0:
        # Mostra uma Exception de Erro de Valor
        raise ValueError('O valor de "n2" não pode ser 0!')
    return n1 / n2


try:
    print(divide2(2, 0))
except ValueError as e:
    # Estaria mandando esse log para um Arquivo. Será mostrado em outra aula
    print(f'log: {e}')


def converte_numero(valor):
    try:
        valor = float(valor)
        return valor
    except ValueError as e:
        pass


# numero = converte_numero(input('Digite um número: '))
# if numero is not None:
#     print(numero * 5)
# else:
#     print('Entre com um valor válido!')

# 3

# Módulos -> São arquivos .py que servem para expandir as funcionalidads padrap da linguagem
# Módulos em: https://docs.python.org/3/py-modindex.html

print(sys.platform)
print(random.randint(0, 10))  # Imprimindo um numero entre 0 e 10

# De preferência usar somente "import random" e "random.randint" para não acabar sobreescrevendo eles
print(randint(0, 10))

PI = math.pi  # Variavel em Maiuscula indica que seu valor é constante e não muda

print(calculo.PI)
lista = [2, 4]
print(calculo.multiplica(lista))

# Formatando um valor para deixa-lo melhor visto

valor = 53.456


def real(valor):
    return f'R${valor:.2f}'.replace('.', ',')

# Quando um parâmetro é declarado = a algo, ao chamar a função não é necessário coloca-lo
# Só colocar o valor do parâmetro caso ele vá ser diferente daquele colocado como padrão


def aumento(valor, porcentagem, formata=False):
    r = valor + (valor * (porcentagem / 100))
    if formata:
        return real(r)
    else:
        return r


print(valor)
print(real(valor))
print(aumento(valor, 15))
print(aumento(valor, 15, True))

# Criando, Lendo e Escrevendo em Arquivos
# https://docs.python.org/3/library/functions.html#open

# w -> Write; w+ -> Read & Write; r -> read; a -> AppendMode
file = open('EstagioSoil.txt', 'w+')
file.write('Linha 1\n')
file.write('Linha 2\n')
file.write('Linha 3\n')
file.seek(0, 0)  # Voltando para a primeira posição
print('Lendo linhas:\n')
print(file.read())
print('###########')
file.seek(0, 0)
# Lê uma linha, movendo o cursos para o seu final
print(file.readline(), end='')
print(file.readline(), end='')  # Lê a proxima linha e etc...
# End é usado para não ter uma linha entre o que foi lido (\n)
print(file.readline(), end='')
print('###########')
file.seek(0, 0)
print(file.readlines())  # Retorna uma lista
print('###########')
file.seek(0, 0)
for linha in file.readlines():  # Ou somente 'linha in file'
    print(linha, end='')
file.close()

# Muitas vezes try e finally são usados ao abrir arquivos mas não são a melhor maneira Python

# Não é necessário fechar o arquivo usando With. Melhor maneira no Python
# 'w' não adicionada outras linhas. Apaga o que tem e coloca novas
with open('EstagioSoil.txt', 'w+') as file:
    file.write('Aoba,\n')
    file.write('Bao\n')
    file.write('D+++!\n')

    file.seek(0)
    print(file.read())

with open('EstagioSoil.txt', 'a+') as file:
    file.write('Agora\n')
    file.write('vai\n')

    file.seek(0)
    print(file.read())

# os.remove('EstagioSoil.txt') -> Apaga um arquivo

clientes = {
    'cliente1': {
        'nome': 'Luiz', 'sobrenome': 'Otávio'
    },
    'cliente2': {
        'nome': 'João', 'sobrenome': 'Moreira'
    }
}

# Transformando Dicionario em Json
clientes_json = json.dumps(clientes, indent=True)

with open('Clientes.json.txt', 'w+') as file:
    file.write(clientes_json)

# Transforma de volta para um Dicionario
clientes_json = json.loads(clientes_json)

# try:
#     import sys
#     import os
# except ImportError:
#     raise

# Função Decoradora & Decorador
#


def master(funcao):
    def slave(*args, **kwargs):
        print('Agora estou decorada!')
        funcao(*args, **kwargs)
    return slave


@master
def fala_oi():
    print('Oi.')


@master
def outra_funcao(msg):
    print(msg)


fala_oi()
outra_funcao('Aoba')


def velocidade(funcao):
    def interna(*args, **kwargs):
        start_time = time()
        resultado = funcao(*args, **kwargs)
        end_time = time()
        tempo = (end_time - start_time) * 1000  # Colocando em ms
        print(f'\nA função {funcao.__name__} '
              f'levou {tempo:.2f}ms para executar!')
        return resultado
    return interna


@velocidade
def demora():
    for i in range(10):
        print(i, end='')


# É como se fosse demora = velocidade(demora) que retorna 'interna' e então demora() que executa 'interna'
demora()

##############################################################################################

# lista = [] é uma lista vazia, padrão para caso não seja mandado nenhuma lista


def lista_de_clientes(clientes_iteravel, lista=[]):
    lista.extend(clientes_iteravel)
    return lista


lista1 = ['Fabricio']
clientes1 = lista_de_clientes(['João', 'Maria', 'Eduardo'])
clientes2 = lista_de_clientes(['Marcos', 'Jonas', 'Zico'], lista1)
# Mandando uma lista vazia para corrigir o Bug
clientes3 = lista_de_clientes(['Marcos', 'Jonas', 'Zico'], [])

# Por usar lista que é mutável, tanto clientes 1 quando clientes 2 mostram a mesma lista
print(clientes1)
print(clientes2)
print(clientes3)

# Mutáveis -> Lista, Dicionarios entre outros
# Imutáveis -> Tuplas, Strings, Números, True, False, None entre outros

# Enviando um atributo Imutável para corrigir o Bug


def lista_de_clientes(clientes_iteravel, lista=None):
    if lista is None:
        lista = []
    lista.extend(clientes_iteravel)
    return lista

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$