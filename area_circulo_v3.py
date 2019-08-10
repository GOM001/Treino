#!/usr/local/bin/python3
from math import pi
import sys
import errno
print(__name__)


def circulo(raio):
    return pi * float(raio) ** 2


def help():
    print(f'''\
            É necessário informar o raio do circulo.
            Sixtaxe: {sys.argv[0]} <raio>''')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
        sys.exit(errno.EPERM)
        print('123456')
    else:
        raio = sys.argv[1]
        area = circulo(raio)
        print(f'Área da Circunferencia {area}')
        input('Enter para sair  ')
