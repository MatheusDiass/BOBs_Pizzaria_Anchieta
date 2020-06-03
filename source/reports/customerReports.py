# Import sqlite3 para tratar os erros
import _sqlite3

# Importa a função de relatório de cliente do arquivo da tabela tblcustomer
from source.db.tblCustomer import selectAllCustomertInformation, selectCustomerByCod, selectCountCustomer

# Exibe todos os clientes
def allClientInformationReports():
    try:
        print('\n--------------------------------------------')
        print('Relatório de Clientes - Todos os Clientes\n')

        countCustomer = selectCountCustomer()
        listAllClientInformation = selectAllCustomertInformation()

        if len(listAllClientInformation) == 0:
            print('Não existem clientes cadastrados!\n')
            input('Pressione enter para continuar...')

        else:

            print('Total de clientes cadastrados: {}\n'.format(countCustomer[0]))

            for customer in listAllClientInformation:
                print('Cod:', customer[0])
                print('Nome:', customer[1])
                print('Endereço:', customer[2])
                print('Número:', customer[3])
                print('Complemento:', customer[4])
                print('Bairro:', customer[5])
                print('Cidade:', customer[6])
                print('UF:', customer[7])
                print('CEP:', customer[8])
                print('Telefone:', customer[9])
                print('Celular:', customer[10])
                print('\n')

            input('Pressione enter para continuar...')

    except _sqlite3.OperationalError as error:
        print('\nNão foi possivel buscar os clientes')
        print('Erro: ', error)
        input('\nPressione enter para continuar...')

# Exibe apenas um cliente, encontrado pelo código
def oneCustomerInformationReports():
    try:
        cod = input('Digite código do cliente: ')

        while not cod.isnumeric():
            print('Opção Inválida!')
            cod = input('Digite o código do cliente novamente: ')

        cod = int(cod)

        print('\n--------------------------------------------')
        print('Relatório de Clientes - Um Cliente\n')

        oneCustomer = selectCustomerByCod(cod)

        if not oneCustomer:
            print('Cliente não encontrado!\n')
            input('Pressione enter para continuar...')

        else:
            print('Cod:', oneCustomer[0])
            print('Nome:', oneCustomer[1])
            print('Endereço:', oneCustomer[2])
            print('Número:', oneCustomer[3])
            print('Complemento:', oneCustomer[4])
            print('Bairro:', oneCustomer[5])
            print('Cidade:', oneCustomer[6])
            print('UF:', oneCustomer[7])
            print('CEP:', oneCustomer[8])
            print('Telefone:', oneCustomer[9])
            print('Celular:', oneCustomer[10])
            print('\n')

            input('Pressione enter para continuar...')

    except _sqlite3.OperationalError as error:
        print('\nNão foi possivel buscar os clientes')
        print('Erro: ', error)
        input('\nPressione enter para continuar...')

# Exibe a quantidade de clientes cadastrados
def quantityCustomerReports():
    try:
        print('\n--------------------------------------------')
        print('Relatório de Clientes - Quantidade\n')

        countCustomer = selectCountCustomer()

        print('Quantidade de clientes cadastrados:', countCustomer[0])
        input('\nPressione enter para continuar...')

    except _sqlite3.OperationalError as error:
        print('\nNão foi possivel buscar os clientes')
        print('Erro: ', error)
        input('\nPressione enter para continuar...')