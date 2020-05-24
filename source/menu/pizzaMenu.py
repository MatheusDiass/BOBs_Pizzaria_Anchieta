from source.menu.principalMenu import principal, headermenu
from source.action.pizzaActions import updatePizza, pizzaRegister , deletarPizza , consultaListaPizza

def pizzaMenu():
    option = 0

    print('\nAções - Cliente\n')
    print('[0] - Voltar')
    print('[1] - Incluir')
    print('[2] - Manutenção')
    print('[3] - Deletar')
    print('[4] - Consultar')

    option = int(input('Digite a opção desejada:  '))

    while option >= 0 or option <= 4:
        if option == 0:
            headermenu()
            principal()
            break

    elif option == 1:
        pizzaRegister()
        headermenu()
        break

    elif option == 2:
        pizzaUpdateMenu()    
        break

    elif option == 4:
       
        break


def pizzaUpdateMenu():
    option = 0

    print('\nManutenção - Pizza\n')
    print('[0] - Voltar')
    print('[1] - Alterar Nome')
    print('[2] - Alterar Ingredientes')
    print('[3] - Alterar Valor')
    print('[4] - Alterar Tipo')

    option = int(input('Digite a opção desejada:  '))

    while option >= 0 or option <= 9:
        if(option == 0):
             headermenu()
            customerMenu()
        else:
            updatePizza(option)
            headermenu()
            customerMenu()
        
    else:
        pizzaUpdateMenu()

def pizzaDeleteMenu():
    print('\nDeletar - Pizza\n')

    cod = int(input('Digite o codigo da pizza:  '))

     while option >= 0:
        deletarPizza(option)
        headermenu()
        customerMenu()
    else:
        print('Codigo invalido...')
        pizzaUpdateMenu()

def pizzaConsultaMenu():
    print('\nConsulta - Pizza\n')

    consultaListaPizza()



