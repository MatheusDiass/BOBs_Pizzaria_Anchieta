import os
from source.menu.principalMenu import principal, headerMenu
from source.menu.customerMenu import customerMenu, maintenanceMenu
from source.option.customerOption import chooseOptionMenuClient, chooseOptionMaintenance

def main():
    headerMenu()
    principal()

    opcao = int(input('Escolha a opção desejada: '))

    while opcao < 1 or opcao > 4:
        print('Opção Inválida!')
        input('Pressione qualquer tecla para continuar...')
        os.system('cls' if os.name == 'nt' else 'clear')
        main()
        #break

    else:
        if opcao == 1:
            print(1)

        if opcao == 4:
            headerMenu()
            customerMenu()
            chooseOptionMenuClient()


main()