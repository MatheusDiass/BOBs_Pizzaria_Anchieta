# Import sqlite3 para tratar os erros
import _sqlite3

# Importa a função de relatório de pizza do arquivo da tabela tblpizza
from source.db.tblPizza import selectAllPizzaInformation, selectPizzaByCod, selectAllPizzaActive, selectAllPizzaInactive, selectCountPizzas

# Exibe todas as pizzas
def allPizzaInformationReports():
    try:
        print('\n--------------------------------------------')
        print('Relatório de Pizzas - Todas as Pizzas\n')

        listAllPizzaInformation = selectAllPizzaInformation()

        if len(listAllPizzaInformation) == 0:
            print('Não existem pizzas cadastradas!\n')
            input('Pressione enter para continuar...')

        else:
            for pizza in listAllPizzaInformation:
                print('Cod: ', pizza[0])
                print('Nome: ', pizza[1])
                print('Ingredientes: ', pizza[2])
                print('Tipo: ', pizza[3])
                print('Valor: ', pizza[4])

                if(pizza[5] == 1):
                    print('Data de Inatividade: ', pizza[6])

                print('\n')

        input('Pressione enter para continuar...')

    except _sqlite3.OperationalError as error:
        print('\nNão foi possivel acessar as pizzas')
        print('Erro: ', error)
        input('\nPressione enter para continuar...')

# Exibe apenas uma pizza, encontrada pelo código
def onePizzaInformationReports():
    try:
        cod = input('Digite código da pizza: ')

        while not cod.isnumeric():
            print('Opção Inválida!')
            cod = input('Digite o código da pizza novamente: ')

        cod = int(cod)

        print('\n--------------------------------------------')
        print('Relatório de Pizzas - Uma Pizza\n')

        onePizza = selectPizzaByCod(cod)

        if not onePizza:
            print('Pizza não encontrado!\n')
            input('Pressione enter para continuar...')

        else:
            averagePrice = onePizza[4] + (onePizza[4] * 0.15)
            bigPrice = onePizza[4] + (onePizza[4] * 0.25)
            giantPrice = onePizza[4] + (onePizza[4] * 0.35)

            print('Cod: ', onePizza[0])
            print('Nome: ', onePizza[1])
            print('Ingredientes: ', onePizza[2])
            print('Tipo: ', onePizza[3])
            print('Valor tamanho médio: ', averagePrice)
            print('Valor tamanho grande: ', bigPrice)
            print('Valor tamanho gigante: ', giantPrice)

            if(onePizza[5] == 1):
                print('Data de Inatividade: ', onePizza[6])

            print('\n')

            input('Pressione enter para continuar...')

    except _sqlite3.OperationalError as error:
        print('Não foi possivel acessar as pizzas')
        print('Erro: ', error)
        input('\nPressione enter para continuar...')

# Exibe todas as pizzas ativas
def allPizzaActiveReports():
    try:
        print('\n--------------------------------------------')
        print('Relatório de Pizzas - Pizzas Ativas\n')

        listPizzaActive = selectAllPizzaActive()

        if len(listPizzaActive) == 0:
            print('Não existem pizzas ativas ou cadastradas!\n')
            input('Pressione enter para continuar...')

        else:
            for pizza in listPizzaActive:
                averagePrice = pizza[4] + (pizza[4] * 0.15)
                bigPrice = pizza[4] + (pizza[4] * 0.25)
                giantPrice = pizza[4] + (pizza[4] * 0.35)

                print('Cod: ', pizza[0])
                print('Nome: ', pizza[1])
                print('Ingredientes: ', pizza[2])
                print('Tipo: ', pizza[3])
                print('Valor tamanho médio: ', averagePrice)
                print('Valor tamanho grande: ', bigPrice)
                print('Valor tamanho gigante: ', giantPrice)
                print('\n')

            input('Pressione enter para continuar...')


    except _sqlite3.OperationalError as error:
        print('Não foi possivel acessar as pizzas')
        print('Erro: ', error)
        input('\nPressione enter para continuar...')

# Exibe todas as pizzas inativas
def allPizzaInactiveReports():
    try:
        print('\n--------------------------------------------')
        print('Relatório de Pizzas - Pizzas Inativas\n')

        listPizzaInactive = selectAllPizzaInactive()

        if len(listPizzaInactive) == 0:
            print('Não existem pizzas inativas ou cadastradas!\n')
            input('Pressione enter para continuar...')

        else:
            for pizza in listPizzaInactive:
                averagePrice = pizza[4] + (pizza[4] * 0.15)
                bigPrice = pizza[4] + (pizza[4] * 0.25)
                giantPrice = pizza[4] + (pizza[4] * 0.35)

                print('Cod: ', pizza[0])
                print('Nome: ', pizza[1])
                print('Ingredientes: ', pizza[2])
                print('Tipo: ', pizza[3])
                print('Valor tamanho médio: ', averagePrice)
                print('Valor tamanho grande: ', bigPrice)
                print('Valor tamanho gigante: ', giantPrice)
                print('\n')

            input('Pressione enter para continuar...')


    except _sqlite3.OperationalError as error:
        print('Não foi possivel acessar as pizzas')
        print('Erro: ', error)
        input('\nPressione enter para continuar...')

# Exibe a quantidade de pizzas cadastradas
def quantityPizzaReports():
    try:
        print('\n--------------------------------------------')
        print('Relatório de Pizzas - Quantidade\n')

        qttPizzas = selectCountPizzas()

        print('Quantidade de pizzas cadastrados: ', qttPizzas[0][0])
        input('\nPressione enter para continuar...')

    except _sqlite3.OperationalError as error:
        print('Não foi possivel acessar as pizzas')
        print('Erro: ', error)
        input('\nPressione enter para continuar...')