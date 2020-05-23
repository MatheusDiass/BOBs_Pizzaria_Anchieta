from source.db.tblPizza import save, updateNomePizza, updateIngredientesPizza, updateValorPizza, updateTipoPizza, deletarPizza, consultaListaPizzas

def pizzaRegister():
    print('\nCadastro de nova pizza\n')

    tipo = str(input('Digite o tipo: '))

    name = str(input('Digite o nome: '))

    ingrediente = str(input('Digite os ingredientes: '))

    valor = str(input('Digite o valor: '))

    data_pizza = ([name, ingrediente, tipo , valor])

    try:
        save(data_pizza)
        print('\nPizza salva com sucesso!\n')
        input('Pressione qualquer tecla para continuar...')
    except:
        print('Ocorreu um erro ao cadastrar a pizza.')
        print('Contate o administrador.\n')
        input('Pressione qualquer tecla para continuar...')

def updatePizza(option):

    if option == 1:
        print('\nAtualizar Nome\n')

        cod = int(input('Digite o código da pizza: '))
        nome = str(input('Digite o novo nome para a pizza: '))

        try:
            updateNomePizza(cod,nome)
            print('Nome da pizza atualizado com sucesso\n')
            input('Pressione qualquer tecla para continuar...')
        except:
            print('Não foi possivel executar a alteração...')
            input('Pressione qualquer tecla para continuar...') 

    elif option == 2:
        print('\nAtualizar ingredientes\n')
        cod = int(input('Digite o código da pizza: '))
        ingredientes = str(input('Digite os novos ingredientes para a pizza: '))

        try:
            updateIngredientesPizza(cod,ingredientes)
            print('Ingredientes da pizza atualizados com sucesso\n')
            input('Pressione qualquer tecla para continuar...')
        except:
            print('Não foi possivel executar a alteração...')
            input('Pressione qualquer tecla para continuar...')
    
    elif option == 3:
        print('\nAtualizar Valor\n')
        cod = int(input('Digite o código da pizza: '))
        valor = int(input('Digite o novo valor para a pizza: '))

        try:
            updateValorPizza(cod,valor)
            print('Valor da pizza atualizado com sucesso\n')
            input('Pressione qualquer tecla para continuar...')
        except:
            print('Não foi possivel executar a alteração...')
            input('Pressione qualquer tecla para continuar...')

    elif option == 4:
        print('\nAtualizar Tipo\n')
        cod = int(input('Digite o código da pizza: '))
        tipo = str(input('Digite o novo tipo para a pizza: '))

        try:
            updateTipoPizza(cod,tipo)
            print('Tipo da pizza atualizado com sucesso\n')
            input('Pressione qualquer tecla para continuar...')
        except:
            print('Não foi possivel executar a alteração...')
            input('Pressione qualquer tecla para continuar...')

def deletarPizza(cod):
    try:
        deletarCod(cod)
        print('Pizza deletada')
        input('Pressione qualquer tecla para continuar...')
    except:
        print('Não foi possivel executar a alteração...')
        input('Pressione qualquer tecla para continuar...')

def consultaListaPizzas():
    try:
        lista = todasPizzas()
        print('\nPizzas\n')
        for piz in lista:
            print('Cod: ',piz[0])
            print('Nome: ',piz[1])
            print('Ingredientes: ',piz[2])
            print('Tipo: ',piz[3])
            print('Valor: ',piz[4])
            print('Data Inatividade: ',piz[5])
            print('Data Criação: ',piz[6])
        input('Pressione qualquer tecla para continuar...')
    except:
        print('Não foi possivel acessar as pizzas')
        input('Pressione qualquer tecla para continuar...')







