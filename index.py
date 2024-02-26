import random

print('Regras do jogo :')

print('pedra VS papel -> papel vence\n'
      'pedra VS tesoura -> pedra vence\n'
      'papel VS tesoura -> tesoura vence\n')

lista_opcao = ['Rocha', 'Papel', 'Tesoura']

while True:
    lista_opcao = ['Rocha', 'Papel', 'Tesoura']
    computador = random.choice(lista_opcao)

    print('[1] - Rocha\n'
          '[2] - Papel\n'
          '[3] - Tesoura\n')

    opcao = input('Escolha uma das opções ? ')

    if opcao == 1:
        jogador = 'Rocha'
    elif opcao == 2:
        jogador = 'Papel'
    elif opcao == 3:
        jogador = 'Tesoura'

    resp = input('Você quer jogar de novo [S ou N] ? ').strip().casefold()[0]
    if resp in 'Nn':
        break
    elif resp in 'Ss':
        continue
    else:
        print('Informação invalida, digite [S ou N]')
