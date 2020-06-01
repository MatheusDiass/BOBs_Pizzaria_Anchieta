# Importa a função de conexão do arquivo de conexão
from source.db.connection import dbConnection

# Realiza o cadastro da pizza
def save(data_pizza):
    dict_connection = dbConnection()

    dict_connection['cursor'].execute('insert into tblpizza(piz_name,piz_ingredients, piz_type,  piz_price, piz_inactivated) \
                    values(?, ?, ?, ?, ?)', data_pizza)

    dict_connection['connection'].commit()

    dict_connection['cursor'].close()
    dict_connection['connection'].close()

# Atualiza o name
def updateName(cod, name):
    dict_connection = dbConnection()
    dict_connection['cursor'].execute('update tblpizza set piz_name = ? where piz_cod = ?', (name, cod))
    dict_connection['connection'].commit()

    dict_connection['cursor'].close()
    dict_connection['connection'].close()

# Atualiza os ingredientes
def updateIngredient(cod, ingredient):
    dict_connection = dbConnection()
    dict_connection['cursor'].execute('update tblpizza set piz_ingredients = ? where piz_cod = ?', (ingredient, cod))
    dict_connection['connection'].commit()

    dict_connection['cursor'].close()
    dict_connection['connection'].close()

# Atualiza o preço
def updatePrice(cod, price):
    dict_connection = dbConnection()
    dict_connection['cursor'].execute('update tblpizza set piz_price = ? where piz_cod = ?', (price, cod))
    dict_connection['connection'].commit()

    dict_connection['cursor'].close()
    dict_connection['connection'].close()

# Atualiza o tipo
def updateType(cod, type):
    dict_connection = dbConnection()
    dict_connection['cursor'].execute('update tblpizza set piz_type = ? where piz_cod = ?', (type, cod))
    dict_connection['connection'].commit()

    dict_connection['cursor'].close()
    dict_connection['connection'].close()

# Deleta a pizza
def delete(cod):
    dict_connection = dbConnection()
    dict_connection['cursor'].execute('delete from tblpizza piz_type where piz_cod = ?', (cod))
    dict_connection['connection'].commit()

    dict_connection['cursor'].close()
    dict_connection['connection'].close()

# Busca a pizza pelo código
def selectPizzaByCod(cod):
    dict_connection = dbConnection()
    dict_connection['cursor'].execute('select * from tblpizza where piz_cod = ?', (cod,))

    listPizzaByCod = dict_connection['cursor'].fetchone()

    dict_connection['cursor'].close()
    dict_connection['connection'].close()

    return listPizzaByCod

# Busca todas as pizzas junto de todas as suas informações
def selectAllPizzaInformation():
    dict_connection = dbConnection()
    dict_connection['cursor'].execute('select * from tblpizza')

    listAllPizzaInformation = dict_connection['cursor'].fetchall()

    dict_connection['cursor'].close()
    dict_connection['connection'].close()

    return listAllPizzaInformation

# Busca a pizza pelo código, selecionando os campos de código, nome, ingredientes, tipo e preço
def selectNameIngredientTypePrice(cod):
    dict_connection = dbConnection()
    dict_connection['cursor'].execute('select piz_cod, piz_name, piz_ingredients, piz_type, piz_price from tblpizza where piz_cod = ?', (cod,))

    listNameIngredientTypePrice = dict_connection['cursor'].fetchall()

    dict_connection['cursor'].close()
    dict_connection['connection'].close()

    return listNameIngredientTypePrice

# Busca o código das pizzas que o cliente já tenha feito o pedido alguma vez
def selectOrderedPizzas(cod):
    dict_connection = dbConnection()
    dict_connection['cursor'].execute('select piz_cod from tblpizza as p\
                                        join tblorderitems as i on i.oit_pizzacod = p.piz_cod \
                                        join tblorder as o on o.ord_cod = i.oit_ordercod \
                                        join tblcustomer as c on c.cus_cod = o.ord_clicod \
                                        where c.cus_cod = ?', (cod,))

    listpizzasNotOrdered = dict_connection['cursor'].fetchall()

    dict_connection['cursor'].close()
    dict_connection['connection'].close()

    return listpizzasNotOrdered

def selectAllPizzaInformation():
    dict_connection = dbConnection()
    dict_connection['cursor'].execute('select * from tblpizza')

    listAllPizzas = dict_connection['cursor'].fetchall()

    dict_connection['cursor'].close()
    dict_connection['connection'].close()

    return listAllPizzas

# Busca as pizzas que estão inativadas
def selectAllPizzaInactive():
    dict_connection = dbConnection()
    dict_connection['cursor'].execute('select * from tblpizza where piz_inactivated = 1')

    listAllPizzasInactivated = dict_connection['cursor'].fetchall()

    dict_connection['cursor'].close()
    dict_connection['connection'].close()

    return listAllPizzasInactivated

# Busca as pizzas que estão ativas
def selectAllPizzaActive():
    dict_connection = dbConnection()
    dict_connection['cursor'].execute('select * from tblpizza where piz_inactivated = 0')

    listAllPizzasNoInactivated = dict_connection['cursor'].fetchall()

    dict_connection['cursor'].close()
    dict_connection['connection'].close()

    return listAllPizzasNoInactivated

# Faz a contagem de quantas pizas estão cadastradas
def selectCountPizzas():
    dict_connection = dbConnection()
    dict_connection['cursor'].execute('select count(piz_cod) from tblpizza')

    countPizzas = dict_connection['cursor'].fetchone()

    dict_connection['cursor'].close()
    dict_connection['connection'].close()

    return countPizzas