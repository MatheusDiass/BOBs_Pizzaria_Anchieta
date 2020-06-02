# Importa a função que limpa a tela
from source.actions.cleanAction import cleanScreem

# Importa as funções que exibe o cabeçalho e o menu principal do arquivo de menu principal
from source.menu.principalMenu import headerMenu, principal

# Importa o arquivo que contém a função que realiza o pedido
from source.actions.OrderAction import request

# Importa as funções que exibe o menu principal do cliente, do arquivo de menu do cliente
from source.menu.customerMenu import customerMenu

# Importa a função que exibe o menu principal de pizza, do arquivo de menu de pizza
from source.menu.pizzaMenu import pizzaMenu

# Importa a função que realiza a escolha das opções do menu de cliente
from source.option.customerOption import chooseOptionMenuCustomer

# Importa a função que realiza a escolha das opções do menu de pizza
from source.option.pizzaOption import chooseOptionMenuPizza

from source.menu.orderMenu import orderMenu
from source.option.orderOption import chooseOptionOrderMenu

# De acordo com o número informado entra em uma das opções do menu principal
def chooseOptionMenuPrincipal():
    option = input('Digite a opção desejada: ')

    while not option.isnumeric():
        print('Opção Inválida!')
        input('Pressione enter para continuar...')
        cleanScreem()
        headerMenu()
        principal()
        option = input('Digite a opção desejada: ')

    option = int(option)

    while option < 1 or option > 4:
        print('Opção Inválida!')
        input('Pressione enter para continuar...')
        cleanScreem()
        headerMenu()
        principal()
        option = int(input('Digite a opção desejada: '))

    else:

        # Número 1 realiza o pedido
        if option == 1:
            request()
            cleanScreem()
            headerMenu()
            principal()
            chooseOptionMenuPrincipal()

        # Número 2 entra no menu de pedidos
        elif option == 2:
            cleanScreem()
            headerMenu()
            orderMenu()
            chooseOptionOrderMenu()

        # Número 3 entra no menu de pizza
        elif option == 3:
            cleanScreem()
            headerMenu()
            pizzaMenu()
            chooseOptionMenuPizza()

        # Número 4 volta ao menu de cliente
        elif option == 4:
            cleanScreem()
            headerMenu()
            customerMenu()
            chooseOptionMenuCustomer()