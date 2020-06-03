# Importa a função de conexão do arquivo de conexão
from source.db.connection import dbConnection

# Busca todos os tipos de pizzas
def selectAllInformationTypePizza():
    dict_connection = dbConnection()
    dict_connection['cursor'].execute('select * from tblpizzatype')

    listAllTypePizzaInformation = dict_connection['cursor'].fetchall()

    dict_connection['cursor'].close()
    dict_connection['connection'].close()

    return listAllTypePizzaInformation

def selectCountTypePizza():
    dict_connection = dbConnection()
    dict_connection['cursor'].execute('select count(pit_cod) from tblpizzatype')

    listAllTypePizzaInformation = dict_connection['cursor'].fetchone()

    dict_connection['cursor'].close()
    dict_connection['connection'].close()

    return listAllTypePizzaInformation