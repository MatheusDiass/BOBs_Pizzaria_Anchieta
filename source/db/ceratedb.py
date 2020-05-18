import _sqlite3

# Database creation
def DbCreate():
    connection = _sqlite3.connect('C:\\Users\Matheus Dias\Desktop\BOBs_Pizzaria_Projeto\data\db_bobsPizzaria')
    cursor = connection.cursor()

    # Create client table
    cursor.execute('create table if not exists tblclient \
                   cli_cod integer primary key\
                   cli_name string(50) \
                   cli_address string(50) \
                   cli_complement string(20) \
                   cli_district string(20) \
                   cli_city string(20) \
                   cli_uf string(2) \
                   cli_cep string(8) \
                   cli_phone string(10) \
                   cli_cellphone string(11)')

    # Create pizza table
    cursor.execute('create table if not exists tblpizza \
                   piz_cod integer primary key \
                   piz_name varchar(50) \
                   piz_ingredients varchar(70) \
                   piz_type varchar(20) \
                   piz_cost float \
                   piz_inactivated integer \
                   piz_inactivdate')