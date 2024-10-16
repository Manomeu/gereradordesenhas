import Control
import Moldel


def mostrar():
    print('=' * 30)
    print('Gerador de Senha:')

    quantidade = int(input('Quantas senhas deseja gerar?'))
    print()
    print('Aqui estão suas Senhas:')
    print('=' * 30)
    for i in range(quantidade):
        print(Control.gerasenha())
    print('=' * 30)


def senhas_armazenadas():
    verificar = input('Gostaria de ver as senhas armazenadas? [S/N]').upper()
    if verificar == 'S':
        print(Moldel.senhas)
    else:
        print('Até mais!')
