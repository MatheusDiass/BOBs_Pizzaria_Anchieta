# Importa a função de limpar tela
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
def chooseOptionMenuClient():
    optionClient = int(input('Digite a opção desejada:  '))

    while optionClient < 0 or optionClient > 4:
        print('Opção Inválida!')
        input('Pressione qualquer tecla para continuar...')
        cleanScreem()
        customerMenu()
        chooseOptionMenuClient()

    else:

        # Número 0 volta ao menu principal
        if optionClient == 0:
            # Importa o arquivo de opções do menu principal e a função que realiza a escolha
            from source.option.principalOption import chooseOptionMenuPrincipal
            cleanScreem()
            headerMenu()
            principal()
            chooseOptionMenuPrincipal()

        # Número 1 para cadastrar o cliente
        elif optionClient == 1:
            customerRegister()
            cleanScreem()
            headerMenu()
            customerMenu()
            chooseOptionMenuClient()

        # número 2 para entrar no menu de manutenção do cliente
        elif optionClient == 2:
            cleanScreem()
            headerMenu()
            customerMaintenanceMenu()
            chooseOptionMaintenance()
            cleanScreem()
            headerMenu()
            customerMenu()
            chooseOptionMenuClient()

        # número 4 para entrar no menu de relatório de cliente
        elif optionClient == 4:
            cleanScreem()
            headerMenu()
            customerReportsMenu()
            chooseOptionReports()
            input('Pressione o enter para continuar...')
            cleanScreem()
            headerMenu()
            customerMenu()
            chooseOptionMenuClient()

# De acordo com o número informado entra em uma das opções do menu de manutenção do cliente
def chooseOptionMaintenance():
    optionMaintenance = int(input('Digite a opção desejada:  '))

    while optionMaintenance < 0 or optionMaintenance > 9:
        print('Opção Inválida!')
        input('Pressione qualquer tecla para continuar...')
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
            chooseOptionMenuClient()

        # Os números de 1 á 9 são utilizados para atualizar alguma informação do cliente
        else:
            update(optionMaintenance)

# De acordo com o número informado entra em uma das opções do menu de relatório de cliente
def chooseOptionReports():
    optionReports = int(input('Digite a opção desejada:  '))

    while optionReports < 0 or optionReports > 1:
        print('Opção Inválida!')
        input('Pressione qualquer tecla para continuar...')
        cleanScreem()
        customerReportsMenu()
        chooseOptionReports()

    else:

        # Número 0 volta ao menu principal do cliente
        if optionReports == 0:
            cleanScreem()
            headerMenu()
            customerMenu()
            chooseOptionMenuClient()

        # Número 1 exibe na tela o relatório
        elif optionReports == 1:
            allClientInformationReports()