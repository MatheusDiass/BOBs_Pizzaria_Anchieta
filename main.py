import os
from source.menu.principalMenu import principal, headermenu
from source.menu.customerMenu import customerMenu
#from source.db.tblCustomer import searchClient, clientcadastre


def main():

    opcao = 0

    headermenu()
    principal()

    opcao = eval(input('Escolha a opção desejada: '))

    while opcao < 1 or opcao > 4:
        print('Opção Inválida!')
        input('Pressione qualquer tecla para continuar...')
        main()
        break

    else:
        if opcao == 1:
            print(1)

        if opcao == 4:
            headermenu()
            customerMenu()

main()