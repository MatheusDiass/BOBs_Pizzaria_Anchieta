def nameValidation(name):
    while len(name) < 4 or len(name) > 50:
        print('O nome deve ser maior ou igual á 4 caracteres e menor ou igual á 50 caracteres!')
        name = str(input('Digite o nome novamente: '))

    return name

def ingredientValidation(ingredient):
    while len(ingredient) < 5 or len(ingredient) > 200:
        print('O nome tipo ser maior ou igual á 4 caracteres e menor ou igual á 20 caracteres!')
        ingredient = str(input('Digite o tipo novamente: '))

    return ingredient

def typeValidation(type):
    while len(type) < 4 or len(type) > 20 or type.isnumeric():
        print('O nome tipo ser maior ou igual á 4 caracteres e menor ou igual á 20 caracteres!')
        type = str(input('Digite o tipo novamente: '))

    return type

def priceValidation(price):
    while not price.isdecimal():
        print('O preço não pode conter letras!')
        price = str(input('Digite o preço novamente: '))

    return price