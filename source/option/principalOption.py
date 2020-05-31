# Importa a função de limpar tela
from source.actions.cleanAction import cleanScreem

# Importa as funções que exibe o cabeçalho e o menu principal do arquivo de menu principal
from source.menu.principalMenu import headerMenu, principal

# Importa o arquivo que contem a função que realiza o pedido
from source.actions.requestAction import request

# Importa o arquivo que contem o menu de pizza
from source.menu.pizzaMenu import pizzaMenu

#Importa o arquivo que contem função de escolha das opções do menu de pizza
from source.option.pizzaOption import chooseOptionMenuPizza

# Importa o arquivo que contem o menu de cliente
from source.menu.customerMenu import customerMenu

# Importa o arquivo que contem a função de escolha das opções do menu de cliente
from source.option.customerOption import chooseOptionMenuClient

# De acordo com o número informado entra em uma das opções do menu principal
def chooseOptionMenuPrincipal():
    option = int(input('Escolha a opção desejada: '))

    while option < 1 or option > 4:
        print('Opção Inválida!')
        input('Pressione qualquer tecla para continuar...')
        cleanScreem()
        headerMenu()
        principal()
        option = int(input('Escolha a opção desejada: '))

    else:
        # Número 1 para realizar pedido
        if option == 1:
            request()

        # Número 3 para entrar no menu de pizza
        elif option == 3:
            cleanScreem()
            headerMenu()
            pizzaMenu()
            chooseOptionMenuPizza()

        # Número 4 para entrar no menu de cliente
        elif option == 4:
            cleanScreem()
            headerMenu()
            customerMenu()
            chooseOptionMenuClient()