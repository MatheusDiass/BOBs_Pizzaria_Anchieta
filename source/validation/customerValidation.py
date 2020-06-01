# Válida o que foi digitado no nome
def nameValidation(name):
    while len(name) < 8 or len(name) > 50 or name.isnumeric():
        print('O nome deve ser maior ou igual á 8 caracteres e menor ou igual á 50 caracteres, não pode conter números!')
        name = str(input('Digite o nome novamente: '))

    return name

# Válida o que foi digitado no endereço
def addressValidation(address):
    while len(address) < 8 or len(address) > 50:
        print('O endereço deve ser maior ou igual á 8 caracteres e menor ou igual á 50 caracteres!')
        address = str(input('Digite o endereço novamente: '))

    return address

# Válida o que foi digitado no número
def numberValidation(number):
    while not number.isnumeric():
        print('O número do endereço só pode conter números!')
        address = str(input('Digite o número novamente: '))

    return number

# Válida o que foi digitado no complemento
def complementValidation(complement):
    while len(complement) < 4 or len(complement) > 20 or complement.isnumeric():
        print('O complemento deve ser maior ou igual á 4 caracteres e menor ou igual á 20 caracteres, não pode conter números!')
        complement = str(input('Digite o complemento novamente: '))

    return complement

# Válida o que foi digitado no bairro
def districtValidation(district):
    while len(district) < 5 or len(district) > 20:
        print('O bairro deve ser maior ou igual á 5 caracteres e menor ou igual á 20 caracteres!')
        district = str(input('Digite o bairro novamente: '))

    return district

# Válida o que foi digitado na cidade
def cityValidation(city):
    while len(city) < 3 or len(city) > 20 or city.isnumeric():
        print('A cidade deve ser maior ou igual á 3 caracteres e menor ou igual á 20 caracteres, não pode conter números!')
        city = str(input('Digite a cidade novamente: '))

    return city

# Válida o que foi digitado no UF
def ufValidation(uf):
    while len(uf) != 2 or uf.isnumeric():
        print('O UF deve ter 2 caracteres e não pode conter números!')
        uf = str(input('Digite o UF novamente: '))

    return uf.upper()

# Válida o que foi digitado no CEP
def cepValidation(cep):
    while len(cep) != 9:
        print('O CEP deve ter 8 números e um traço depois dos 5 primeiros números!')
        print('Exemplo: 12345-678')
        cep = str(input('Digite o CEP novamente: '))

    return cep

# Válida o que foi digitado no telefone
def phoneValidation(phone):
    while len(phone) != 13:
        print('Verifique o exemplo!')
        print('Exemplo: (11)4578-9123')
        phone = str(input('Digite o número de telefone novamente: '))

    return phone

# Válida o que foi digitado no telefone celular
def cellPhoneValidation(cellPhone):
    while len(cellPhone) != 14:
        print('Verifique o exemplo!')
        print('Exemplo: (11)98578-9123')
        cellPhone = str(input('Digte o número de telefone celular: '))

    return cellPhone