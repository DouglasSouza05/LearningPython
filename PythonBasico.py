print('Aulas', 'Python \n')
print('Douglas', 'Souza', sep='-', end='###')
print('1730')
print(type('Douglas'))  # Type - Retorna o tipo da variavel
print(10, type(10))
print('Douglas' + ' Souza')
# * -> Pode ser usado para repetir Str
# // -> Divisão com arredondamento
# ** -> Potenciaçao
# % -> Resto
nome = 'Douglas'
print(f'{nome}')  # Print de forma formatada
# varivel:.2f -> usado para mostrar um valor com 2 casas decimais (nesse caso float (f))
print('{}'.format(nome))
# usar print('{0}'.format(nome)) para quando precicar repetir ou
# print('{n}'.format(n=nome))
# idade = input('Qual sua idade?') - Comentando para evitar colocar toda vez
# Mesmo colocando int, a variavel salva e str, por isso usar casting
idade = 20
birth_year = 2022 - int(idade)
print(f'{nome} tem {idade} anos, logo nasceu em {birth_year}')
if int(idade) > 18:
    print('true')
elif int(idade) < 18:
    print('false')
else:
    print('18tão')
n1 = 10
n2 = 3
iguais = (n1 == n2)
print(iguais)  # Verifica através da variavel iguais se n1 é igual a n2
# and = &&; or = |; not = !
a = 'l'  # ou a = 0
if not a:
    print('Por favor, preencha o valor de a!')
else:
    print('Variavel a Preenchido')

if 'D' in nome:
    print(f'O nome {nome} tem a letra D')
# not in = in invertido
# quantidade de caracteres - é possivel somar len(variavel) com outra
tamanho_nome = len(nome)
# Documentação Python -> https://docs.python.org/3/library/stdtypes.html

#########################################################################################

# Para futuramente colocar algum codigo usar pass ou ... para não dar IndentaionError

divisao = n1 / n2
print('{d:.2f}'.format(d=divisao))
# float -> f; str -> s; int -> d
# Colocando cerquilhas a esquerda e direita do nome (ao centro)
print(f'{nome:#^20}')
print(f'{n1:0>10}')  # n1 com 0 a esquerda resultando em 10 casas decimais
print(f'{n1:0<10}')  # n1 com 0 a direita resultando em 10 casas decimais
print(f'{n1:2^10}')  # n1 com 2 ao centro resultando em 10 casas decimais
# Formatando nome com @ a esquerda resultando em 10 casas
nome_formatado = f'{nome:@>10}'
print(nome_formatado)
# Completa os caracteres restantes com '#' (max = 10)
nome = nome.ljust(10, '#')
print(nome)
nome = 'douglas'
print(nome.lower())  # Minusculo
print(nome.upper())  # Maisculo
print(nome.title())  # Primeiras letras maiusculas
print(nome[3])  # Acessando o indice 3
print(nome[2:5])  # Pegando os indices 2, 3 e 4 (5 não incluido)
# [:5] -> indice 0 ao 4
# [5:] -> indice 5 ao final
print(nome[-1])  # Usando indices negativos -> -1 equivale ao ultimo (s)
# Pegando os indices de 0 e 6 pulando de 1 em 1 - pega todos que der
print(nome[0::2])
# Pegando os indices de 0 a 6 pulando de 2 em 2 -> tem limite
print(nome[0:6:2])
for letra in nome:
    print(letra)  # Printa cada letra na vertical

#########################################################################################

x = 0
while x <= 60:
    if x >= 30:
        print(x)
        x += 3
        # Pula o restante do codigo e vai para o próximo loop (roda somente o que esta acima)
        continue
    print(x)
    x += 1
else:
    # Comandos como break dados no while não fazem passar pelo else
    print('Cheguei no Else.')
# Break -> Finaliza o loop

frase = 'o rato roeu a roupa do rei de roma'  # Iterável
tamanho_frase = len(frase)
contador = 0
nova_string = ''

# Iteração <- Iterar (percorrer cada um dos elementos)
while contador < tamanho_frase:
    nova_string += frase[contador]  # Contatenando com cada indice de 'frase'
    contador += 1
    print(nova_string)

nome = 'Souza'
# Pegando cada letra do texto e numero (ela enumera começando em 0)
for i, letra in enumerate(nome):
    print(letra)

for num in range(5, 10, 1):
    print(num)

for n in range(41):  # Imprindo os valores multiplos de 8
    if n % 8 == 0:
        print(n)

###############################################################################

lista = ['A', 'Bacana', 'C', 10.5]
print(lista[1])
print(lista[2])
print(lista[-1])  # print(lsita[3])
lista[2] = 'Nice'
print(lista[2])
print(lista[1:4])  # Listas também podem ser fatiadas
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = l1 + l2
print(l1)
print(l3)
l2.extend(l1)  # Adiciona os valores da lista 1 na própria lista 2 sem ordenar
print(l2)
l3.append('bão')  # Insere um valor no final da lista
print(l3)
l3.insert(0, 'first')  # Insere um valor em um indice especifico
print(l3)
l4 = [7, 8, 9]
print(l4)
l4.pop()
print(l4)  # Apaga o ultimo elemento da lista
l5 = [10, 11, 12, 13, 14]
print(l5)
del (l5[1:3])  # Apagando os elementos de indice 1 e 2
print(l5)
print(max(l5))  # Pegando o maior valor da lista 5
print(min(l5))  # Pegando o menor valor da lista 5
l6 = range(1, 10)
print(l6)  # Função range não retorna lista e sim um objeto - Para isso usar função list
l6 = list(range(1, 10))  # List transforma objetos iteráveis em lista
print(l6)
l7 = list(range(0, 100, 20))
for valor in l7:
    print(valor)

secreta = 'perfume'
digitadas = []
chances = 5

while True:
    break  # Colocando break para não ficar pedindo toda vez
    if chances <= 0:
        print('Você perdeu!')
        break

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Coloca somente uma letra!')
        continue
    elif len(letra) < 1:
        print('Coleque uma letra!')
        continue

    digitadas.append(letra)

    if letra in secreta:
        print(f'Boa, a letra {letra} existe na palavra secreta.')
    else:
        print(f'A letra {letra} não existe na palavra secreta.')
        digitadas.pop()
        chances -= 1
        if chances > 1:
            print(f'Você ainda tem {chances} chances.')

    secreto_temp = ''
    for letra_secreta in secreta:
        if letra_secreta in digitadas:
            secreto_temp += letra_secreta
        else:
            secreto_temp += '*'

    if secreto_temp == secreta:
        print(f'Boa, você VENCEU!!! A palavra secreta era: {secreto_temp}')
        break
    else:
        print(f'A palavra secreta está assm: {secreto_temp}')

#####################################################################################

variavel = ['Luiz Otávio', 'Joãozinho', 'Maria']

for valor in variavel:
    if valor.lower().startswith('J'):  # Pega o valor, converte para minusculo e verifica se é igual a 'J'
        print('Começa com J: ', valor)
    else:
        print('Não começa com J: ', valor)

string = 'O Brasil é o país do futebol, o Hexa vem!'
lista = string.split(' ')  # Separa a string em partes que tem espaço
lista2 = string.split(',')  # Separa a string em partes que tem vírgula
print(lista)
print(lista2)

for valor in lista2:
    print(f'A palavra {valor} apareceu {lista2.count(valor)}x na frase!')

for valor in lista2:
    # .strip() -> retira os espaços do inicio e fim da string; .capitaliza() -> deixa o primeiro caractere maiusculo
    print(valor.strip().capitalize())

 # join -> transforma uma lista em string
string = 'O Brasil é o país do futebol, o Hexa vem!'
lista = string.split(' ')
string2 = ','.join(lista)  # junta a lista através da ','
string3 = ' '.join(lista)

print(string)
print(lista)
print(string2)
print(string3)

# enumerate -> pega o indice e o valor desse indice de uma lista
for indice, valor in enumerate(lista):
    print(indice, lista[indice])  # Valor = lista[indice]

# Colocando uma lista em uma lista
lista4 = [[0, 'Luiz'], [1, 'João'], [2, 'Maria']]

for valor in lista4:
    break
    print(valor)
    print(valor[0])  # Pegando o valor de indice 0 de cada valor da lista
    print(valor[0], valor[1])

for indice, nome in lista4:
    print(indice, nome)

lista5 = ['Luiz', 'João', 'Maria']

# Faz o mesmo que o de cime, de forma mais eficiente
for indice, nome in enumerate(lista5):
    print(indice, nome)

# Trocando valor entre variaveis
x = 10  # Receberá 'Eu'
y = 'Luiz'  # Receberá '10'
z = 'Eu'  # Receberá 'Luiz'

x, y, z = z, x, y

print(f'x={x}; y={y} e z={z}')

# Desempacotamente de lista em Python
lista = ['Luiz', 'João', 'Maria', 1, 2, 3, 4, 100]

# n1, n2 = lista -> Da erro por que lista tem muito mais elementos que 2
# Não da erro. *outra_lista -> gera uma lista que recebe os valores restantes
n1, n2, *outra_lista, ultimo_lista = lista

print(n1, n2, outra_lista, ultimo_lista)

##############################################################################################################################

# Operação ternária em Python
logged_user = False
# Ou 'if logged_user == True'
msg = 'Usuario logado.' if logged_user else 'Usuário precisa logar.'

print(msg)

idade = 19
maior = (idade >= 18)  # Verifica e retorna True or False para 'maior'
msg = 'Pode acessar.' if maior else 'Não pode acessar!'

print(msg)

# Expressões condicionais com Operador OR
#nome = input('Qual o seu nome? ')
# Se não houver nada em 'nome' (Vazio) printa 'Você não digitou nada!'
print(nome or 'Você não digitou nada!')
print(nome or None or False or 0 or 'Você não digitou nada' or 'Outra coisa')

a = 0
b = None
c = False
d = []
e = {}
f = 22
g = 'Luiz'

variavel = a or b or c or d or e or f or g
print(variavel)

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
