# EXEMPLO DE MÓDULO CRIADO

import math

PI = math.pi


def dobra_lista(lista):
    return [x * 2 for x in lista]


def multiplica(lista):
    r = 1
    for i in lista:
        r *= i
    return r


# Se estiver sendo importado por outro módulo não executa
# Se estiver sendo importado por outro módulo não executa
if __name__ == '__main__':
    lista = [1, 2, 3, 4, 5]
    print(dobra_lista(lista))
    print(multiplica(lista))
    print(PI)
