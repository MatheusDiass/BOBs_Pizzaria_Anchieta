from source.menu.principalMenu import headerMenu, principal
from source.menu.orderMenu import reportMenuOrder
from source.reports.orderReports import allOrderInformationReports

def chooseOptionOrderMenu():
    optionOrder = int(input('Digite a opção desejada:  '))

    while optionOrder < 0 or optionOrder > 2:
        print('Opção Inválida!')
        input('Pressione qualquer tecla para continuar...')
        os.system('cls' if os.name == 'nt' else 'clear')
        reportMenuOrder()
        chooseOptionOrderMenu()
        break

    else:

        if optionOrder == 0:
            headerMenu()
            principal()

        elif optionOrder == 2:
            reportMenuOrder()
            chooseOrderOptionReports()


def chooseOrderOptionReports():
    optionReports = int(input('Digite a opção desejada:  '))

    while optionReports < 0 or optionReports > 1:
        print('Opção Inválida!')
        input('Pressione qualquer tecla para continuar...')
        os.system('cls' if os.name == 'nt' else 'clear')
        reportMenuOrder()
        chooseOrderOptionReports()
        break

    else:

        # Número 0 volta ao menu principal do cliente
        if optionReports == 0:
            headerMenu()
            orderMenu()

        # Número 1 exibe na tela o relatório
        elif optionReports == 1:
            allOrderInformationReports()

        