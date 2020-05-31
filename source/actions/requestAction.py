# Importa a função de limpar tela
from source.actions.cleanAction import cleanScreem
import os
import random
from datetime import datetime
from source.menu.principalMenu import headerMenu, principal
from source.db.tblCustomer import searchClientByPhone
from source.db.tblPizza import selectOrderedPizzas, selectNameIngredientTypePrice, selectCountPizzas, selectPizzaByCod
from source.db.tblOrder import saveOrder, selectCodOrder, updateTotal
from source.db.tblOrderItems import saveOrderItems

def request():
    count = 1
    total = 0
    verifyRequest = 0
    list_itensOrder = []

    clientPhone = str(input('Digite o telefone do cliente: '))
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
            os.system('cls' if os.name == 'nt' else 'clear')
            headerMenu()
            principal()

            # Importa o arquivo de opções do menu principal e a função que realiza a escolha
            from source.option.principalOption import chooseOptionMenuPrincipal
            chooseOptionMenuPrincipal()

    else:

        offerCustomersOtherFlavors(oneClient[0])

        saveOrder(oneClient[0], str(datetime.now()))

        qtdPizzas = int(input('Digite a quantidade de pizzas do pedido: '))

        while(count <= qtdPizzas):
            codPizza = int(input('Digite o codigo da pizza: '))

            listPizzaByCod = selectPizzaByCod(codPizza)

            while not listPizzaByCod:
                print('Pizza não encontrada!')
                codPizza = int(input('Digite o codigo da pizza novamente: '))
                listPizzaByCod = selectPizzaByCod(codPizza)

            print('\n[1] - Médio')
            print('[2] - Grande')
            print('[3] - Gigante')
            sizePizza = int(input('Digite o código do tamanho da pizza: '))

            while sizePizza < 1 or sizePizza > 3:
                print('\nCódigo inválido!')
                print('\n[1] - Médio')
                print('[2] - Grande')
                print('[3] - Gigante')
                sizePizza = int(input('Digite o código do tamanho da pizza novamente: '))

            else:

                uniPrice = listPizzaByCod[4]

                totalPrice = calculatePizzaValue(sizePizza, listPizzaByCod[4])

                codOrder = selectCodOrder()

                item = [codOrder[0], codPizza, sizePizza, uniPrice, totalPrice]

                list_itensOrder.append(item)

                total = total + totalPrice

                count += count

        updateTotal(codOrder[0], total)

        list_itensOrder = tuple(list_itensOrder)

        saveOrderItems(list_itensOrder)

        input('Pressione qualquer tecla para continuar...')

def offerCustomersOtherFlavors(cod):
    count = 0

    listpizzasNotOrdered = selectOrderedPizzas(cod)

    if not listpizzasNotOrdered:
        countPizzas = selectCountPizzas()

        print('\nPizzas á oferecer ao cliente\n')

        while count < 3:
            ran = random.randrange(1, countPizzas[0][0])

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
