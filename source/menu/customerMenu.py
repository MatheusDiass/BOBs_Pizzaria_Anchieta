from source.actions.customerActions import customerRegister, update
from source.reports.customerReports import allClientInformationReports

# Client Menu
def customerMenu():
    #optionClient = 0

    print('\nAções - Cliente\n')
    print('[0] - Voltar')
    print('[1] - Cadastro')
    print('[2] - Manutenção')
    print('[3] - Deletar')
    print('[4] - Relatórios')

    '''optionClient = int(input('Digite a opção desejada:  '))

    while optionClient < 0 or optionClient > 4:
        print('Opção Inválida!')
        input('Pressione qualquer tecla para continuar...')
        os.system('cls' if os.name == 'nt' else 'clear')
        customerMenu()
        break

    else:
        if optionClient == 0:
            headermenu()
            principal()

        elif optionClient == 1:
            headermenu()
            customerRegister()
            customerMenu()

        elif optionClient == 2:
            headermenu()
            maintenanceMenu()

        elif optionClient == 4:
            headermenu()
            reportsMenu()'''


def maintenanceMenu():
    print('\nManutenção - Cliente\n')
    print('[0] - Voltar')
    print('[1] - Alterar Nome')
    print('[2] - Alterar Endereço')
    print('[3] - Alterar Complemento')
    print('[4] - Alterar Bairro')
    print('[5] - Alterar Cidade')
    print('[6] - Alterar UF')
    print('[7] - Alterar CEP')
    print('[8] - Alterar Telefone')
    print('[9] - Alterar Celular')

    '''optionMaintenance = int(input('Digite a opção desejada:  '))

    while optionMaintenance >= 0 or optionMaintenance <= 9:

        if optionMaintenance == 0:
            headermenu()
            customerMenu()

        else:
            update(optionMaintenance)
            headermenu()
            customerMenu()

    else:
        customerMenu()'''

def reportsMenu():
    optionReports = 0

    print('\nRelátorios - Cliente\n')
    print('[0] - Voltar')
    print('[1] - Todos os clientes com todas as informações')

    '''while optionReports >= 0 or optionReports <= 1:
        if optionReports == 0:
            headermenu()
            customerMenu()
            break

        elif optionReports == 1:
            allClientInformationReports()
            break'''