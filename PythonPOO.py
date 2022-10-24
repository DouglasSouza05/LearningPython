from enum import Enum, auto
from dataclasses import dataclass
from dataclasses import field
from abc import ABC, abstractmethod
from contextlib import contextmanager
from datetime import datetime
from operator import index
from random import randint
from sqlite3 import dbapi2
from contextlib import contextmanager

# Programação Orientada a Objetos

# Classes

from statistics import variance
from textwrap import indent
from tkinter.font import names
from unittest import result
from xml.etree.ElementTree import C14NWriterTarget


class Pessoa:
    pass


# Recebem a mesma classe mas são dois Objetos diferentes. Possuem Endereços diferentes
p1 = Pessoa()
p2 = Pessoa()
print(p1)
print(p2)


class Pessoa:
    # def falar(self):
    #     print('Pessoa está falando!')

    # Pega o Ano atual OF OUR SOCIETY
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, nome, idade, falando=False, comendo=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

        variavel = 'valor'
        print(variavel)

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo!')
            return
        print(f'{self.nome} está comendo {alimento}!')
        self.comendo = True

    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo nada no momento.')
            return

        print(f'{self.nome} parou de comer!')
        self.comendo = False

    def falar(self, assunto):
        if self.comendo == False:
            if not self.falando:
                print(f'{self.nome} começou a falar sobre {assunto}!')
                self.falando = True
                return
            elif self.falando:
                print(f'{self.nome} ja está falando!')
                return

        print(f'{self.nome} está com a boca cheia.')
        self.falando = False

    def get_birth(self, year, birth):
        return year - birth

    def get_ano_nascimento(self, data):
        return self.ano_atual - data

    # Método de Classe -> Se refere a classe e não a Instancia
    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        # Variaveis sem 'self.' antes não poderão ser usadas fora da sua Classe
        # A variavel 'ano_atual' por ter sido criada na classe 'Pessoa' pode ser usado aqui
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

    # Método Static -> Não utiliza nem a Classe, nem a Instancia
    @staticmethod
    def gera_id():
        rand = randint(10000, 19999)
        return rand

# Class sem decorador -> É um método de Instância, por isso precisa receber o parâmetro 'self'
# Classmthod -> Variaveis Globais da Classe -> Precisa ser decorado e é referente a Classe
# Staticmethos -> Função normal, mas dentro do seu corpo não podemos usar 'self' nem 'cls'


p3 = Pessoa('Doug', 20, False, False)
print(p3.nome)
print(p3.idade)
print(p3.falando)
p3.comer('Abacaxi')
p3.comer('Laranja')
p3.parar_comer()
p3.falar('Codigos')
p3.falar('Magic')
p3.comer('Laranja')
p3.comer('Maça')
p3.falar('Dotin')
print(p3.get_birth(2022, 20))
print(p3.get_ano_nascimento(20))
p4 = Pessoa.por_ano_nascimento('Doug', 2002)
print(p4)
print(p4.nome, p4.idade)
print(Pessoa.gera_id())
# É possível criar mas não temos acesso a Instância dentro do método
print(p4.gera_id())

#####################################################################################

# Getters & Setters


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))

    # Getter
    @property
    def preco(self):
        return self._preco

    # Setter
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))
            self.preco = valor
            return

        self._preco = valor

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor.title().replace('a', '@')


p1 = Produto('Camiseta -', 50)
p1.desconto(10)
print(p1.nome, p1.preco)

p2 = Produto('Caneca -', 'R$15')
p2.desconto(10)
print(p2.nome, p2.preco)

# Encapsulamento

# _variavel -> Não recomendado usar fora da Classe ("Protected" -> na verdade publico)
# __variavel -> Recomenda fortemente não usar fora da Classe ("Private")


class DataBase:
    def __init__(self):
        self.__dados = {}

    @property
    def dados(self):
        return self.__dados

    def insert(self, id, nome):
        if 'Clientes' not in self.__dados:
            self.__dados['Clientes'] = {id: nome}
        else:
            self.__dados['Clientes'].update({id: nome})

    def list(self):
        for id, nome in self.__dados['Clientes'].items():
            print(id, nome)

    def delete(self, id):
        del self.__dados['Clientes'][id]


db = DataBase()
db.insert(1, 'Otávio')
db.insert(2, 'Maria')
db.insert(3, 'Rose')
db.delete(2)
db.list()
db.__dados = 'Outra coisa'
# print(db.__dados)
print(db._DataBase__dados)
# bd.list
print(db.dados)

#############################################################################################

# Associação -> Classes conectadas mas que podem existir individualmente (independentes)
# Cada Classe pode ser usada por uma ou outra Classe


class Escritor:
    def __init__(self, nome):
        self.__nome = nome  # Atributo privado
        self.__ferramenta = None

    @property
    def nome(self):
        return self.__nome

    @property
    def ferramenta(self):
        return self.__ferramenta

    @ferramenta.setter
    def ferramenta(self, obj):
        self.__ferramenta = obj


e1 = Escritor('Juanzito')
print(e1.nome)


class Caneta:
    def __init__(self, marca):
        self.__marca = marca

    @property
    def marca(self):
        return self.__marca

    def escrever(self):
        print('Caneta está escrevendo...')


class MaquinaDeEscrever:
    def escrever(self):
        print('Maquina está escrevendo...')


c1 = Caneta('Bic')
print(c1.marca)
m1 = MaquinaDeEscrever()

e1.ferramenta = c1
e1.ferramenta.escrever()
del e1
print(c1.marca)
m1.escrever

# Agregação -> Uma Classe precisa de outra Classe para funcionar corretamente
# A Classe existe individualmente mas não tem muita utilidade sem a outra


class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []

    def insert(self, obj):
        self.produtos.append(obj)

    def list(self):
        for prod in self.produtos:
            print(prod.nome, prod.valor)

    def somaTotal(self):
        total = 0  # Inicializando a variavel com 0 para impedir lixo
        for prod in self.produtos:
            total += prod.valor

        return total


class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor


p1 = Produto('Camiseta', 50)
p2 = Produto('Calça', 70)

c1 = CarrinhoDeCompras()
c1.insert(p1)
c1.insert(p2)
c1.list()
print(c1.somaTotal())

# Composição -> Uma Classe só Existe enquanto outra Classe existir
# Não faz sentido existir sem a outra. Uma pertende a outra


class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []

    def insert_enderecos(self, cidade, estado):
        self.enderecos.append(Endereco(cidade, estado))

    def list_enderecos(self):
        for x in self.enderecos:
            print(x.cidade, x.estado)

    # def __del__(self):
    #     print(f'{self.nome} WAS DELETED!!!')


class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado

    # def __del__(self):
    #     print(f'{self.cidade} {self.estado} WERE DELETED!!!')


c1 = Cliente('Doug', 20)
c2 = Cliente('DEUSO', 100000000)
print(c1.nome, c1.idade)
c1.insert_enderecos('Pouso Alegre -', 'MG')
c1.list_enderecos()
del c1
print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
print(c2.nome, c2.idade)
c2.insert_enderecos('Grand Society -', 'Heaven')
c2.list_enderecos()

############################################################################

# Herança Simples & Sobreposição de membros


class Pessoas:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print(f'{self.nomeclasse} está falando...')

 # Classe Funcionario e Aluno Herdam da Classe 'Pessoa'


class Funcionario(Pessoas):
    def comprar(self):
        print(f'{self.nomeclasse} está comprando...')

    def falar(self):
        print('Estou em Funcionario...')


# Herda da Classe Funcionario que herda da Classe Pessoa
class FuncionarioVIP(Funcionario):
    def falar(self):
        Pessoas.falar(self)  # Chama o método falar da Super Classe (Pessoa)
        super().falar()  # Pega o primeiro métdodo 'falar' acima desta Classe
        # Fazendo uma sobreposição
        print(f'O funcionario VIP estás a falar...')


class Aluno(Pessoas):
    def __init__(self, nome, idade, sobrenome):
        super().__init__(nome, idade)
        self.sobrenome = sobrenome

    def falar(self):
        Pessoas.falar(self)
        print(f'{self.nome} {self.sobrenome} está falando...')


f1 = Funcionario('Luiz', 25)
#a1 = Aluno('Roberto', 45)
print(f1.nome)
# print(a1.nome)
f1.comprar()
f2 = FuncionarioVIP('Rose', 22)
f2.falar()
a1 = Aluno('Doug', 20, 'KCaF')
a1.falar()

# Herança Multipla


class A:
    def falar(self):
        print('Estou em A!')


class B(A):
    def falar(self):
        print('Estou em B!')


class C(A):
    def falar(self):
        print('Estou em C!')


class D(B, C):
    pass


d = D()  # Pega primeiro da Esquerda (B)
d.falar()

# Classes Abstratas -> Método sem corpo. Utilizado para forçar as classes filhas a criarem esse método em
# seus escopos. No entando, com isso a Classe Abstrata não pode ser instanciada


# Força todas as classes filhas a terem o método 'Falar()'

class A(ABC):
    @abstractmethod
    def falar(self):
        pass


class B(A):
    def falar(self):
        print('B está Falando...')


b = B()
b.falar()


class Conta(ABC):  # Classe Abstrata
    def __init__(self, agencia, conta, saldo):
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo

    @property
    def agencia(self):
        return self._agencia

    @property
    def conta(self):
        return self._conta

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        # Chega se valor é uma isntância de Int ou Float
        if not isinstance(valor, (int, float)):
            raise ValueError('Saldo precisa ser numérico!!!')

        self._saldo = valor

    def depositar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('Valor do depósito precisa ser numérico!!!')

        self._saldo += valor
        self.detalhes()

    def detalhes(self):
        print(f'Agência: {self._agencia}', end=' ')
        print(f'Conta: {self._conta}', end=' ')
        print(f'Saldo: {self._saldo}')

    @abstractmethod  # Cada tipo de conta tem modos diferentes de saque por isso ela é abstrata
    def sacar(self, valor):
        pass


class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self.saldo < valor:
            print('Saldo Insuficiente!!!')
            return

        self.saldo -= valor
        self.detalhes()


class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite=100):
        super().__init__(agencia, conta, saldo)
        self._limite = limite

    @property
    def limite(self):
        return self._limite

    def sacar(self, valor):
        if (self.saldo + self.limite) < valor:
            print('Saldo Insuficiente!!!')
            return

        self.saldo -= valor
        self.detalhes()


cp = ContaPoupanca(1111, 2222, 0)
cp.depositar(10)
cp.sacar(5)
cp.sacar(6)
print('###############################')
cc = ContaCorrente(1111, 3333, 0, 500)
cc.depositar(100)
cc.sacar(250)
cc.sacar(350)
cc.sacar(1)

# Polimorfismo -> Permite que Classes derivados de uma mesma Superclasse tenham métdos iguais com
# comportamentos diferentes

########################################################################################################

# Criando Exceções personalizadas


class TudoEradoMeu(Exception):
    pass


def testar():
    raise TudoEradoMeu('Erado Pkaraio Meu!!!')


try:
    testar()
except TudoEradoMeu as erou:
    print(f'Erro: {erou}')

# Sobrecarga de Operadores

# Métodos mágicos -> __variavel__


class Retangulo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_area(self):
        return self.x * self.y

    # Vai representa o r3 (r1 + r2)
    def __repr__(self):
        return f"<class 'Retangulo({self.x}, {self.y})'>"

    # self -> instâcia. other -> outro objeto
    # Criando novo objeto da Classe
    # Vai representar o r1 + r2 (soma)
    def __add__(self, other):
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return Retangulo(novo_x, novo_y)

    # Vai funcionar como 'Less Than'
    def __lt__(self, other):
        a1 = self.get_area()
        a2 = other.get_area()

        if a1 < a2:
            return True
        else:
            return False

    # Vai funcionar como 'Greater Than'
    def __gt__(self, other):
        a1 = self.get_area()
        a2 = other.get_area()

        if a1 > a2:
            return True
        else:
            return False

    # Vai funcionar como 'Equal to'
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False


r1 = Retangulo(10, 20)
r2 = Retangulo(10, 20)
r3 = r1 + r2
print(r3 > r1)
print(r3 < r1)
print(r1 == r2)

# https://rszalski.github.io/magicmethods/ -> Documentação para Métodos mágicos


class A:
    def __new__(cls, *args, **kwargs):
        print('Eu sou o NEW')

        cls.nome = 'Doug'  # Atributo de Classe

        return super().__new__(cls)  # Toda Classe deriva de 'Object' (Primeira Class)
        # ou return object.__new__(cls)

    def __init__(self):  # Inicializador
        print('Eu sou o INIT')

    def __call__(self, *args, **kwargs):
        print(args)
        print(kwargs)

        resultado = 1

        for i in args:
            resultado *= i

        return resultado

    def __setattr__(self, key, value):
        if key == 'nome':
            # Intercepta 'a.nome' fazendo com que que seu valor seja 'Você não pode fazer isso!'
            self.__dict__[key] = 'Você não pode fazer isso!'
        else:
            self.__dict__[key] = value


a = A()
print(a.nome)
# Só é possível por causa do Método Mágico __call__ (usar a Classe como função)
resultado = a(1, 2, 3, 4, nome='Doug')
print(resultado)
a.nome = 'Doug'
print(a.nome)  # Funciona por causa do Método Mágico __setattr__

# Gerenciador de Contexto -> Context Manager. Necessário usa-lo com o 'with...'


class Arquivo:
    def __init__(self, arquivo, modo):
        print('abrindo arquivo')
        self.arquivo = open(arquivo, modo)

    def __enter__(self):
        print('retornando arquivo')
        return self.arquivo

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('fechando arquivo')
        self.arquivo.close()
        # Tratei a exceção
        return True


with Arquivo('abc.txt', 'w') as arquivo:
    arquivo.write('Writing...')

# Criando um Context Manager usando Função -> Algo mais simples


@contextmanager
def abrir(arquivo, modo):
    try:
        arquivo = open(arquivo, modo)
        yield arquivo  # Aqui 'yield' substitui 'return'
    finally:
        arquivo.close


with abrir('abc.txt', 'w') as arquivo:
    arquivo.write('Writing... now')

############################################################################

# Metaclasse -> Classes que criam outras Classes

# Type é uma Metaclasse
# mcs -> Metaclasse; names -> nome da classe criada; bases -> Classes pai das classes criadas


class Metaclasse(type):
    def __new__(msc, name, bases, namespace):
        if name == 'A':  # Classe A não terá comportamente diferente, só suas classes filhas
            return type.__new__(msc, name, bases, namespace)

        print(namespace)
        # Forçando a class B (filha de A) a ter o Método 'b_fala()'
        if 'b_fala' not in namespace:
            print(f'Ta errado! Precisa criar o método "b_fala()" em {name}.')
        else:
            # Verifica se "b_fala" é mesmo um Método e não uma variavel
            if not callable(namespace['b_fala']):
                print(
                    f'"b_fala" precisa ser um Método, não um atributo em {name}.')

        # Impede que uma classe Filha sobreescreva um atributo da classe Mãe, nesse caso 'attr_classe'
        if 'attr_classe' in namespace:
            print(f'{name} tentou sobreescrever o atributo!')
            del namespace['attr_classe']

        # Necessário retornar para criar as novas classes
        return type.__new__(msc, name, bases, namespace)


class A(metaclass=Metaclasse):
    def fala(self):
        self.b_fala()

    attr_classe = 'valor A'


class B(A):
    teste = 'valor'

    def sei_la():
        pass

    def b_fala():
        print('Oi!')

    attr_classe = 'valor B'


class C(B):
    attr_classe = 'valor C'


c = C()
print(c.attr_classe)

# Dataclasses -> É um modulo que fornece um decorador e funções para criar métodos automaticamente (como __init__)
# São Syntax Sugar para criar Classes normais. Não foi feito pensando muito e Herânça

# Documentação: https://docs.python.org/pt-br/3/library/dataclasses.html


# Uma Dataclasse que ja vem o __init__ criado automaticamente, entre outros...

# eq=False e repr=False desativa o Método Mágico '__eq__' & '__repr__'
@dataclass(eq=False, repr=True)
class Pessoa:
    nome: str  # String
    sobrenome: str = field(repr=False)  # Tira o sobrenome do Método '__repr__'

    def __post_init__(self):  # Método chamado depois do INIT
        self.nome_completo = f'{self.nome} {self.sobrenome}'

        # '__name__' transforma '<class 'int'> em int

        # if not isinstance(self.nome, str):
        #     raise TypeError(
        #         f'Tipo inválido {type(self.nome).__name__} != str em {self}')

    # def nome_completo(self):
    #     return f'{self.nome} {self.sobrenome}'


p1 = Pessoa('Doug', 'KCaF')
# Aparece certo por ser Dataclasse. Ao Desativar '__repr__' volta a mostrar Endereço
print(p1.nome_completo)
p2 = Pessoa('Doug', 'KCaF')
# Isso acontece pois o Método '__eq__' ja foi escrito por ser uma Dataclasse. (True se não desativar)
print(p1 == p2)
p3 = Pessoa(1234, 'O Brabo')
# Métodos como '__order__', '__frozen__', '__init__'

################################################################################################################

# ENUM -> docs.python.org/pt-br/3/library/enum.html
# Você tem um conjunto de coisas e não quer sair desse conjunta usa-se ENUM


class Directions(Enum):  # Vai ter as escolhas e vai verificar a Direction usando essa Classe
    right = auto()  # valor simbólico
    left = auto()
    up = auto()
    down = auto()


def move(direction):
    if not isinstance(direction, Directions):
        raise ValueError('Cannot move in this direction!')

    return f'Moving {direction.name}'  # Pega o nome (rigt left etc...)


if __name__ == '__main__':
    print(move(Directions.right))
    print(move(Directions.left))
    print(move(Directions.up))
    print(move(Directions.down))

    for direction in Directions:
        print(direction, direction.name, direction.value)

# Criando Listas. Implementando um Iterator


class MinhaLista:
    def __init__(self):
        self.__items = []
        self.__index = 0

    def add(self, valor):
        self.__items.append(valor)

    def __getitem__(self, index):  # Pegar itens usando indice
        return self.__items[index]

    def __setitem__(self, index, valor):
        if index >= len(self.__items):
            self.__items.append(valor)

        self.__items[index] = valor

    def __delitem__(self, index):
        del self.__items[index]

    def __iter__(self):  # Indica quem é o Iterador, nesse caso a própria Classe
        return self

    def __next__(self):  # Retorna o próximo elemento da Lista
        try:
            item = self.__items[self.__index]
            self.__index += 1
            return item
        # Impede que dê erro no for por falta de elementos (estouro do indice)
        except IndexError:
            raise StopIteration

    def __str__(self):
        return f'{self.__class__.__name__} ({self.__items})'

    def __repr__(self):
        return self.__str__

# Como é um Iterator, se não transformar em Lista ela pode ficar esgotada


if __name__ == '__main__':
    lista = MinhaLista()
    lista.add('Doug')
    lista.add('Juanzito')

    # Transformando em Lista mesmo para não esgotar o Iterator
    lista = list(lista)

    for valor in lista:
        print(valor)

    lista[0] = 'KCaF'

    print(lista[0])
    print(lista[1])
    lista[2] = 'Aobaaa'

    print(lista[2])
    del lista[2]
