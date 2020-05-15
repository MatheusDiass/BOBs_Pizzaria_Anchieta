import os
from source.menu.principal import principal, headermenu
from source.menu.client import clientmenu


def main():

    opcao = 0

    headermenu()
    principal()

    opcao = eval(input('Escolha a opção desejada: '))

    while(opcao >= 1 or opcao <= 4):
        if(opcao == 4):
            os.system('cls')
            headermenu()
            clientmenu()
            break

        else:
            os.system('cls')
            main()
            break

main()