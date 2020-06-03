# Importa a função que limpa a tela
from source.actions.cleanAction import cleanScreem

# Importa as funções que exibe o cabeçalho e o menu principal do arquivo de menu principal
from source.menu.principalMenu import headerMenu, principal

# Importa função para deletar pedido
from source.actions.OrderAction import delete

# Importa as funções que exibe o menu principal de pedido e o menu de relatório de pedido, do arquivo de menu do pedido
from source.menu.orderMenu import orderMenu, reportMenuOrder

# Importa a função de relatório do arquivo de relatório de pedido
from source.reports.orderReports import allOrderInformationReports, allOrderBetweenDateReports

def chooseOptionOrderMenu():
    optionOrder = input('Digite a opção desejada: ')

    # Valida se apenas números foram digitados
    while not optionOrder.isnumeric():
        print('Opção Inválida!')
        input('Pressione enter para continuar...')
        cleanScreem()
        headerMenu()
        orderMenu()
        optionOrder = input('Digite a opção desejada: ')

    optionOrder = int(optionOrder)

    while optionOrder < 0 or optionOrder > 2:
        print('Opção Inválida!')
        input('Pressione enter para continuar...')
        cleanScreem()
        reportMenuOrder()
        chooseOptionOrderMenu()

    else:

        if optionOrder == 0:
            # Importa a função que realiza a escolha das opções do menu principal
            from source.option.principalOption import chooseOptionMenuPrincipal
            cleanScreem()
            headerMenu()
            principal()
            chooseOptionMenuPrincipal()

        elif optionOrder == 1:
            delete()
            cleanScreem()
            headerMenu()
            orderMenu()
            chooseOptionOrderMenu()

        elif optionOrder == 2:
            cleanScreem()
            headerMenu()
            reportMenuOrder()
            chooseOrderOptionReports()


def chooseOrderOptionReports():
    optionReports = input('Digite a opção desejada: ')

    # Valida se apenas números foram digitados
    while not optionReports.isnumeric():
        print('Opção Inválida!')
        input('Pressione enter para continuar...')
        cleanScreem()
        headerMenu()
        reportMenuOrder()
        optionReports = input('Digite a opção desejada: ')

    optionReports = int(optionReports)

    while optionReports < 0 or optionReports > 2:
        print('Opção Inválida!')
        input('Pressione enter para continuar...')
        cleanScreem()
        headerMenu()
        reportMenuOrder()
        chooseOrderOptionReports()

    else:

        # Número 0 volta ao menu principal do pedidos
        if optionReports == 0:
            cleanScreem()
            headerMenu()
            orderMenu()
            chooseOptionOrderMenu()

        # Número 1 exibe na tela o relatório de todos os pedidos
        elif optionReports == 1:
            allOrderInformationReports()
            cleanScreem()
            headerMenu()
            reportMenuOrder()
            chooseOrderOptionReports()

        # Número 2 exibe na tela o relatório de todos os pedidos de acordo com o periodo informado
        elif optionReports == 2:
            allOrderBetweenDateReports()
            cleanScreem()
            headerMenu()
            reportMenuOrder()
            chooseOrderOptionReports()