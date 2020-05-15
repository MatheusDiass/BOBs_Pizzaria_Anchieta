import _sqlite3

# Database creation
def DbCreate():
    connection = _sqlite3.connect('C:\\Users\Matheus Dias\Desktop\BOBs_Pizzaria_Projeto\data\db_bobsPizzaria')
    cursor = connection.cursor()

    # Create client table
    cursor.execute('create table if not exists tblclient \
                   cli_cod integer primary key\
                   cli_name varchar(50) \
                   cli_address varchar(50) \
                   cli_complement varchar(20) \
                   cli_district varchar(20) \
                   cli_city varchar(20) \
                   cli_uf varchar(2) \
                   cli_cep varchar(8) \
                   cli_phone varchar(10) \
                   cli_cellphone varchar(11)')

    # Create pizza table
    cursor.execute('create table if not exists tblpizza \
                   piz_cod integer primary key \
                   piz_name varchar(50) \
                   piz_ingredients varchar(70) \
                   piz_type varchar(20) \
                   piz_cost float \
                   piz_inactivated integer \
                   piz_inactivdate')