import os
from source.menu.principalMenu import headerMenu, principal
from source.menu.customerMenu import customerMenu, customerMaintenanceMenu, customerReportsMenu
from source.actions.customerActions import customerRegister, update
from source.reports.customerReports import allClientInformationReports

def chooseOptionMenuClient():
    optionClient = int(input('Digite a opção desejada:  '))

    while optionClient < 0 or optionClient > 4:
        print('Opção Inválida!')
        input('Pressione qualquer tecla para continuar...')
        os.system('cls' if os.name == 'nt' else 'clear')
        customerMenu()
        chooseOptionMenuClient()
        break

    else:
        if optionClient == 0:
            headerMenu()
            principal()

        elif optionClient == 1:
            headerMenu()
            customerRegister()
            customerMenu()

        elif optionClient == 2:
            headerMenu()
            customerMaintenanceMenu()
            chooseOptionMaintenance()

        elif optionClient == 4:
            headerMenu()
            customerReportsMenu()
            chooseOptionReports()

def chooseOptionMaintenance():
    optionMaintenance = int(input('Digite a opção desejada:  '))

    while optionMaintenance < 0 or optionMaintenance > 9:
        print('Opção Inválida!')
        input('Pressione qualquer tecla para continuar...')
        os.system('cls' if os.name == 'nt' else 'clear')
        customerMaintenanceMenu()
        chooseOptionMaintenance()
        break

    else:

        if optionMaintenance == 0:
            headerMenu()
            customerMenu()

        else:
            update(optionMaintenance)
            headerMenu()
            customerMenu()

def chooseOptionReports():
    optionReports = int(input('Digite a opção desejada:  '))

    while optionReports < 0 or optionReports > 1:
        print('Opção Inválida!')
        input('Pressione qualquer tecla para continuar...')
        os.system('cls' if os.name == 'nt' else 'clear')
        customerReportsMenu()
        chooseOptionReports()
        break

    else:

        if optionReports == 0:
            headerMenu()
            customerMenu()

        elif optionReports == 1:
            allClientInformationReports()