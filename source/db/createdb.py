import _sqlite3


# Database creation
def dbcreate():
    path = 'C:\\Users\Matheus Dias\Documents\GitHub_MyProjects\BOBs_Pizzaria_Anchieta\data\db_bobsPizzaria'
    connection = _sqlite3.connect(path)
    cursor = connection.cursor()

    # Create client table
    cursor.execute('create table if not exists tblclient \
                   (cli_cod integer not null primary key, \
                   cli_name string(50), \
                   cli_address string(50), \
                   cli_complement string(20), \
                   cli_district string(20), \
                   cli_city string(20), \
                   cli_uf string(2), \
                   cli_cep string(8), \
                   cli_phone string(10), \
                   cli_cellphone string(11))')

    # Create pizza table
    cursor.execute('create table if not exists tblpizza \
                   (piz_cod integer not null primary key, \
                   piz_name varchar(50), \
                   piz_ingredients text, \
                   piz_type varchar(20), \
                   piz_price decimal(10,2), \
                   piz_inactivated integer, \
                   piz_inactdate datetime)')

    # Create order table
    cursor.execute('create table if not exists tblorder \
                   (ord_cod integer not null primary key, \
                   ord_clicod integer, \
                   ord_date date, \
                   ord_time time, \
                   ord_totalorder decimal(10, 2), \
                   constraint fk_orderclient foreign key(ord_cliCod) references tblclient(cli_cod))')

    # Create Order Items table
    cursor.execute('create table if not exists tblorderitems \
                   (oit_cod integer not null, \
                   oit_ordercod integer not null, \
                   oit_pizzacod integer not null, \
                   oit_size string(10), \
                   oit_uniprice decimal(10, 2), \
                   oit_totalprice decimal(10, 2), \
                   constraint fk_orderitem primary key(oit_cod, oit_ordercod), \
                   constraint fk_orderitempizza foreign key(oit_pizzacod) references tblpizza(piz_cod))')

    # Add data to the pizza table
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

    cursor.executemany('insert into tblpizza(piz_name, piz_ingredients, piz_type, piz_price, piz_inactivated) \
                        values(?, ?, ?, ?, ?)', list_pizza)

    connection.commit()

dbcreate()