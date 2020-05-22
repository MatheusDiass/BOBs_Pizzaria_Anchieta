def nameValidation(name):
    while len(name) < 8 or len(name) > 50:
        print('O nome deve ser maior ou igual á 8 caracteres e menor ou igual á 50 caracteres!')
        name = str(input('Digite o nome novamente: '))

    return name

def addressValidation(address):
    while len(address) < 8 or len(address) > 50:
        print('O endereço deve ser maior ou igual á 8 caracteres e menor ou igual á 50 caracteres!')
        address = str(input('Digite o endereço novamente: '))

    return address

def complementValidation(complement):
    while len(complement) < 4 or len(complement) > 20:
        print('O complemento deve ser maior ou igual á 4 caracteres e menor ou igual á 20 caracteres!')
        complement = str(input('Digite o complemento novamente: '))

    return complement

def districtValidation(district):
    while len(district) < 5 or len(district) > 20:
        print('O bairro deve ser maior ou igual á 5 caracteres e menor ou igual á 20 caracteres!')
        district = str(input('Digite o bairro novamente: '))

    return district

def cityValidation(city):
    while len(city) < 3 or len(city) > 20:
        print('A cidade deve ser maior ou igual á 3 caracteres e menor ou igual á 20 caracteres!')
        city = str(input('Digite a cidade novamente: '))

    return city

def ufValidation(uf):
    while len(uf) != 2:
        print('O UF deve ter 2 caracteres!')
        uf = str(input('Digite o UF novamente: '))

    return uf.upper()

def cepValidation(cep):
    while len(cep) != 9:
        print('O CEP deve ter 8 números e um traço depois dos 5 primeiros números!')
        print('Exemplo: 12345-678')
        cep = str(input('Digite o CEP novamente: '))

    return cep

def phoneValidation(phone):
    while len(phone) != 13:
        print('Verifique o exemplo!')
        print('Exemplo: (11)4578-9123')
        phone = str(input('Digite o número de telefone novamente: '))

    return phone

def cellPhoneValidation(cellPhone):
    while len(cellPhone) != 14:
        print('Verifique o exemplo!')
        print('Exemplo: (11)98578-9123')
        cellPhone = str(input('Digte o número de telefone celular: '))

    return cellPhone