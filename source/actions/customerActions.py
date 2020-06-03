# Para validar erros
import _sqlite3

# Importa as funções do arquivo da tabela tblcustomer para interagir com o banco de dados
from source.db.tblCustomer import save, updateName, updateAddress, updateComplement, updateDistrict, updateCity, updateUf, updateCep, updatePhone, updateCellPhone, delete, selectCustomerByCod

# Importa as funções de validação do arquivo de validação do cliente
from source.validation.customerValidation import customerCodValidation, nameValidation, addressValidation, numberValidation, complementValidation, districtValidation, cityValidation, ufValidation, cepValidation, phoneValidation, cellPhoneValidation

# Salva o cliente no banco de dados e trata a exceção caso ocorrer algum erro
def customerRegister():
    print('\nCadastro de Cliente\n')

    name = str(input('Digite o nome: '))
    name = nameValidation(name)

    address = str(input('Digite o endereço: '))
    address = addressValidation(address)

    number = str(input('Digite o número: '))
    number = numberValidation(number)

    complement = str(input('Digite o complemento: '))
    complement = complementValidation(complement)

    district = str(input('Digite o bairro: '))
    district = districtValidation(district)

    city = str(input('Digite a cidade: '))
    city = cityValidation(city)

    uf = str(input('Digite o UF: '))
    uf = ufValidation(uf)

    print('Exemplo: 12345-678')
    cep = str(input('Digite o CEP: '))
    cep = cepValidation(cep)

    print('Exemplo: (11)4578-9123')
    phone = str(input('Digite o número de telefone: '))
    phone = phoneValidation(phone)

    print('Exemplo: (11)98578-9123')
    cellPhone = str(input('Digte o número de telefone celular: '))
    cellPhone = cellPhoneValidation(cellPhone)

    data_client = ([name, address, number, complement, district, city, uf, cep, phone, cellPhone])

    try:
        save(data_client)

        print('\nCliente salvo com sucesso!\n')
        input('Pressione qualquer tecla para continuar...')

    except _sqlite3.OperationalError as error:
        print('\nNão foi possivel cadastrar o cliente!')
        print('Erro: ', error)
        input('\nPressione enter para continuar...')

# Atualiza as informações do cliente de acordo com o número selecinado
def update(option):
    try:
        # Número 1 para atualizar o nome
        if option == 1:
            print('\nAtualizar Nome\n')
            cod = input('Digite o código do cliente: ')
            cod = customerCodValidation(cod)
            name = str(input('Digite o nome: '))

            name = nameValidation(name)

            updateName(cod, name)

            print('\nNome atualizado com sucesso!\n')
            input('Pressione qualquer tecla para continuar...')

        # Número 2 para atualizar o endereço
        elif option == 2:
            print('\nAtualizar Endereço\n')
            cod = input('Digite o código do cliente: ')
            cod = customerCodValidation(cod)
            address = str(input('Digite o endereço: '))

            address = addressValidation(address)

            updateAddress(cod, address)

            print('\nEndereço atualizado com sucesso!\n')
            input('Pressione qualquer tecla para continuar...')

        # Número 3 para atualizar o complemento
        elif option == 3:
            print('\nAtualizar Complemento\n')
            cod = input('Digite o código do cliente: ')
            cod = customerCodValidation(cod)
            complement = str(input('Digite o complemento: '))

            complement = complementValidation(complement)

            updateComplement(cod, complement)

            print('\nComplemento atualizado com sucesso!\n')
            input('Pressione qualquer tecla para continuar...')

        # Número 4 para atualizar o bairro
        elif option == 4:
            print('\nAtualizar Bairro\n')
            cod = input('Digite o código do cliente: ')
            cod = customerCodValidation(cod)
            district = str(input('Digite o bairro: '))

            district = districtValidation(district)

            updateDistrict(cod, district)

            print('\nBairro atualizado com sucesso!\n')
            input('Pressione qualquer tecla para continuar...')

        # Número 5 para atualizar a cidade
        elif option == 5:
            print('\nAtualizar Cidade\n')
            cod = input('Digite o código do cliente: ')
            cod = customerCodValidation(cod)
            city = str(input('Digite a cidade: '))

            city = cityValidation(city)

            updateCity(cod, city)

            print('\nCidade atualizada com sucesso!\n')
            input('Pressione qualquer tecla para continuar...')

        # Número 6 para atualizar o UF
        elif option == 6:
            print('\nAtualizar UF\n')
            cod = input('Digite o código do cliente: ')
            cod = customerCodValidation(cod)
            uf = str(input('Digite o UF: '))

            uf = ufValidation(uf)

            updateUf(cod, uf)

            print('\nUF atualizado com sucesso!\n')
            input('Pressione qualquer tecla para continuar...')

        # Número 7 para atualizar o CEP
        elif option == 7:
            print('\nAtualizar CEP\n')
            cod = input('Digite o código do cliente: ')
            cod = customerCodValidation(cod)
            print('Exemplo: 12345-678')
            cep = str(input('Digite o número do CEP: '))

            cep = cepValidation(cep)

            updateCep(cod, cep)

            print('\nCEP atualizado com sucesso!\n')
            input('Pressione qualquer tecla para continuar...')

        # Número 8 para atualizar o telefone
        elif option == 8:
            print('\nAtualizar Número do Telefone\n')
            cod = input('Digite o código do cliente: ')
            cod = customerCodValidation(cod)
            print('Exemplo: (11)4578-9123')
            phone = str(input('Digite o número do elefone: '))

            phone = phoneValidation(phone)

            updatePhone(cod, phone)

            print('\nNúmero do telefone atualizado com sucesso!\n')
            input('Pressione qualquer tecla para continuar...')

        # Número 9 para atualizar o telefone celular
        elif option == 9:
            print('\nAtualizar Número do Celular\n')
            cod = input('Digite o código do cliente: ')
            print('Exemplo: (11)98578-9123')
            cellPhone = str(input('Digite o número do celular: '))

            cellPhone = cellPhoneValidation(cellPhone)

            print('\nNúmero do celular atualizado com sucesso!\n')
            input('Pressione qualquer tecla para continuar...')

            updateCellPhone(cod, cellPhone)

    except _sqlite3.OperationalError as error:
        print('\nNão foi possivel atualizar o cadastro do cliente!')
        print('Erro: ', error)
        input('\nPressione enter para continuar...')

# Deleta o cliente
def deleteCustomer():
    try:
        cod = input('Digite o código do cliente: ')

        cod = customerCodValidation(cod)

        # Importa "selectOrderCustomer" para realizar uma validação antes de excluir o cliente
        from source.db.tblOrder import selectOrderCustomer
        orderCustomer = selectOrderCustomer(cod)

        if not orderCustomer:
            delete(cod)

            print('\nCliente deletado com sucesso!')
            input('\nPressione enter para continuar...')

        else:
            print('\nNão foi possivel deletar pois existem pedidos relacionados a este cliente!')
            input('\nPressione enter para continuar...')

    except _sqlite3.OperationalError as error:
        print('\nNão foi possivel deletar o cliente!')
        print('Erro: ', error)
        input('\nPressione enter para continuar...')