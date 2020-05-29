# Importa a função de relatório de cliente do arquivo da tabela tblcustomer
from source.db.tblCustomer import selectAllClientInformation

# Exibe o relatório de cliente
def allClientInformationReports():
    listAllClientInformation = selectAllClientInformation()

    print('--------------------------------------------')
    print('\nRelatório de Clientes - Todos os Dados\n')

    if len(listAllClientInformation) == 0:
        print('Não existem clientes cadastrados!\n')

    else:
        for customer in listAllClientInformation:
            print('Cod: ', customer[0])
            print('Nome: ', customer[1])
            print('Endereço: ', customer[2])
            print('Complemento: ', customer[3])
            print('Bairro: ', customer[4])
            print('Cidade: ', customer[5])
            print('UF: ', customer[6])
            print('CEP: ', customer[7])
            print('Telefone: ', customer[8])
            print('Celular: ', customer[9])
            print('\n')