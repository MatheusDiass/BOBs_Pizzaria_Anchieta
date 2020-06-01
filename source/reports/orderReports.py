# Import sqlite3 para tratar os erros
import _sqlite3

# Importa a função de relatório de pedidos
from source.db.tblOrder import selectAllOrderInformation

def allOrderInformationReports():

    try:
        print('\n--------------------------------------------')
        print('Relatório de Pedidos - Todos os Pedidos\n')

        listAllOrder = selectAllOrderInformation()

        if len(listAllOrder) == 0:
            print('Não existem pedidos atuais!\n')

        else:
            for order in listAllOrder:
                print('Cod do Pedido: ', order[0])
                print('Data do Pedido: ', order[1])
                print('Nome do Cliente: ', order[2])
                print('Preço total: ', order[3])
                print('\n')

            input('Pressione enter para continuar...')

    except _sqlite3.OperationalError as error:
        print('\nNão foi possivel buscar os clientes')
        print('Erro: ', error)
        input('\nPressione enter para continuar...')

