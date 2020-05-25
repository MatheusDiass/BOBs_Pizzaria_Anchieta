import os
from source.menu.principalMenu import principal, headerMenu
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
        main()
        break

    else:
        if option == 1:
            print(1)

        elif option == 3:
            headerMenu()
            pizzaMenu()
            chooseOptionMenuPizza()

        elif option == 4:
            headerMenu()
            customerMenu()
            chooseOptionMenuClient()


main()