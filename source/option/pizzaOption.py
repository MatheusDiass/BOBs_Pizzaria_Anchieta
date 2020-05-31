# Importa a função de limpar tela
from source.actions.cleanAction import cleanScreem

# Importa as funções que exibe o cabeçalho e o menu principal do arquivo de menu principal
from source.menu.principalMenu import headerMenu, principal

# Importa as funções que exibe o menu principal de pizza, o menu de manutenção de pizza e o menu de relatório de pizza, do arquivo de menu de pizza
from source.menu.pizzaMenu import pizzaMenu, pizzaMaintenanceMenu, pizzaReportsMenu

# Importa as funções de cadastrar a pizza e atualizar seus dados, do arquivo de ações de pizza
from source.actions.pizzaActions import pizzaRegister, update

# Importa a função de relatório do arquivo de relatório de pizza
from source.reports.pizzaReports import allPizzaInformationReports

# De acordo com o número informado entra em uma das opções do menu de pizza
def chooseOptionMenuPizza():
    optionPizza = int(input('Digite a opção desejada:  '))

    while optionPizza < 0 or optionPizza > 4:
        print('Opção Inválida!')
        input('Pressione qualquer tecla para continuar...')
        cleanScreem()
        pizzaMenu()
        chooseOptionMenuPizza()

    else:

        # Número 0 volta ao menu principal
        if optionPizza == 0:
            # Importa o arquivo de opções do menu principal e a função que realiza a escolha
            from source.option.principalOption import chooseOptionMenuPrincipal
            cleanScreem()
            headerMenu()
            principal()
            chooseOptionMenuPrincipal()

        # Número 1 para cadastrar a pizza
        elif optionPizza == 1:
            pizzaRegister()
            headerMenu()
            pizzaMenu()
            chooseOptionMenuPizza()

        # número 2 para entrar no menu de manutenção de pizza
        elif optionPizza == 2:
            cleanScreem()
            headerMenu()
            pizzaMaintenanceMenu()
            chooseOptionMaintenancePizza()

            # Após terminar, limpa a tela e exibe o menu de pizzas novamente
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
            input('Pressione o enter para continuar...')

            # Após terminar, limpa a tela e exibe o menu de pizzas novamente
            cleanScreem()
            headerMenu()
            pizzaMenu()
            chooseOptionMenuPizza()

# De acordo com o número informado entra em uma das opções do menu de manutenção de pizza
def chooseOptionMaintenancePizza():
    optionMaintenance = int(input('Digite a opção desejada:  '))

    while optionMaintenance < 0 or optionMaintenance > 4:
        print('Opção Inválida!')
        input('Pressione qualquer tecla para continuar...')
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

# De acordo com o número informado entra em uma das opções do menu de relatório de pizza
def chooseOptionReportsPizza():
    optionReports = int(input('Digite a opção desejada:  '))

    while optionReports < 0 or optionReports > 1:
        print('Opção Inválida!')
        input('Pressione qualquer tecla para continuar...')
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

        # Número 1 exibe na tela o relatório
        elif optionReports == 1:
            allPizzaInformationReports()

