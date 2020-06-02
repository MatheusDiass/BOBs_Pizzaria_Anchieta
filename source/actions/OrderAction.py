# Import sqlite3 para tratar os erros
import _sqlite3

# Importa a função que limpa a tela
from source.actions.cleanAction import cleanScreem

# Importado para gerar números aleatórios
import random

# Importado para pegar data e hora atual do sistema
from datetime import datetime

# Importa as funções que exibe o cabeçalho e o menu principal do arquivo de menu principal
from source.menu.principalMenu import headerMenu, principal

# Importa algumas funções para utilização das pizzas
from source.db.tblPizza import selectOrderedPizzas, selectNameIngredientTypePrice, selectCountPizzas, selectPizzaByCod

# Importa funções para salvar, selecionar, atualizar e deletar pedido
from source.db.tblOrder import saveOrder, selectCodOrder, updateTotal, deleteOrder

# Função para realizar pedido
def request():
    count = 0
    total = 0
    list_itensOrder = []
    namePizzas = []

    clientPhone = str(input('Digite o telefone do cliente: '))

    # Importa função para buscar cliente pelo número de telefone
    from source.db.tblCustomer import searchClientByPhone
    oneClient = searchClientByPhone(clientPhone)

    while not oneClient:
        print('\nCliente não encontrado!')
        resp = str(input('Deseja fazer a busca novamente (S/N) ?'))
        resp = resp.upper()

        while 'S' != resp != 'N':
            print('\nResposta incorreta!')
            resp = str(input('Deseja fazer a busca novamente (S/N) ?'))
            resp = resp.upper()

        else:
            if resp == 'S':
                clientPhone = str(input('Digite o telefone do cliente: '))
                oneClient = searchClientByPhone(clientPhone)

        if resp == 'N':
            cleanScreem()
            headerMenu()
            principal()

            # Importa a função que realiza a escolha das opções do menu principal
            from source.option.principalOption import chooseOptionMenuPrincipal
            chooseOptionMenuPrincipal()

    else:

        offerCustomersOtherFlavors(oneClient[0])

        # Cria o pedido no banco de dados
        saveOrder(oneClient[0], str(datetime.now().date()), str(datetime.now().time()))

        qtdPizzas = input('Digite a quantidade de pizzas do pedido: ')

        # Valida se apenas números foram digitados
        while not qtdPizzas.isnumeric():
            print('A quantidade de pizzas não pode conter letras!')
            qtdPizzas = input('Digite a quantidade de pizzas do pedido novamente: ')

        qtdPizzas = int(qtdPizzas)

        # Realiza um loop com base na quantidade pizza pedida pelo usúario
        while(count < qtdPizzas):
            codPizza = input('Digite o codigo da pizza: ')

            # Valida se apenas números foram digitados
            while not codPizza.isnumeric():
                print('O código da pizza não pode conter letras!')
                codPizza = input('Digite o codigo da pizza novamente: ')

            codPizza = int(codPizza)

            listPizzaByCod = selectPizzaByCod(codPizza)

            while not listPizzaByCod:
                print('Pizza não encontrada!')
                codPizza = int(input('Digite o codigo da pizza novamente: '))
                listPizzaByCod = selectPizzaByCod(codPizza)

            print('\n')
            namePizzas.append(listPizzaByCod[1])

            print('\n[1] - Médio')
            print('[2] - Grande')
            print('[3] - Gigante')
            sizePizza = input('Digite o código do tamanho da pizza: ')

            # Valida se apenas números foram digitado
            while not sizePizza.isnumeric():
                print('O código do tamanho só pode conter números!')
                sizePizza = input('Digite o código do tamanho da pizza novamente: ')

            sizePizza = int(sizePizza)

            print('\n')

            while sizePizza < 1 or sizePizza > 3:
                print('\nCódigo inválido!')
                print('\n[1] - Médio')
                print('[2] - Grande')
                print('[3] - Gigante')
                sizePizza = int(input('Digite o código do tamanho da pizza novamente: '))
                print('\n')

            else:

                # Recebe o preço unitário da pizza
                uniPrice = listPizzaByCod[4]

                # Calcula o total da pizza
                totalPrice = calculatePizzaValue(sizePizza, listPizzaByCod[4])

                # Recebe código do pedido, busca realizada no banco
                codOrder = selectCodOrder()

                item = [codOrder[0], codPizza, sizePizza, uniPrice, totalPrice]

                list_itensOrder.append(item)

                # Recebe o total somando todos os itens
                total = total + totalPrice

                count += 1

        # Exibe na tela o total do pedido
        print('')
        print('----------------------')
        print('- Total: {:.2f}'.format(total))
        print('----------------------')

        customerMoney = input('Digite o valor em dinheiro que o clinete irá entregar: ')

        # Valida se apenas números foram digitados
        while not customerMoney.isnumeric():
            print('Valor inválido!')
            customerMoney = input('Digite o valor em dinheiro que o clinete ira entregar novamente: ')

        customerMoney = float(customerMoney)

        while customerMoney < total:
            print('O valor digitado não pode ser menor que o total do pedido!')
            customerMoney = float(input('Digite o valor em dinheiro que o cliete ira entregar novamente: '))

        # Armazena o troco do pedido
        rest = customerMoney - total

        # Atualiza o total no pedido do cliente
        updateTotal(codOrder[0], total)

        list_itensOrder = tuple(list_itensOrder)

        # Importa função para salvar os itens do pedido
        from source.db.tblOrderItems import saveOrderItems

        # Salva os itens
        saveOrderItems(list_itensOrder)

        # Exibe na tela a nota do pedido
        print('\n')
        print('-'*55)
        print('- Nota\n')
        print('- Código do Pedido:', codOrder[0])
        print('- Nome do Cliente:', oneClient[1])

        for name in namePizzas:
            print('- Item:', name)

        print('- Valor total: {:.2f}'.format(total))
        print('- Troco: {:.2f}'.format(rest))
        print('-' * 55)

        input('\nPressione qualquer tecla para continuar...')

def offerCustomersOtherFlavors(cod):
    count = 0

    listpizzasNotOrdered = selectOrderedPizzas(cod)

    if not listpizzasNotOrdered:
        countPizzas = selectCountPizzas()

        print('\nPizzas á oferecer ao cliente\n')

        while count < 3:
            ran = random.randrange(1, countPizzas[0])

            listNameIngredientTypePrice = selectNameIngredientTypePrice(ran)

            for pizza in listNameIngredientTypePrice:
                print('Cod: ', pizza[0])
                print('Nome: ', pizza[1])
                print('Ingredientes: ', pizza[2])
                print('Tipo: ', pizza[3])
                print('Valor: ', pizza[4])
                print('\n')

            count += 1

        input('Pressione qualquer tecla para continuar...')

def calculatePizzaValue(sizePizza, price):
    if sizePizza == 1:
        uniprice = price + (price * 0.15)

    elif sizePizza == 2:
        uniprice = price + (price * 0.25)

    elif sizePizza == 3:
        uniprice = price + (price * 0.35)

    return uniprice

def delete():
    try:
        cod = input('Digite o código do pedido:  ')

        while not cod.isnumeric():
            print('Código Inválido!')
            cod = input('Digite o código do pedido novamente: ')

        cod = int(cod)

        # Importa função para deletar os itens do pedido
        from source.db.tblOrderItems import deleteOrderItems
        deleteOrderItems(cod)
        deleteOrder(cod)

        print('\nPedido Deletado!')
        input('\nPressione enter para continuar...')

    except _sqlite3.OperationalError as error:
        print('\nNão foi possivel buscar os clientes')
        print('Erro: ', error)
        input('\nPressione enter para continuar...')
