import os
from source.menu.principalMenu import principal, headerMenu
from source.actions.requestAction import request
from source.menu.customerMenu import customerMenu
from source.menu.pizzaMenu import pizzaMenu
from source.option.customerOption import chooseOptionMenuClient
from source.option.pizzaOption import chooseOptionMenuPizza

def main():
    headerMenu()
    principal()

    option = int(input('Escolha a opção desejada: '))

    while option < 1 or option > 4:
        print('Opção Inválida!')
        input('Pressione qualquer tecla para continuar...')
        os.system('cls' if os.name == 'nt' else 'clear')
        headerMenu()
        principal()
        option = int(input('Escolha a opção desejada: '))

    else:
        if option == 1:
            request()

        elif option == 3:
            headerMenu()
            pizzaMenu()
            chooseOptionMenuPizza()

        elif option == 4:
            headerMenu()
            customerMenu()
            chooseOptionMenuClient()

main()