import os
from source.menu.customerMenu import customerMenu

# Pizzaria Name - Header
def headerMenu():
    print('*' * 18)
    print('* BOB`s Pizzaria *')
    print('*' * 18)

# Principal Menu
def principal():
    #optionPrincipal = 0

    print('\nMenu Principal\n')
    print('[1] - Realizar Pedido')
    print('[2] - Pedidos')
    print('[3] - Pizzas')
    print('[4] - Clientes')

    '''optionPrincipal = int(input('Escolha a opção desejada: '))

    while optionPrincipal < 1 or optionPrincipal > 4:
        print('Opção Inválida!')
        input('Pressione qualquer tecla para continuar...')
        os.system('cls' if os.name == 'nt' else 'clear')
        break

    else:
        if optionPrincipal == 1:
            print(1)

        if optionPrincipal == 4:
            headerMenu()
            customerMenu()'''