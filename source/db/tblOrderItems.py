# Importa a função de conexão do arquivo de conexão
from source.db.connection import dbConnection

# Salva todos os itens do pedido do cliente
def saveOrderItems(data_orderItens):
    dict_connection = dbConnection()

    dict_connection['cursor'].executemany('insert into tblorderitems(oit_ordercod, oit_pizzacod, oit_size, oit_uniprice, oit_totalprice) \
                            values(?, ?, ?, ?, ?)', data_orderItens)

    dict_connection['connection'].commit()

    dict_connection['cursor'].close()
    dict_connection['connection'].close()