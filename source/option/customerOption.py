# Importa a função que limpa a tela
from source.actions.cleanAction import cleanScreem

# Importa as funções que exibe o cabeçalho e o menu principal do arquivo de menu principal
from source.menu.principalMenu import headerMenu, principal

# Importa as funções que exibe o menu principal do cliente, o menu de manutenção do cliente e o menu de relatório de cliente, do arquivo de menu do cliente
from source.menu.customerMenu import customerMenu, customerMaintenanceMenu, customerReportsMenu

# Importa as funções de cadastrar o cliente e atualizar seus dados, do arquivo de ações do cliente
from source.actions.customerActions import customerRegister, update, deleteCustomer

# Importa a função de relatório do arquivo de relatório de cliente
from source.reports.customerReports import allClientInformationReports, oneCustomerInformationReports, quantityCustomerReports

# De acordo com o número informado entra em uma das opções do menu do cliente
def chooseOptionMenuCustomer():
    optionCustomer = input('Digite a opção desejada: ')

    # Valida se apenas números foram digitados
    while not optionCustomer.isnumeric():
        print('Opção Inválida!')
        input('Pressione enter para continuar...')
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

        elif optionCustomer == 3:
            deleteCustomer()
            cleanScreem()
            headerMenu()
            customerMenu()
            chooseOptionMenuCustomer()

        # número 4 para entrar no menu de relatório de cliente
        elif optionCustomer == 4:
            cleanScreem()
            headerMenu()
            customerReportsMenu()
            chooseOptionReports()


# De acordo com o número informado entra em uma das opções do menu de manutenção do cliente
def chooseOptionMaintenance():
    optionMaintenance = input('Digite a opção desejada: ')

    # Valida se apenas números foram digitados
    while not optionMaintenance.isnumeric():
        print('Opção Inválida!')
        input('Pressione enter para continuar...')
        cleanScreem()
        headerMenu()
        customerMaintenanceMenu()
        optionMaintenance = input('Digite a opção desejada novamente: ')

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
            customerMaintenanceMenu()
            chooseOptionMaintenance()


# De acordo com o número informado entra em uma das opções do menu de relatório de cliente
def chooseOptionReports():
    optionReports = input('Digite a opção desejada: ')

    # Valida se apenas números foram digitados
    while not optionReports.isnumeric():
        print('Opção Inválida!')
        input('Pressione enter para continuar...')
        cleanScreem()
        headerMenu()
        customerReportsMenu()
        optionReports = input('Digite a opção desejada: ')

    optionReports = int(optionReports)

    while optionReports < 0 or optionReports > 3:
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

        # Número 1 exibe na tela o relatório de todos os clientes
        elif optionReports == 1:
            allClientInformationReports()
            cleanScreem()
            headerMenu()
            customerReportsMenu()
            chooseOptionReports()

        # Número 2 exibe na tela o relatório de um cliente
        elif optionReports == 2:
            oneCustomerInformationReports()
            cleanScreem()
            headerMenu()
            customerReportsMenu()
            chooseOptionReports()

        # Número 3 exibe na tela o relatório da quantidade de clientes cadastrados
        elif optionReports == 3:
            quantityCustomerReports()
            cleanScreem()
            headerMenu()
            customerReportsMenu()
            chooseOptionReports()