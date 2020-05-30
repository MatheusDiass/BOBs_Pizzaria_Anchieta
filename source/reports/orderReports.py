from source.db.tblOrder import selectAllOrderInformation

def allOrderInformationReports():

    try:
        print('--------------------------------------------')
        print('\nRelatório de Pedidos - Todos os Dados\n')

        listAllOrder = selectAllOrderInformation()

        if len(listAllOrder) == 0:
            print('Não existem pedidos atuais!\n')

        else:
            for order in listAllOrder:
                print('Cod: ', order[0])
                print('Cliente: ', order[1])
                print('Data: ', order[2])
                print('Preço total: ', order[4])
                print('\n')
    except:
        print('Não foi possivel acessar os pedidos')
        input('Pressione qualquer tecla para continuar...')

