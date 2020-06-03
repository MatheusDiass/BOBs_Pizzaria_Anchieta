# Importado para verificar se arquivo existe
import os

# Importa a função de conexão e o caminho para conexão
from source.db.connection import dbConnection

# Criação do Banco de Dados
def dbcreate():
    dict_connection = dbConnection()

    nameTableCustomer = verifyTableCustomer()
    nameTablePizza = verifyTablePizza()
    nameTableOrder = verifyTableOrder()
    nameTableItems = verifyTableItems()

    if not nameTableCustomer and not nameTablePizza and not nameTableOrder and not nameTableItems:

        # Criação da tabela de clientes
        dict_connection['cursor'].execute('create table if not exists tblcustomer \
                    (cus_cod integer not null primary key, \
                    cus_name string(50), \
                    cus_address string(50), \
                    cus_number int, \
                    cus_complement string(20), \
                    cus_district string(20), \
                    cus_city string(20), \
                    cus_uf string(2), \
                    cus_cep string(9), \
                    cus_phone string(14), \
                    cus_cellphone string(13))')

        # Criação da tabela de pizzas
        dict_connection['cursor'].execute('create table if not exists tblpizza \
                    (piz_cod integer not null primary key, \
                    piz_name varchar(50), \
                    piz_ingredients text, \
                    piz_price decimal(10,2), \
                    piz_inactivated integer, \
                    piz_inactdate datetime, \
                    piz_typecod integer, \
                    constraint fk_pizzatype foreign key(piz_typecod) references tblpizzatype(pit_cod))')

        # Criação da tabela de tipos de pizza
        dict_connection['cursor'].execute('create table if not exists tblpizzatype \
                                          (pit_cod integer not null primary key, \
                                           pit_name varchar(20))')

        # Criação da tabela de tamanho de pizzas
        dict_connection['cursor'].execute('create table if not exists tblpizzasize \
                       (pis_cod integer not null primary key, \
                       pis_name varchar(20))')

        # Criação da tabela de pedidos
        dict_connection['cursor'].execute('create table if not exists tblorder \
                    (ord_cod integer not null primary key, \
                    ord_clicod integer, \
                    ord_date date, \
                    ord_time time, \
                    ord_totalorder float(10, 2), \
                    constraint fk_orderclient foreign key(ord_cliCod) references tblclient(cli_cod))')

        # Criação da tabela dos itens dos pedidos
        dict_connection['cursor'].execute('create table if not exists tblorderitems \
                    (oit_cod integer not null primary key, \
                    oit_ordercod integer not null, \
                    oit_pizzacod integer not null, \
                    oit_size int, \
                    oit_uniprice float(10, 2), \
                    oit_totalprice float(10, 2), \
                    constraint fk_orderitempizza foreign key(oit_ordercod) references tblorder(ord_cod), \
                    constraint fk_orderitempizza foreign key(oit_pizzacod) references tblpizza(piz_cod), \
                    constraint fk_orderitemsize foreign key(oit_size) references tblpizzasize(pis_cod))')

        # Insere algumas pizzas na tabela tblpizza
        list_pizza = [('Alho e Óleo', 'Alho frito picado, parmesão ralado e azeitonas', 22.90, 0, 1),
                      ('Allici', 'Alicci importado, rodelas de tomate, parmesão e azeitonas', 28.90, 0, 1),
                      ('Atum', 'Atum, cebola e azeitona', 22.90, 0, 1),
                      ('Bacon', 'Bacon coberto com muzzarela e azeitonas', 26.90, 0, 1),
                      ('Berinjela', 'Berinjela, cobertura com muzzarela, manjericão e parmesão', 23.90, 0, 1),
                      ('Caipira', 'Frango desfiado, coberto com catupiry, milho verde e azeitonas', 26.90, 0, 1),
                      ('Calabresa', 'Linguiça calabresa, cebola e azeitonas', 19.90, 0, 1),
                      ('Cinco Queijos', 'Muzzarela, parmesão, catupiry, gorgonzola e provolone', 29.90, 0, 1),
                      ('Escarola', 'Escarola refogada, muzzarela e azeitonas', 24.90, 0, 1),
                      ('Executiva', 'Milho verde, catupiry e azeitonas', 22.90, 0, 1),
                      ('Peruana', 'Atum, cebola, muzzarela e azeitonas', 26.90, 0, 1),
                      ('Palmito', 'Palmito com muzzarela e azeitonas', 26.90, 0, 1),
                      ('Banana', 'Banana fatiada com cobertura de leite condensado e canela em pó', 21.90, 0, 2),
                      ('Brigadeiro', 'Chocolate, leite condensado e chocolate granulado', 23.90, 0, 2),
                      ('Prestígio', 'Chocolate coberto com côco', 23.90, 0, 2)]

        dict_connection['cursor'].executemany('insert into tblpizza(piz_name, piz_ingredients, piz_price, piz_inactivated, piz_typecod) \
                        values(?, ?, ?, ?, ?)', list_pizza)

        # Insere os tipos de pizza na tabela tblpizzatype
        list_pizzatype = [('Salgada',),
                          ('Doce',)]

        dict_connection['cursor'].executemany('insert into tblpizzatype(pit_name) values(?)', list_pizzatype)

        # Insere os tamanhos de pizza na tabela tblpizzasize
        list_pizzasize = [('Médio',),
                          ('Grande',),
                          ('Gigante',)]

        dict_connection['cursor'].executemany('insert into tblpizzasize(pis_name) values(?)', list_pizzasize)

        dict_connection['connection'].commit()

        print('\nBanco de dados criado com sucesso!\n')
        input('Pressione enter para continuar...')

    else:
        print('\nBanco de dados já existe!\n')
        input('Pressione enter para continuar...')

# Verifica se a tabela de cliente existe
def verifyTableCustomer():
    dict_connection = dbConnection()
    dict_connection['cursor'].execute("select name from sqlite_master where type='table' AND name='tblcustomer'")

    nameTable = dict_connection['cursor'].fetchone()

    dict_connection['cursor'].close()
    dict_connection['connection'].close()

    return nameTable

# Verifica se a tabela de pizza existe
def verifyTablePizza():
    dict_connection = dbConnection()
    dict_connection['cursor'].execute("select name from sqlite_master where type='table' AND name='tblpizza'")

    nameTable = dict_connection['cursor'].fetchone()

    dict_connection['cursor'].close()
    dict_connection['connection'].close()

    return nameTable

# Verifica se a tabela de pedidos existe
def verifyTableOrder():
    dict_connection = dbConnection()
    dict_connection['cursor'].execute("select name from sqlite_master where type='table' AND name='tblorder'")

    nameTable = dict_connection['cursor'].fetchone()

    dict_connection['cursor'].close()
    dict_connection['connection'].close()

    return nameTable

# Verifica se a tabela de itens do pedido existe
def verifyTableItems():
    dict_connection = dbConnection()
    dict_connection['cursor'].execute("select name from sqlite_master where type='table' AND name='tblorderitems'")

    nameTable = dict_connection['cursor'].fetchone()

    dict_connection['cursor'].close()
    dict_connection['connection'].close()

    return nameTable