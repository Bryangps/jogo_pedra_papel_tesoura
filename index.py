import random
from time import sleep
import funcao

print('Regras do jogo :')

print('pedra VS papel -> papel vence\n'
      'pedra VS tesoura -> pedra vence\n'
      'papel VS tesoura -> tesoura vence\n')

while True:
    try:
        print('[1] - Rocha\n'
              '[2] - Papel\n'
              '[3] - Tesoura\n')

        opcao_usuario = int(input('Escolha uma das opções ? '))

        while opcao_usuario > 3 or opcao_usuario < 0:
            opcao_usuario = int(input('Escolha uma das opções ? '))

    except ValueError:
        print('Erro, valor informado não pode ser letra e campo não pode ficar vazio. Por favor tente novamente')
        continue

    except KeyboardInterrupt:
        print('\nVolte sempre')
        break

    else:
        if opcao_usuario == 1:
            usuario = 'Rocha'
        elif opcao_usuario == 2:
            usuario = 'Papel'
        elif opcao_usuario == 3:
            usuario = 'Tesoura'

        print('Agora é a vez do computador.....')
        sleep(2)
        escolha_computador = random.randint(1, 3)

        if escolha_computador == 1:
            computador = 'Rocha'
        elif escolha_computador == 2:
            computador = 'Papel'
        elif escolha_computador == 3:
            computador = 'Tesoura'

        funcao.exibir_enfeite(computador, usuario)

        funcao.imprir_resultado(computador, usuario)
    try:
        resp = input('Você quer jogar de novo (S ou N) ? ').casefold().strip()[0]
        while not resp in 'ns':
            resp = input('Informação invalida, digite (S ou N) ? ')

        if resp in 'Ss':
            continue
        else:
            break
    except KeyboardInterrupt:
        break
print()
print('Obrigado por jogar')
