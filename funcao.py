from time import sleep


def imprir_resultado(computador, usuario):
    if computador == 'Rocha':
        if usuario == 'Tesoura':
            print(f'{computador} venceu =>  Vitória da maquina')
        elif usuario == 'Papel':
            print(f'{usuario} venceu =>  Vitória do usuário')
        else:
            print('Empate')
    elif computador == 'Papel':
        if usuario == 'Rocha':
            print(f'{computador} venceu =>  Vitória da maquina')
        elif usuario == 'Tesoura':
            print(f'{usuario} venceu =>  Vitória do usuário')
        else:
            print('Empate')
    elif computador == 'Tesoura':
        if usuario == 'Papel':
            print(f'{computador} venceu =>  Vitória da maquina')
        elif usuario == 'Rocha':
            print(f'{usuario} venceu =>  Vitória do usuário')
        else:
            print('Empate')


def exibir_enfeite(computador, usuario):
    print('-=' * 25)
    print('Pedra ! ', end='')
    sleep(1)
    print('Papel ! ', end='')
    sleep(1)
    print('Tesoura ....!')
    sleep(1)
    print('-=' * 25)
    print(f'{computador} VS {usuario}')


