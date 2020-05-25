from source.db.tblPizza import save, updateName, updateIngredient, updatePrice, updateType, delete, selectAllPizzaInformation

def pizzaRegister():
    print('\nCadastro de pizza\n')

    name = str(input('Digite o nome: '))

    type = str(input('Digite o tipo: '))

    ingredient = str(input('Digite os ingredientes: '))

    price = float(input('Digite o valor: '))

    inactvated = 0

    data_pizza = ([name, ingredient, type , price, inactvated])

    try:
        save(data_pizza)
        print('\nPizza salva com sucesso!\n')
        input('Pressione qualquer tecla para continuar...')
    except:
        print('Ocorreu um erro ao cadastrar a pizza.')
        print('Contate o administrador.\n')
        input('Pressione qualquer tecla para continuar...')

def update(option):

    if option == 1:
        print('\nAtualizar Nome\n')

        cod = int(input('Digite o código da pizza: '))
        name = str(input('Digite o novo nome para a pizza: '))

        try:
            updateName(cod, name)
            print('Nome da pizza atualizado com sucesso\n')
            input('Pressione qualquer tecla para continuar...')
        except:
            print('Não foi possivel executar a alteração...')
            input('Pressione qualquer tecla para continuar...') 

    elif option == 2:
        print('\nAtualizar ingredientes\n')
        cod = int(input('Digite o código da pizza: '))
        ingredient = str(input('Digite os novos ingredientes para a pizza: '))

        try:
            updateIngredient(cod, ingredient)
            print('Ingredientes da pizza atualizados com sucesso\n')
            input('Pressione qualquer tecla para continuar...')
        except:
            print('Não foi possivel executar a alteração...')
            input('Pressione qualquer tecla para continuar...')
    
    elif option == 3:
        print('\nAtualizar Valor\n')
        cod = int(input('Digite o código da pizza: '))
        price = int(input('Digite o novo valor para a pizza: '))

        try:
            updatePrice(cod, price)
            print('Valor da pizza atualizado com sucesso\n')
            input('Pressione qualquer tecla para continuar...')
        except:
            print('Não foi possivel executar a alteração...')
            input('Pressione qualquer tecla para continuar...')

    elif option == 4:
        print('\nAtualizar Tipo\n')
        cod = int(input('Digite o código da pizza: '))
        type = str(input('Digite o novo tipo para a pizza: '))

        try:
            updateType(cod, type)
            print('Tipo da pizza atualizado com sucesso\n')
            input('Pressione qualquer tecla para continuar...')
        except:
            print('Não foi possivel executar a alteração...')
            input('Pressione qualquer tecla para continuar...')

def delete(cod):
    try:
        delete(cod)
        print('Pizza deletada')
        input('Pressione qualquer tecla para continuar...')
    except:
        print('Não foi possivel executar a alteração...')
        input('Pressione qualquer tecla para continuar...')







