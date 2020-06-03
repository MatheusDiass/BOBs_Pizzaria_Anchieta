# Import sqlite3 para tratar os erros
import _sqlite3

# Importado para formatar a data
from datetime import date, datetime

# Importa a função de relatório de pedidos
from source.db.tblOrder import selectAllOrderInformation, selectAllOrderBetweenDate

# Exibe todos os pedidos
def allOrderInformationReports():
    try:
        print('\n--------------------------------------------')
        print('Relatório de Pedidos - Todos os Pedidos\n')

        listAllOrder = selectAllOrderInformation()

        if len(listAllOrder) == 0:
            print('Não existem pedidos atuais!\n')
            input('Pressione enter para continuar...')

        else:
            for order in listAllOrder:
                # Formata a data
                date = datetime.strftime(datetime.strptime(order[1], '%Y-%m-%d'), '%d/%m/%Y')
                print('Cod do Pedido:', order[0])
                print('Data do Pedido:', date)
                print('Nome do Cliente:', order[2])
                print('Preço total: {:.2f}'.format(order[3]))
                print('\n')

            input('Pressione enter para continuar...')

    except _sqlite3.OperationalError as error:
        print('\nNão foi possivel buscar os clientes')
        print('Erro: ', error)
        input('\nPressione enter para continuar...')

# Exibe todos os pedidos de acordo com o periodo informado
def allOrderBetweenDateReports():
    try:
        print('\nExemplo de data: 28/09/2010\n')
        staDate = str(input('Digite a data de inicio: '))
        endDate = str(input('Digite a data de fim: '))

        # Formata a data
        staDate = datetime.strptime(staDate, '%d/%m/%Y').date()
        endDate = datetime.strptime(endDate, '%d/%m/%Y').date()

        print('\n--------------------------------------------')
        print('Relatório de Pedidos - Pedidos por Período\n')

        listAllOrderBetweenDate = selectAllOrderBetweenDate(str(staDate), str(endDate))

        if len(listAllOrderBetweenDate) == 0:
            print('Não existem pedidos atuais!\n')

        else:
            for order in listAllOrderBetweenDate:
                # Formata a data
                date = datetime.strftime(datetime.strptime(order[1], '%Y-%m-%d'), '%d/%m/%Y')
                print('Cod do Pedido:', order[0])
                print('Data do Pedido:', date)
                print('Nome do Cliente:', order[2])
                print('Preço total: {:.2f}'.format(order[3]))
                print('\n')

            input('Pressione enter para continuar...')

    except ValueError as error:
        print('\nNão foi possivel buscar os pedidos')
        print('Erro: ', error)
        input('\nPressione enter para continuar...')

    except _sqlite3.OperationalError as error:
        print('\nNão foi possivel buscar os pedidos')
        print('Erro: ', error)
        input('\nPressione enter para continuar...')