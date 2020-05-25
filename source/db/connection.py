import _sqlite3

#Conexão com DB
def dbConnection():
    path = 'C:\\Users\Matheus Dias\Documents\Git_MyProjects\BOBs_Pizzaria_Anchieta\data\db_bobsPizzaria'
    connection = _sqlite3.connect(path)
    cursor = connection.cursor()
    dict_connection = {'connection': connection, 'cursor': cursor}
    return dict_connection