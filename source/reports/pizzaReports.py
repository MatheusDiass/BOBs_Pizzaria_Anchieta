# Import sqlite3 para tratar os erros
import _sqlite3

# Importado para formatar as datas
from datetime import datetime

# Importa a função de relatório de pizza do arquivo da tabela tblpizza
from source.db.tblPizza import selectAllPizzaInformation, selectPizzaByCod, selectAllPizzaActive, selectAllPizzaInactive, selectCountPizzas

# Exibe todas as pizzas
def allPizzaInformationReports():
    try:
        print('\n--------------------------------------------')
        print('Relatório de Pizzas - Todas as Pizzas\n')

        countPizzas = selectCountPizzas()
        listAllPizzaInformation = selectAllPizzaInformation()

        if len(listAllPizzaInformation) == 0:
            print('Não existem pizzas cadastradas!\n')
            input('Pressione enter para continuar...')

        else:

            print('Total de pizzas cadastradas: {}\n'.format(countPizzas[0]))

            for pizza in listAllPizzaInformation:
                averagePrice = pizza[3] + (pizza[3] * 0.15)
                bigPrice = pizza[3] + (pizza[3] * 0.25)
                giantPrice = pizza[3] + (pizza[3] * 0.35)

                print('Cod:', pizza[0])
                print('Nome:', pizza[1])
                print('Ingredientes:', pizza[2])
                print('Tipo:', pizza[8])
                print('Preço Padrão: {:.2f}'.format(pizza[3]))
                print('Preço tamanho médio: {:.2f}'.format(averagePrice))
                print('Preço tamanho grande: {:.2f}'.format(bigPrice))
                print('preço tamanho gigante: {:.2f}'.format(giantPrice))

                if (pizza[4] == 1):
                    print('Data e hora da inativação:', datetime.strftime(datetime.strptime(pizza[5], '%Y-%m-%d %H:%M:%S.%f'), '%d/%m/%Y %H:%M'))

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
            averagePrice = onePizza[3] + (onePizza[3] * 0.15)
            bigPrice = onePizza[3] + (onePizza[3] * 0.25)
            giantPrice = onePizza[3] + (onePizza[3] * 0.35)

            print('Cod:', onePizza[0])
            print('Nome:', onePizza[1])
            print('Ingredientes:', onePizza[2])
            print('Tipo:', onePizza[8])
            print('Preço Padrão: {:.2f}'.format(onePizza[3]))
            print('Preço tamanho médio: {:.2f}'.format(averagePrice))
            print('Preço tamanho grande: {:.2f}'.format(bigPrice))
            print('preço tamanho gigante: {:.2f}'.format(giantPrice))

            if(onePizza[4] == 1):
                print('Data e hora da inativação:', datetime.strftime(datetime.strptime(onePizza[5], '%Y-%m-%d %H:%M:%S.%f'), '%d/%m/%Y %H:%M'))

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
                averagePrice = pizza[3] + (pizza[3] * 0.15)
                bigPrice = pizza[3] + (pizza[3] * 0.25)
                giantPrice = pizza[3] + (pizza[3] * 0.35)

                print('Cod:', pizza[0])
                print('Nome:', pizza[1])
                print('Ingredientes:', pizza[2])
                print('Tipo:', pizza[8])
                print('Preço Padrão: {:.2f}'.format(pizza[3]))
                print('Preço tamanho médio: {:.2f}'.format(averagePrice))
                print('Preço tamanho grande: {:.2f}'.format(bigPrice))
                print('Preço tamanho gigante: {:.2f}'.format(giantPrice))
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

                #date = datetime.strptime(pizza[6], '%Y-%m-%d').date()
                #date = datetime.strptime(str(date), '%d/%m/%Y').date()

                print('Cod:', pizza[0])
                print('Nome:', pizza[1])
                print('Ingredientes:', pizza[2])
                print('Tipo: ', pizza[8])
                print('Preço Padrão: {:.2f}'.format(pizza[3]))
                print('Preço tamanho médio: {:.2f}'.format(averagePrice))
                print('Preço tamanho grande: {:.2f}'.format(bigPrice))
                print('Preço tamanho gigante: {:.2f}'.format(giantPrice))
                print('Data e hora da inativação:', datetime.strftime(datetime.strptime(pizza[5], '%Y-%m-%d %H:%M:%S.%f'), '%d/%m/%Y %H:%M'))
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

        print('Quantidade de pizzas cadastradas: ', qttPizzas[0])
        input('\nPressione enter para continuar...')

    except _sqlite3.OperationalError as error:
        print('Não foi possivel acessar as pizzas')
        print('Erro: ', error)
        input('\nPressione enter para continuar...')