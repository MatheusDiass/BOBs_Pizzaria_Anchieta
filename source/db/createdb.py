# Importa a função de conexão do arquivo de conexão
from source.db.connection import dbConnection

# Criação do Banco de Dados
def dbcreate():
    dict_connection = dbConnection()

    # Criação da tabela de clientes
    dict_connection['cursor'].execute('create table if not exists tblcustomer \
                   (cus_cod integer not null primary key, \
                   cus_name string(50), \
                   cus_address string(50), \
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
                   piz_type varchar(20), \
                   piz_price decimal(10,2), \
                   piz_inactivated integer, \
                   piz_inactdate datetime)')

    # Criação da tabela de tamanho de pizzas
    dict_connection['cursor'].execute('create table if not exists tblpizzasize \
                       (pis_cod integer not null primary key, \
                       pis_name varchar(20))')

    # Criação da tabela de pedidos
    dict_connection['cursor'].execute('create table if not exists tblorder \
                   (ord_cod integer not null primary key, \
                   ord_clicod integer, \
                   ord_datetime datetime, \
                   ord_totalorder decimal(10, 2), \
                   constraint fk_orderclient foreign key(ord_cliCod) references tblclient(cli_cod))')

    # Criação da tabela dos itens dos pedidos
    dict_connection['cursor'].execute('create table if not exists tblorderitems \
                   (oit_cod integer not null primary key, \
                   oit_ordercod integer not null, \
                   oit_pizzacod integer not null, \
                   oit_size int, \
                   oit_uniprice decimal(10, 2), \
                   oit_totalprice decimal(10, 2), \
                   constraint fk_orderitempizza foreign key(oit_ordercod) references tblorder(ord_cod), \
                   constraint fk_orderitempizza foreign key(oit_pizzacod) references tblpizza(piz_cod), \
                   constraint fk_orderitemsize foreign key(oit_size) references tblpizzasize(pis_cod))')

    # Insere algumas pizzas na tabela tblpizza
    list_pizza = [('Alho e Óleo', 'Alho frito picado, parmesão ralado e azeitonas', 'Salgada', 22.90, 0),
                  ('Allici', 'Alicci importado, rodelas de tomate, parmesão e azeitonas', 'Salgada', 28.90, 0),
                  ('Atum', 'Atum, cebola e azeitona', 'Salgada', 22.90, 0),
                  ('Bacon', 'Bacon coberto com muzzarela e azeitonas', 'Salgada', 26.90, 0),
                  ('Berinjela', 'Berinjela, cobertura com muzzarela, manjericão e parmesão', 'Salgada', 23.90, 0),
                  ('Caipira', 'Frango desfiado, coberto com catupiry, milho verde e azeitonas', 'Salgada', 26.90, 0),
                  ('Calabresa', 'Linguiça calabresa, cebola e azeitonas', 'Salgada', 19.90, 0),
                  ('Cinco Queijos', 'Muzzarela, parmesão, catupiry, gorgonzola e provolone', 'Salgada', '29.90', 0),
                  ('Escarola', 'Escarola refogada, muzzarela e azeitonas', 'Salgada', 24.90, 0),
                  ('Executiva', 'Milho verde, catupiry e azeitonas', 'Salgada', 22.90, 0),
                  ('Peruana', 'Atum, cebola, muzzarela e azeitonas', 'Salgada', 26.90, 0),
                  ('Palmito', 'Palmito com muzzarela e azeitonas', 'Salgada', 26.90, 0),
                  ('Banana', 'Banana fatiada com cobertura de leite condensado e canela em pó', 'Doce', 21.90, 0),
                  ('Brigadeiro', 'Chocolate, leite condensado e chocolate granulado', 'Doce', 23.90, 0),
                  ('Pestígio', 'Chocolate coberto com côco', 'Doce', 23.90, 0)]

    dict_connection['cursor'].executemany('insert into tblpizza(piz_name, piz_ingredients, piz_type, piz_price, piz_inactivated) \
                        values(?, ?, ?, ?, ?)', list_pizza)

    # Insere os tamanhos de pizza noa tabela tblpizzasize
    list_pizzasize = [('Médio',),
                      ('Grande',),
                      ('Gigante',)]

    dict_connection['cursor'].executemany('insert into tblpizzasize(pis_name) values(?)', list_pizzasize)

    dict_connection['connection'].commit()

# Chama a função de criação
dbcreate()