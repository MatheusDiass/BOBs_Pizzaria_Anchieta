import sqlite3

def dbConnection():
    path = 'C:\\Users\Matheus Dias\Documents\GitHub_MyProjects\BOBs_Pizzaria_Anchieta\data\db_bobsPizzaria'
    connection = _sqlite3.connect(path)
    cursor = connection.cursor()
    dict_connection = {'connection':connection, 'cursor':cursor}
    return dict_connection

def save(cadastro):
    dict_connection = dbConnection()

    dict_connection['cursor'].execute('insert into tblpizza(piz_name,piz_ingredients, piz_type,  piz_price, piz_inactivated) \
                    values(?, ?, ?, ?, ?)', cadastro)

    dict_connection['connection'].commit()

    dict_connection['cursor'].close()
    dict_connection['connection'].close()

def updateNomePizza(cod,nome):
    dict_connection = dbConnection()
    dict_connection['cursor'].execute('update tblpizza set piz_name = ? where piz_cod = ?', (name, cod))
    dict_connection['connection'].commit()

    dict_connection['cursor'].close()
    dict_connection['connection'].close()

def updateIngredientesPizza(cod,ingrediente):
    dict_connection = dbConnection()
    dict_connection['cursor'].execute('update tblpizza set piz_ingredients = ? where piz_cod = ?', (ingrediente, cod))
    dict_connection['connection'].commit()

    dict_connection['cursor'].close()
    dict_connection['connection'].close()

def updateValorPizza(cod,valor):
    dict_connection = dbConnection()
    dict_connection['cursor'].execute('update tblpizza set piz_price = ? where piz_cod = ?', (valor, cod))
    dict_connection['connection'].commit()

    dict_connection['cursor'].close()
    dict_connection['connection'].close()

def updateTipoPizza(cod,tipo):
    dict_connection = dbConnection()
    dict_connection['cursor'].execute('update tblpizza set piz_type = ? where piz_cod = ?', (tipo, cod))
    dict_connection['connection'].commit()

    dict_connection['cursor'].close()
    dict_connection['connection'].close()

def deletarPizza(cod):
    dict_connection = dbConnection()
    dict_connection['cursor'].execute('delete from tblpizza piz_type where piz_cod = ?', (cod))
    dict_connection['connection'].commit()

    dict_connection['cursor'].close()
    dict_connection['connection'].close()

def consultaListaPizzas():
    dict_connection = dbConnection()
    dict_connection['cursor'].execute('select * from tblpizza')

    listAllPizza = dict_connection['cursor'].fetchall()

    return listAllPizza