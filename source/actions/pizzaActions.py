# Para validar erros
import _sqlite3

# Importa as funções do arquivo da tabela tblpizza para interagir com o banco de dados
from source.db.tblPizza import save, updateName, updateIngredient, updatePrice, updateType, deactivate

# Importa a função que busca todos os tipos de pizza
from source.db.tblpizzatype import selectAllInformationTypePizza, selectCountTypePizza

# Importa as funções de validação do arquivo de validação do cliente
from source.validation.pizzaValidation import pizzaCodValidation, nameValidation, ingredientValidation, typeValidation, priceValidation

# Salva a pizza no banco de dados e trata a exceção caso ocorrer algum erro
def pizzaRegister():
    print('\nCadastro de pizza\n')

    try:
        listTypePizza = selectAllInformationTypePizza()
        countTypePizza = selectCountTypePizza()

        name = str(input('Digite o nome: '))
        name = nameValidation(name)

        ingredient = str(input('Digite os ingredientes: '))
        ingredient = ingredientValidation(ingredient)

        for type in listTypePizza:
            print('[{}] - {}'.format(type[0], type[1]))

        type = input('Digite o código do tipo: ')
        type = typeValidation(type, countTypePizza[0])

        price = input('Digite o valor: ')
        price = priceValidation(price)

        inactvated = 0

        data_pizza = ([name, ingredient, price, inactvated, type])

        save(data_pizza)

        print('\nPizza salva com sucesso!\n')
        input('Pressione qualquer tecla para continuar...')

    except _sqlite3.OperationalError as error:
        print('\nNão foi possivel cadastrar a pizza')
        print('Erro: ', error)
        input('\nPressione enter para continuar...')

# Atualiza as informações da pizza de acordo com o número selecinado
def update(option):
    try:
        # Número 1 para atualizar o nome
        if option == 1:
            print('\nAtualizar Nome\n')

            cod = input('Digite o código da pizza: ')
            cod = pizzaCodValidation(cod)
            name = str(input('Digite o nome: '))

            updateName(cod, name)

            print('\nNome da pizza atualizado com sucesso\n')
            input('Pressione qualquer tecla para continuar...')

        # Número 2 para atualizar os ingredientes
        elif option == 2:
            print('\nAtualizar ingredientes\n')
            cod = input('Digite o código da pizza: ')
            cod = pizzaCodValidation(cod)
            ingredient = str(input('Digite os ingredientes: '))

            updateIngredient(cod, ingredient)

            print('\nIngredientes da pizza atualizados com sucesso\n')
            input('Pressione qualquer tecla para continuar...')

        # Número 3 para atualizar o valor
        elif option == 3:
            print('\nAtualizar Valor\n')
            cod = input('Digite o código da pizza: ')
            cod = pizzaCodValidation(cod)
            price = int(input('Digite o valor: '))

            updatePrice(cod, price)

            print('\nValor da pizza atualizado com sucesso\n')
            input('Pressione qualquer tecla para continuar...')

        # Número 4 para atualizar o tipo
        elif option == 4:
            print('\nAtualizar Tipo\n')
            cod = input('Digite o código da pizza: ')
            cod = pizzaCodValidation(cod)

            listTypePizza = selectAllInformationTypePizza()
            countTypePizza = selectCountTypePizza()

            for type in listTypePizza:
                print('[{}] - {}'.format(type[0], type[1]))

            type = input('Digite o código do tipo: ')
            type = typeValidation(type, countTypePizza[0])

            updateType(cod, type)

            print('\nTipo da pizza atualizado com sucesso\n')
            input('Pressione qualquer tecla para continuar...')

    except _sqlite3.OperationalError as error:
        print('\nNão foi possivel atualizar o cadastro da pizza!')
        print('Erro: ', error)
        input('\nPressione enter para continuar...')

# Desativar a pizza
def deactivatePizza():
    try:
        cod = input('Digite o código da pizza:  ')

        cod = pizzaCodValidation(cod)

        # Importado para pegar data e hora atual do sistema
        from datetime import datetime
        deactivate(cod, str(datetime.now()))

        print('\nPizza Desativada!')
        input('\nPressione enter para continuar...')

    except _sqlite3.OperationalError as error:
        print('\nNão foi possivel desativar a pizza!')
        print('Erro: ', error)
        input('\nPressione enter para continuar...')