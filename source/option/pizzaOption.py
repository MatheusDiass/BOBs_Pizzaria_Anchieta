# Importa a função que limpa a tela
from source.actions.cleanAction import cleanScreem

# Importa as funções que exibe o cabeçalho e o menu principal do arquivo de menu principal
from source.menu.principalMenu import headerMenu, principal

# Importa as funções que exibe o menu principal de pizza, o menu de manutenção de pizza e o menu de relatório de pizza, do arquivo de menu de pizza
from source.menu.pizzaMenu import pizzaMenu, pizzaMaintenanceMenu, pizzaReportsMenu

# Importa as funções de cadastrar a pizza e atualizar seus dados, do arquivo de ações de pizza
from source.actions.pizzaActions import pizzaRegister, update, deactivatePizza

# Importa a função de relatório do arquivo de relatório de pizza
from source.reports.pizzaReports import allPizzaInformationReports, onePizzaInformationReports, allPizzaActiveReports, allPizzaInactiveReports, quantityPizzaReports

# De acordo com o número informado entra em uma das opções do menu de pizza
def chooseOptionMenuPizza():
    optionPizza = input('Digite a opção desejada: ')

    # Valida se apenas números foram digitados
    while not optionPizza.isnumeric():
        print('Opção Inválida!')
        input('Pressione enter para continuar...')
        cleanScreem()
        headerMenu()
        pizzaMenu()
        optionPizza = input('Digite a opção desejada: ')

    optionPizza = int(optionPizza)

    while optionPizza < 0 or optionPizza > 4:
        print('Opção Inválida!')
        input('Pressione enter para continuar...')
        cleanScreem()
        headerMenu()
        pizzaMenu()
        chooseOptionMenuPizza()

    else:

        # Número 0 volta ao menu principal
        if optionPizza == 0:
            # Importa a função que realiza a escolha das opções do menu principal
            from source.option.principalOption import chooseOptionMenuPrincipal
            cleanScreem()
            headerMenu()
            principal()
            chooseOptionMenuPrincipal()

        # Número 1 para cadastrar a pizza
        elif optionPizza == 1:
            pizzaRegister()
            cleanScreem()
            headerMenu()
            pizzaMenu()
            chooseOptionReportsPizza()

        # número 2 para entrar no menu de manutenção de pizza
        elif optionPizza == 2:
            cleanScreem()
            headerMenu()
            pizzaMaintenanceMenu()
            chooseOptionMaintenancePizza()

        elif optionPizza == 3:
            deactivatePizza()
            cleanScreem()
            headerMenu()
            pizzaMenu()
            chooseOptionMenuPizza()


        # número 4 para entrar no menu de relatório de pizza
        elif optionPizza == 4:
            cleanScreem()
            headerMenu()
            pizzaReportsMenu()
            chooseOptionReportsPizza()

# De acordo com o número informado entra em uma das opções do menu de manutenção de pizza
def chooseOptionMaintenancePizza():
    optionMaintenance = input('Digite a opção desejada: ')

    # Valida se apenas números foram digitados
    while not optionMaintenance.isnumeric():
        print('Opção Inválida!')
        input('Pressione enter para continuar...')
        cleanScreem()
        headerMenu()
        pizzaMaintenanceMenu()
        optionMaintenance = input('Digite a opção desejada: ')

    optionMaintenance = int(optionMaintenance)

    while optionMaintenance < 0 or optionMaintenance > 4:
        print('Opção Inválida!')
        input('Pressione enter para continuar...')
        cleanScreem()
        pizzaMaintenanceMenu()
        chooseOptionMaintenancePizza()

    else:

        # Número 0 volta ao menu principal de pizza
        if optionMaintenance == 0:
            cleanScreem()
            headerMenu()
            pizzaMenu()
            chooseOptionMenuPizza()

        # Os números de 1 á 4 são utilizados para atualizar alguma informação da pizza
        else:
            update(optionMaintenance)
            cleanScreem()
            headerMenu()
            pizzaMaintenanceMenu()
            chooseOptionMaintenancePizza()

# De acordo com o número informado entra em uma das opções do menu de relatório de pizza
def chooseOptionReportsPizza():
    optionReports = input('Digite a opção desejada: ')

    # Valida se apenas números foram digitados
    while not optionReports.isnumeric():
        print('Opção Inválida!')
        input('Pressione enter para continuar...')
        cleanScreem()
        headerMenu()
        pizzaReportsMenu()
        optionReports = input('Digite a opção desejada: ')

    optionReports = int(optionReports)

    while optionReports < 0 or optionReports > 5:
        print('Opção Inválida!')
        input('Pressione enter para continuar...')
        cleanScreem()
        pizzaReportsMenu()
        chooseOptionReportsPizza()

    else:

        # Número 0 volta ao menu principal de pizza
        if optionReports == 0:
            cleanScreem()
            headerMenu()
            pizzaMenu()
            chooseOptionMenuPizza()

        # Número 1 exibe na tela o relatório de todas as pizzas
        elif optionReports == 1:
            allPizzaInformationReports()
            cleanScreem()
            headerMenu()
            pizzaReportsMenu()
            chooseOptionReportsPizza()

        # Número 2 exibe na tela o relatório de uma pizza
        elif optionReports == 2:
            onePizzaInformationReports()
            cleanScreem()
            headerMenu()
            pizzaReportsMenu()
            chooseOptionReportsPizza()

        # Número 3 exibe na tela o relatório de todas as pizzas ativas
        elif optionReports == 3:
            allPizzaActiveReports()
            cleanScreem()
            headerMenu()
            pizzaReportsMenu()
            chooseOptionReportsPizza()

        # Número 4 exibe na tela o relatório de todas as pizzas inativas
        elif optionReports == 4:
            allPizzaInactiveReports()
            cleanScreem()
            headerMenu()
            pizzaReportsMenu()
            chooseOptionReportsPizza()

        # Número 5 exibe na tela o relatório da quantidade de pizzas cadastradas
        elif optionReports == 5:
            quantityPizzaReports()
            cleanScreem()
            headerMenu()
            pizzaReportsMenu()
            chooseOptionReportsPizza()