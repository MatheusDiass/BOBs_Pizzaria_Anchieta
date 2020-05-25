import os
from source.menu.principalMenu import headerMenu, principal
from source.menu.pizzaMenu import pizzaMenu, pizzaMaintenanceMenu, pizzaReportsMenu
from source.actions.pizzaActions import pizzaRegister, update
from source.reports.pizzaReports import allPizzaInformationReports

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
        if optionPizza == 0:
            headerMenu()
            principal()

        elif optionPizza == 1:
            pizzaRegister()
            headerMenu()

        elif optionPizza == 2:
            pizzaMaintenanceMenu()
            chooseOptionMaintenancePizza()

        elif optionPizza == 4:
            headerMenu()
            pizzaReportsMenu()
            chooseOptionReportsPizza()

def chooseOptionMaintenancePizza():
    optionMaintenance = int(input('Digite a opção desejada:  '))

    while optionMaintenance < 0 or optionMaintenance > 1:
        print('Opção Inválida!')
        input('Pressione qualquer tecla para continuar...')
        os.system('cls' if os.name == 'nt' else 'clear')
        pizzaMaintenanceMenu()
        chooseOptionMaintenancePizza()
        break

    else:
        if optionMaintenance == 0:
            headerMenu()
            pizzaMenu()

        elif optionMaintenance == 1:
            update(optionMaintenance)
            headerMenu()
            pizzaMenu()

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

        if optionReports == 0:
            headerMenu()
            pizzaMenu()

        elif optionReports == 1:
            allPizzaInformationReports()
