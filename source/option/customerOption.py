# Importa a função que limpa a tela
from source.actions.cleanAction import cleanScreem

# Importa as funções que exibe o cabeçalho e o menu principal do arquivo de menu principal
from source.menu.principalMenu import headerMenu, principal

# Importa as funções que exibe o menu principal do cliente, o menu de manutenção do cliente e o menu de relatório de cliente, do arquivo de menu do cliente
from source.menu.customerMenu import customerMenu, customerMaintenanceMenu, customerReportsMenu

# Importa as funções de cadastrar o cliente e atualizar seus dados, do arquivo de ações do cliente
from source.actions.customerActions import customerRegister, update

# Importa a função de relatório do arquivo de relatório de cliente
from source.reports.customerReports import allClientInformationReports


# De acordo com o número informado entra em uma das opções do menu do cliente
def chooseOptionMenuCustomer():
    optionCustomer = input('Digite a opção desejada:  ')

    while not optionCustomer.isnumeric():
        print('Opção Inválida!')
        input('Pressione qualquer tecla para continuar...')
        cleanScreem()
        headerMenu()
        customerMenu()
        optionCustomer = input('Digite a opção desejada: ')

    optionCustomer = int(optionCustomer)

    while optionCustomer < 0 or optionCustomer > 4:
        print('Opção Inválida!')
        input('Pressione enter para continuar...')
        cleanScreem()
        headerMenu()
        customerMenu()
        chooseOptionMenuCustomer()

    else:

        # Número 0 volta ao menu principal
        if optionCustomer == 0:
            # Importa a função que realiza a escolha das opções do menu principal
            from source.option.principalOption import chooseOptionMenuPrincipal
            cleanScreem()
            headerMenu()
            principal()
            chooseOptionMenuPrincipal()


        # Número 1 para cadastrar o cliente
        elif optionCustomer == 1:
            customerRegister()
            cleanScreem()
            headerMenu()
            customerMenu()
            chooseOptionMenuCustomer()

        # número 2 para entrar no menu de manutenção do cliente
        elif optionCustomer == 2:
            cleanScreem()
            headerMenu()
            customerMaintenanceMenu()
            chooseOptionMaintenance()

        # número 4 para entrar no menu de relatório de cliente
        elif optionCustomer == 4:
            cleanScreem()
            headerMenu()
            customerReportsMenu()
            chooseOptionReports()


# De acordo com o número informado entra em uma das opções do menu de manutenção do cliente
def chooseOptionMaintenance():
    optionMaintenance = input('Digite a opção desejada:  ')

    while not optionMaintenance.isnumeric():
        print('Opção Inválida!')
        input('Pressione qualquer tecla para continuar...')
        cleanScreem()
        headerMenu()
        customerMaintenanceMenu()
        optionMaintenance = input('Digite a opção desejada: ')

    optionMaintenance = int(optionMaintenance)

    while optionMaintenance < 0 or optionMaintenance > 9:
        print('Opção Inválida!')
        input('Pressione enter para continuar...')
        cleanScreem()
        headerMenu()
        customerMaintenanceMenu()
        chooseOptionMaintenance()

    else:

        # Número 0 volta ao menu principal do cliente
        if optionMaintenance == 0:
            cleanScreem()
            headerMenu()
            customerMenu()
            chooseOptionMenuCustomer()

        # Os números de 1 á 9 são utilizados para atualizar alguma informação do cliente
        else:
            update(optionMaintenance)
            cleanScreem()
            headerMenu()
            customerMenu()
            chooseOptionMenuCustomer()


# De acordo com o número informado entra em uma das opções do menu de relatório de cliente
def chooseOptionReports():
    optionReports = input('Digite a opção desejada:  ')

    while not optionReports.isnumeric():
        print('Opção Inválida!')
        input('Pressione qualquer tecla para continuar...')
        cleanScreem()
        headerMenu()
        customerReportsMenu()
        optionReports = input('Digite a opção desejada: ')

    optionReports = int(optionReports)

    while optionReports < 0 or optionReports > 1:
        print('Opção Inválida!')
        input('Pressione enter para continuar...')
        cleanScreem()
        headerMenu()
        customerReportsMenu()
        chooseOptionReports()

    else:

        # Número 0 volta ao menu principal do cliente
        if optionReports == 0:
            cleanScreem()
            headerMenu()
            customerMenu()
            chooseOptionMenuCustomer()

        # Número 1 exibe na tela o relatório
        elif optionReports == 1:
            allClientInformationReports()
            input('Pressione enter para continuar...')
            cleanScreem()
            headerMenu()
            customerMenu()
            chooseOptionMenuCustomer()
