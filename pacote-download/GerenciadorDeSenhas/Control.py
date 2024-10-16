import random
import string

import Moldel


def gerasenha():
    senha = ''
    for s in range(3):
        for i in range(8):
            aleatorio = random.randint(0, 2)
            if aleatorio == 0:
                numeros = random.randint(0, 9)
                senha += str(numeros)
            if aleatorio == 1:
                letras = random.choice(string.ascii_letters)
                senha += letras
            if aleatorio == 2:
                especial = random.choice('!@#$%^&*?.,')
                senha += especial
        if s < 2:
            senha += '-'
    Moldel.senhas.append(senha)
    return senha
