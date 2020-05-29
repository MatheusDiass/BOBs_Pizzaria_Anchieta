# Importa a função de conexão do arquivo de conexão
from source.db.connection import dbConnection

# Salva o pedido
def saveOrder(codCustomer, datetime):
    dict_connection = dbConnection()

    dict_connection['cursor'].execute('insert into tblorder(ord_clicod, ord_datetime) \
                        values(?, ?)', (codCustomer, datetime))

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