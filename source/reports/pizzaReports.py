# Importa a função de relatório de pizza do arquivo da tabela tblpizza
from source.db.tblPizza import selectAllPizzaInformation

# Exibe o relatório de pizza
def allPizzaInformationReports():
    try:
        print('--------------------------------------------')
        print('\nRelatório de Clientes - Todos os Dados\n')

        listAllPizzaInformation = selectAllPizzaInformation()

        if len(listAllPizzaInformation) == 0:
            print('Não existem pizzas cadastradas!\n')

        else:
            for pizza in listAllPizzaInformation:
                print('Cod: ', pizza[0])
                print('Nome: ', pizza[1])
                print('Ingredientes: ', pizza[2])
                print('Tipo: ', pizza[3])
                print('Valor: ', pizza[4])

                if(pizza[5] == 1):
                    print('Data de Inatividade: ', pizza[6])

                print('\n')

        input('Pressione enter para continuar...')
    except:
        print('Não foi possivel acessar as pizzas')
        input('Pressione qualquer tecla para continuar...')