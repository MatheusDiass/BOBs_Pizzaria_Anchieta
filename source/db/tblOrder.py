# Importa a função de conexão do arquivo de conexão
from source.db.connection import dbConnection

# Salva o pedido
def saveOrder(codCustomer, date, time):
    dict_connection = dbConnection()

    dict_connection['cursor'].execute('insert into tblorder(ord_clicod, ord_date, ord_time) \
                        values(?, ?, ?)', (codCustomer, date, time))

    dict_connection['connection'].commit()

    dict_connection['cursor'].close()
    dict_connection['connection'].close()

# Atualiza o total do pedido
def updateTotal(cod, total):
    dict_connection = dbConnection()
    dict_connection['cursor'].execute('update tblorder set ord_totalorder = ? where ord_cod = ?', (total, cod))
    dict_connection['connection'].commit()

    dict_connection['cursor'].close()
    dict_connection['connection'].close()

# Busca o código do último pedido cadastrado
def selectCodOrder():
    dict_connection = dbConnection()

    dict_connection['cursor'].execute('select ord_cod from tblorder order by ord_cod desc limit 1')

    codOrder = dict_connection['cursor'].fetchone()

    dict_connection['cursor'].close()
    dict_connection['connection'].close()

    return codOrder

def selectAllOrderInformation():
    dict_connection = dbConnection()
    dict_connection['cursor'].execute('select o.ord_cod, o.ord_date, c.cus_name, o.ord_totalorder from tblorder as o \
                                       join tblcustomer as c on c.cus_cod = o.ord_clicod ')

    listAllOrder = dict_connection['cursor'].fetchall()

    dict_connection['cursor'].close()
    dict_connection['connection'].close()

    return listAllOrder