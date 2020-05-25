#from source.menu.principalMenu import principal, headermenu
#from source.action.pizzaActions import updatePizza, pizzaRegister , deletarPizza , consultaListaPizza

def pizzaMenu():
    option = 0

    print('\nAções - Pizza\n')
    print('[0] - Voltar')
    print('[1] - Cadastrar')
    print('[2] - Manutenção')
    print('[3] - Deletar')
    print('[4] - Relatórios')

def pizzaMaintenanceMenu():
    option = 0

    print('\nManutenção - Pizza\n')
    print('[0] - Voltar')
    print('[1] - Alterar Nome')
    print('[2] - Alterar Ingredientes')
    print('[3] - Alterar Valor')
    print('[4] - Alterar Tipo')

'''def delete():
    print('\nDeletar - Pizza\n')

    cod = int(input('Digite o codigo da pizza:  '))

     while option >= 0:
        deletarPizza(option)
        headermenu()
        customerMenu()
    else:
        print('Codigo invalido...')
        pizzaUpdateMenu()'''

def pizzaReportsMenu():
    print('\nRelátorios - Pizzas\n')
    print('[0] - Voltar')
    print('[1] - Todos as pizzas com todas as informações')



