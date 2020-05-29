# Importa as funções do arquivo da tabela tblcustomer para interagir com o banco de dados
from source.db.tblCustomer import save, updateName, updateAddress, updateComplement, updateDistrict, updateCity, updateUf, updateCep, updatePhone, updateCellPhone

# Importa as funções de validação do arquivo de validação do cliente
from source.validation.customerValidation import nameValidation, addressValidation, complementValidation, districtValidation, cityValidation, ufValidation, cepValidation, phoneValidation, cellPhoneValidation

# Salva o cliente no banco de dados e trata a exceção caso ocorrer algum erro
def customerRegister():
    print('\nCadastro de Cliente\n')

    name = str(input('Digite o nome: '))
    name = nameValidation(name)

    address = str(input('Digite o endereço: '))
    address = addressValidation(address)

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

    data_client = ([name, address, complement, district, city, uf, cep, phone, cellPhone])

    try:
        save(data_client)
        print('\nCliente salvo com sucesso!\n')
        input('Pressione qualquer tecla para continuar...')
    except:
        print('Ocorreu um erro ao cadastrar o cliente.')
        print('Contate o administrador.\n')
        input('Pressione qualquer tecla para continuar...')

# Atualiza as informações do cliente de acordo com o número selecinado
def update(option):

    # Número 1 para atualizar o nome
    if option == 1:
        print('\nAtualizar Nome\n')
        cod = int(input('Digite o código do cliente: '))
        name = str(input('Digite o nome: '))

        name = nameValidation(name)

        updateName(cod, name)

        print('\nNome atualizado com sucesso!\n')
        input('Pressione qualquer tecla para continuar...')

    # Número 2 para atualizar o endereço
    elif option == 2:
        print('\nAtualizar Endereço\n')
        cod = int(input('Digite o código do cliente: '))
        address = str(input('Digite o endereço: '))

        address = addressValidation(address)

        updateAddress(cod, address)

        print('\nEndereço atualizado com sucesso!\n')
        input('Pressione qualquer tecla para continuar...')

    # Número 3 para atualizar o complemento
    elif option == 3:
        print('\nAtualizar Complemento\n')
        cod = int(input('Digite o código do cliente: '))
        complement = str(input('Digite o complemento: '))

        complement = complementValidation(complement)

        updateComplement(cod, complement)

        print('\nComplemento atualizado com sucesso!\n')
        input('Pressione qualquer tecla para continuar...')

    # Número 4 para atualizar o bairro
    elif option == 4:
        print('\nAtualizar Bairro\n')
        cod = int(input('Digite o código do cliente: '))
        district = str(input('Digite o bairro: '))

        district = districtValidation(district)

        updateDistrict(cod, district)

        print('\nBairro atualizado com sucesso!\n')
        input('Pressione qualquer tecla para continuar...')

    # Número 5 para atualizar a cidade
    elif option == 5:
        print('\nAtualizar Cidade\n')
        cod = int(input('Digite o código do cliente: '))
        city = str(input('Digite a cidade: '))

        city = cityValidation(city)

        updateCity(cod, city)

        print('\nCidade atualizada com sucesso!\n')
        input('Pressione qualquer tecla para continuar...')

    # Número 6 para atualizar o UF
    elif option == 6:
        print('\nAtualizar UF\n')
        cod = int(input('Digite o código do cliente: '))
        uf = str(input('Digite o UF: '))

        uf = ufValidation(uf)

        updateUf(cod, uf)

        print('\nUF atualizado com sucesso!\n')
        input('Pressione qualquer tecla para continuar...')

    # Número 7 para atualizar o CEP
    elif option == 7:
        print('\nAtualizar CEP\n')
        cod = int(input('Digite o código do cliente: '))
        print('Exemplo: 12345-678')
        cep = str(input('Digite o número do CEP: '))

        cep = cepValidation(cep)

        updateCep(cod, cep)

        print('\nCEP atualizado com sucesso!\n')
        input('Pressione qualquer tecla para continuar...')

    # Número 8 para atualizar o telefone
    elif option == 8:
        print('\nAtualizar Número do Telefone\n')
        cod = int(input('Digite o código do cliente: '))
        print('Exemplo: (11)4578-9123')
        phone = str(input('Digite o número do elefone: '))

        phone = phoneValidation(phone)

        updatePhone(cod, phone)

        print('\nNúmero do telefone atualizado com sucesso!\n')
        input('Pressione qualquer tecla para continuar...')

    # Número 9 para atualizar o telefone celular
    elif option == 9:
        print('\nAtualizar Número do Celular\n')
        cod = int(input('Digite o código do cliente: '))
        print('Exemplo: (11)98578-9123')
        cellPhone = str(input('Digite o número do celular: '))

        cellPhone = cellPhoneValidation(cellPhone)

        print('\nNúmero do celular atualizado com sucesso!\n')
        input('Pressione qualquer tecla para continuar...')

        updateCellPhone(cod, cellPhone)