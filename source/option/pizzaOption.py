import os
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
        os.system('cls' if os.name == 'nt' else 'clear')
        pizzaMenu()
        chooseOptionMenuPizza()
        break

    else:

        # Número 0 volta ao menu principal
        if optionPizza == 0:
            headerMenu()
            principal()

        # Número 1 para cadastrar a pizza
        elif optionPizza == 1:
            pizzaRegister()
            headerMenu()

        # número 2 para entrar no menu de manutenção de pizza
        elif optionPizza == 2:
            pizzaMaintenanceMenu()
            chooseOptionMaintenancePizza()

        # número 4 para entrar no menu de relatório de pizza
        elif optionPizza == 4:
            headerMenu()
            pizzaReportsMenu()
            chooseOptionReportsPizza()

# De acordo com o número informado entra em uma das opções do menu de manutenção de pizza
def chooseOptionMaintenancePizza():
    optionMaintenance = int(input('Digite a opção desejada:  '))

    while optionMaintenance < 0 or optionMaintenance > 4:
        print('Opção Inválida!')
        input('Pressione qualquer tecla para continuar...')
        os.system('cls' if os.name == 'nt' else 'clear')
        pizzaMaintenanceMenu()
        chooseOptionMaintenancePizza()
        break

    else:

        # Número 0 volta ao menu principal de pizza
        if optionMaintenance == 0:
            headerMenu()
            pizzaMenu()

        # Os números de 1 á 4 são utilizados para atualizar alguma informação da pizza
        else:
            update(optionMaintenance)
            headerMenu()
            pizzaMenu()

# De acordo com o número informado entra em uma das opções do menu de relatório de pizza
def chooseOptionReportsPizza():
    optionReports = int(input('Digite a opção desejada:  '))

    while optionReports < 0 or optionReports > 1:
        print('Opção Inválida!')
        input('Pressione qualquer tecla para continuar...')
        os.system('cls' if os.name == 'nt' else 'clear')
        pizzaReportsMenu()
        chooseOptionReportsPizza()
        break

    else:

        # Número 0 volta ao menu principal de pizza
        if optionReports == 0:
            headerMenu()
            pizzaMenu()

        # Número 1 exibe na tela o relatório
        elif optionReports == 1:
            allPizzaInformationReports()
