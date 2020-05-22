import _sqlite3

def dbConnection():
    path = 'C:\\Users\Matheus Dias\Documents\GitHub_MyProjects\BOBs_Pizzaria_Anchieta\data\db_bobsPizzaria'
    connection = _sqlite3.connect(path)
    cursor = connection.cursor()
    dict_connection = {'connection':connection, 'cursor':cursor}
    return dict_connection


# Cadastre of the clients
def save(data_client):
    dict_connection = dbConnection()
    dict_connection['cursor'].execute('insert into tblclient(cli_name, cli_address, cli_complement, cli_district, cli_city, cli_uf, cli_cep, cli_phone, cli_cellphone) \
                    values(?, ?, ?, ?, ?, ?, ?, ?, ?)', data_client)

    dict_connection['connection'].commit()

    dict_connection['cursor'].close()
    dict_connection['connection'].close()

def updateName(cod, name):
    dict_connection = dbConnection()
    dict_connection['cursor'].execute('update tblclient set cli_name = ? where cli_cod = ?', (name, cod))
    dict_connection['connection'].commit()

    dict_connection['cursor'].close()
    dict_connection['connection'].close()

def updateAddress(cod, address):
    dict_connection = dbConnection()
    dict_connection['cursor'].execute('update tblclient set cli_address = ? where cli_cod = ?', (address, cod))
    dict_connection['connection'].commit()

    dict_connection['cursor'].close()
    dict_connection['connection'].close()

def updateComplement(cod, complement):
    dict_connection = dbConnection()
    dict_connection['cursor'].execute('update tblclient set cli_complement = ? where cli_cod = ?', (complement, cod))
    dict_connection['connection'].commit()

    dict_connection['cursor'].close()
    dict_connection['connection'].close()

def updateDistrict(cod, district):
    dict_connection = dbConnection()
    dict_connection['cursor'].execute('update tblclient set cli_district = ? where cli_cod = ?', (district, cod))
    dict_connection['connection'].commit()

    dict_connection['cursor'].close()
    dict_connection['connection'].close()

def updateCity(cod, city):
    dict_connection = dbConnection()
    dict_connection['cursor'].execute('update tblclient set cli_city = ? where cli_cod = ?', (city, cod))
    dict_connection['connection'].commit()

    dict_connection['cursor'].close()
    dict_connection['connection'].close()

def updateUf(cod, uf):
    dict_connection = dbConnection()
    dict_connection['cursor'].execute('update tblclient set cli_uf = ? where cli_cod = ?', (uf, cod))
    dict_connection['connection'].commit()

    dict_connection['cursor'].close()
    dict_connection['connection'].close()

def updateCep(cod, cep):
    dict_connection = dbConnection()
    dict_connection['cursor'].execute('update tblclient set cli_cep = ? where cli_cod = ?', (cep, cod))
    dict_connection['connection'].commit()

    dict_connection['cursor'].close()
    dict_connection['connection'].close()

def updatePhone(cod, phone):
    dict_connection = dbConnection()
    dict_connection['cursor'].execute('update tblclient set cli_phone = ? where cli_cod = ?', (phone, cod))
    dict_connection['connection'].commit()

    dict_connection['cursor'].close()
    dict_connection['connection'].close()

def updateCellPhone(cod, cellPhone):
    dict_connection = dbConnection()
    dict_connection['cursor'].execute('update tblclient set cli_cellphone = ? where cli_cod = ?', (cellPhone, cod))
    dict_connection['connection'].commit()

    dict_connection['cursor'].close()
    dict_connection['connection'].close()

def selectAllClientInformation():
    dict_connection = dbConnection()
    dict_connection['cursor'].execute('select * from tblclient')

    listAllClientInformation = dict_connection['cursor'].fetchall()

    return listAllClientInformation

# Search clients by Phone
'''def searchClient():
    print('\nProcurar por Cliente\n')

    phoneClient = str(input('Digite o telefone do cliente: '))

    cursor.execute('select * from tblclient where cli_phone like ? or cli_cellphone like ?',
                   ('%' + phoneClient + '%', '%' + phoneClient + '%'))

    list_search = cursor.fetchall()

    return list_search'''
