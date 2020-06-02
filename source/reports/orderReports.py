# Import sqlite3 para tratar os erros
import _sqlite3

# Importado para formatar a data
from datetime import date, datetime

# Importa a função de relatório de pedidos
from source.db.tblOrder import selectAllOrderInformation, selectAllOrderBetweenDate

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

def allOrderBetweenDateReports():
    try:
        print('\nExemplo de data: 28/09/2010\n')
        staDate = str(input('Digite a data de inicio: '))
        endDate = str(input('Digite a data de fim: '))

        staDate = datetime.strptime(staDate, '%d/%m/%Y').date()
        endDate = datetime.strptime(endDate, '%d/%m/%Y').date()

        print('\n--------------------------------------------')
        print('Relatório de Pedidos - Pedidos por Período\n')

        listAllOrderBetweenDate = selectAllOrderBetweenDate(str(staDate), str(endDate))

        if len(listAllOrderBetweenDate) == 0:
            print('Não existem pedidos atuais!\n')

        else:
            for order in listAllOrderBetweenDate:
                print('Cod do Pedido:', order[0])
                print('Data do Pedido:', order[1])
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