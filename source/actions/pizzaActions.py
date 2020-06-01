# Importa as funções do arquivo da tabela tblpizza para interagir com o banco de dados
from source.db.tblPizza import save, updateName, updateIngredient, updatePrice, updateType, delete

# Importa as funções de validação do arquivo de validação do cliente
from source.validation.pizzaValidation import nameValidation, ingredientValidation, typeValidation, priceValidation

# Salva a pizza no banco de dados e trata a exceção caso ocorrer algum erro
def pizzaRegister():
    print('\nCadastro de pizza\n')

    name = str(input('Digite o nome: '))
    name = nameValidation(name)

    ingredient = str(input('Digite os ingredientes: '))
    ingredient = ingredientValidation(ingredient)

    type = str(input('Digite o tipo: '))
    type = typeValidation(type)

    price = input('Digite o valor: ')
    price = priceValidation(price)

    inactvated = 0

    data_pizza = ([name, ingredient, type , price, inactvated])

    try:
        save(data_pizza)
        print('\nPizza salva com sucesso!\n')
        input('Pressione qualquer tecla para continuar...')
    except:
        print('\nOcorreu um erro ao cadastrar a pizza.')
        print('Contate o administrador.\n')
        input('Pressione qualquer tecla para continuar...')

# Atualiza as informações da pizza de acordo com o número selecinado
def update(option):

    # Número 1 para atualizar o nome
    if option == 1:
        print('\nAtualizar Nome\n')

        cod = int(input('Digite o código da pizza: '))
        name = str(input('Digite o novo nome para a pizza: '))

        try:
            updateName(cod, name)
            print('\nNome da pizza atualizado com sucesso\n')
            input('Pressione qualquer tecla para continuar...')
        except:
            print('\nNão foi possivel executar a alteração...\n')
            input('Pressione qualquer tecla para continuar...')

    # Número 2 para atualizar os ingredientes
    elif option == 2:
        print('\nAtualizar ingredientes\n')
        cod = int(input('Digite o código da pizza: '))
        ingredient = str(input('Digite os novos ingredientes para a pizza: '))

        try:
            updateIngredient(cod, ingredient)
            print('\nIngredientes da pizza atualizados com sucesso\n')
            input('Pressione qualquer tecla para continuar...')
        except:
            print('\nNão foi possivel executar a alteração...\n')
            input('Pressione qualquer tecla para continuar...')

    # Número 3 para atualizar o valor
    elif option == 3:
        print('\nAtualizar Valor\n')
        cod = int(input('Digite o código da pizza: '))
        price = int(input('Digite o novo valor para a pizza: '))

        try:
            updatePrice(cod, price)
            print('\nValor da pizza atualizado com sucesso\n')
            input('Pressione qualquer tecla para continuar...')
        except:
            print('\nNão foi possivel executar a alteração...\n')
            input('Pressione qualquer tecla para continuar...')

    # Número 4 para atualizar o tipo
    elif option == 4:
        print('\nAtualizar Tipo\n')
        cod = int(input('Digite o código da pizza: '))
        type = str(input('Digite o novo tipo para a pizza: '))

        try:
            updateType(cod, type)
            print('\nTipo da pizza atualizado com sucesso\n')
            input('Pressione qualquer tecla para continuar...')
        except:
            print('\nNão foi possivel executar a alteração...\n')
            input('Pressione qualquer tecla para continuar...')

# Deleta a pizza do banco de dados
def delete(cod):
    try:
        delete(cod)
        print('Pizza deletada')
        input('\nPressione qualquer tecla para continuar...\n')
    except:
        print('\nNão foi possivel executar a alteração...\n')
        input('Pressione qualquer tecla para continuar...')