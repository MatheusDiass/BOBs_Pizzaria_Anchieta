# Válida se o código do cliente só contem números
def pizzaCodValidation(cod):
    while not cod.isnumeric():
        print('Opção Inválida!')
        cod = input('Digite o código da pizza novamente: ')

    cod = int(cod)

    return cod

# Válida o que foi digitado no nome
def nameValidation(name):
    while len(name) < 4 or len(name) > 50:
        print('O nome deve ser maior ou igual á 4 caracteres e menor ou igual á 50 caracteres!')
        name = str(input('Digite o nome novamente: '))

    return name

# Válida o que foi digitado no ingrediente
def ingredientValidation(ingredient):
    while len(ingredient) < 5 or len(ingredient) > 200:
        print('Os ingredientes deve ser maior ou igual á 5 caracteres e menor ou igual á 200 caracteres!')
        ingredient = str(input('Digite o tipo novamente: '))

    return ingredient

# Válida o que foi digitado no tipo
def typeValidation(type, countType):
    while not type.isnumeric():
        print('O código do tipo não pode conter letras!'.format(countType))
        type = input('Digite o código do tipo novamente: ')

    type = int(type)

    while type < 1 or type > countType:
        print('O código do tipo deve ser maior ou igual a 1 ou menor ou igual a {}!'.format(countType))
        type = input('Digite o código do tipo novamente: ')

        while not type.isnumeric():
            print('O código do tipo não pode conter letras!'.format(countType))
            type = input('Digite o código do tipo novamente: ')

        type = int(type)

    return type

# Válida o que foi digitado no preço
def priceValidation(price):
    while not price.replace('.', '').isnumeric():
        print('O preço não pode conter letras!')
        price = str(input('Digite o preço novamente: '))

    return price