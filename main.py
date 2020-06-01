# Importa a função que limpa a tela
from source.actions.cleanAction import cleanScreem

# Importa as funções que exibe o cabeçalho e o menu principal do arquivo de menu principal
from source.menu.principalMenu import principal, headerMenu

# Importa a função que realiza a escolha das opções do menu principal
from source.option.principalOption import chooseOptionMenuPrincipal

def main():
    cleanScreem()
    headerMenu()
    principal()
    chooseOptionMenuPrincipal()

main()