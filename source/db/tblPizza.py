import _sqlite3
from source.db.connection import dbConnection

def save(data_pizza):
    dict_connection = dbConnection()

    dict_connection['cursor'].execute('insert into tblpizza(piz_name,piz_ingredients, piz_type,  piz_price, piz_inactivated) \
                    values(?, ?, ?, ?, ?)', data_pizza)

    dict_connection['connection'].commit()

    dict_connection['cursor'].close()
    dict_connection['connection'].close()

def updateName(cod, name):
    dict_connection = dbConnection()
    dict_connection['cursor'].execute('update tblpizza set piz_name = ? where piz_cod = ?', (name, cod))
    dict_connection['connection'].commit()

    dict_connection['cursor'].close()
    dict_connection['connection'].close()

def updateIngredient(cod, ingredient):
    dict_connection = dbConnection()
    dict_connection['cursor'].execute('update tblpizza set piz_ingredients = ? where piz_cod = ?', (ingredient, cod))
    dict_connection['connection'].commit()

    dict_connection['cursor'].close()
    dict_connection['connection'].close()

def updatePrice(cod, price):
    dict_connection = dbConnection()
    dict_connection['cursor'].execute('update tblpizza set piz_price = ? where piz_cod = ?', (price, cod))
    dict_connection['connection'].commit()

    dict_connection['cursor'].close()
    dict_connection['connection'].close()

def updateType(cod, type):
    dict_connection = dbConnection()
    dict_connection['cursor'].execute('update tblpizza set piz_type = ? where piz_cod = ?', (type, cod))
    dict_connection['connection'].commit()

    dict_connection['cursor'].close()
    dict_connection['connection'].close()

def delete(cod):
    dict_connection = dbConnection()
    dict_connection['cursor'].execute('delete from tblpizza piz_type where piz_cod = ?', (cod))
    dict_connection['connection'].commit()

    dict_connection['cursor'].close()
    dict_connection['connection'].close()

def selectAllPizzaInformation():
    dict_connection = dbConnection()
    dict_connection['cursor'].execute('select * from tblpizza')

    listAllPizzaInformation = dict_connection['cursor'].fetchall()

    return listAllPizzaInformation