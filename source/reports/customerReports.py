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
            print('Número: ', customer[3])
            print('Complemento: ', customer[4])
            print('Bairro: ', customer[5])
            print('Cidade: ', customer[6])
            print('UF: ', customer[7])
            print('CEP: ', customer[8])
            print('Telefone: ', customer[9])
            print('Celular: ', customer[10])
            print('\n')