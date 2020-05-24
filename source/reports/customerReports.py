from source.db.tblCustomer import selectAllClientInformation

# Report with all information of the all clients
def allClientInformationReports():
    listAllClientInformation = selectAllClientInformation()

    print('----------------------------------------------------------')
    print('\nRelatório de Clientes - Todos os Dados\n')

    if len(listAllClientInformation) == 0:
        print('Não existem clientes cadastrados\n')

    else:
        for clint in listAllClientInformation:
            print('Cod: ', clint[0])
            print('Nome: ', clint[1])
            print('Endereço: ', clint[2])
            print('Complemento: ', clint[3])
            print('Bairro: ', clint[4])
            print('Cidade: ', clint[5])
            print('UF: ', clint[6])
            print('CEP: ', clint[7])
            print('Telefone: ', clint[8])
            print('Celular: ', clint[9])
            print('\n')