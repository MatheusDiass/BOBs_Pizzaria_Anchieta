import _sqlite3

def dbConnection():
    path = 'C:\\Users\Matheus Dias\Documents\Git_MyProjects\BOBs_Pizzaria_Anchieta\data\db_bobsPizzaria'
    connection = _sqlite3.connect(path)
    cursor = connection.cursor()
    dict_connection = {'connection':connection, 'cursor':cursor}
    return dict_connection


# Cadastre of the clients
def save(data_client):
    dict_connection = dbConnection()
    dict_connection['cursor'].execute('insert into tblcustomer(cus_name, cus_address, cus_complement, cus_district, cus_city, cus_uf, cus_cep, cus_phone, cus_cellphone) \
                    values(?, ?, ?, ?, ?, ?, ?, ?, ?)', data_client)

    dict_connection['connection'].commit()

    dict_connection['cursor'].close()
    dict_connection['connection'].close()

def updateName(cod, name):
    dict_connection = dbConnection()
    dict_connection['cursor'].execute('update tblcustomer set cus_name = ? where cus_cod = ?', (name, cod))
    dict_connection['connection'].commit()

    dict_connection['cursor'].close()
    dict_connection['connection'].close()

def updateAddress(cod, address):
    dict_connection = dbConnection()
    dict_connection['cursor'].execute('update tblcustomer set cus_address = ? where cus_cod = ?', (address, cod))
    dict_connection['connection'].commit()

    dict_connection['cursor'].close()
    dict_connection['connection'].close()

def updateComplement(cod, complement):
    dict_connection = dbConnection()
    dict_connection['cursor'].execute('update tblcustomer set cus_complement = ? where cus_cod = ?', (complement, cod))
    dict_connection['connection'].commit()

    dict_connection['cursor'].close()
    dict_connection['connection'].close()

def updateDistrict(cod, district):
    dict_connection = dbConnection()
    dict_connection['cursor'].execute('update tblcustomer set cus_district = ? where cus_cod = ?', (district, cod))
    dict_connection['connection'].commit()

    dict_connection['cursor'].close()
    dict_connection['connection'].close()

def updateCity(cod, city):
    dict_connection = dbConnection()
    dict_connection['cursor'].execute('update tblcustomer set cus_city = ? where cus_cod = ?', (city, cod))
    dict_connection['connection'].commit()

    dict_connection['cursor'].close()
    dict_connection['connection'].close()

def updateUf(cod, uf):
    dict_connection = dbConnection()
    dict_connection['cursor'].execute('update tblcustomer set cus_uf = ? where cus_cod = ?', (uf, cod))
    dict_connection['connection'].commit()

    dict_connection['cursor'].close()
    dict_connection['connection'].close()

def updateCep(cod, cep):
    dict_connection = dbConnection()
    dict_connection['cursor'].execute('update tblcustomer set cus_cep = ? where cus_cod = ?', (cep, cod))
    dict_connection['connection'].commit()

    dict_connection['cursor'].close()
    dict_connection['connection'].close()

def updatePhone(cod, phone):
    dict_connection = dbConnection()
    dict_connection['cursor'].execute('update tblcustomer set cus_phone = ? where cus_cod = ?', (phone, cod))
    dict_connection['connection'].commit()

    dict_connection['cursor'].close()
    dict_connection['connection'].close()

def updateCellPhone(cod, cellPhone):
    dict_connection = dbConnection()
    dict_connection['cursor'].execute('update tblcustomer set cus_cellphone = ? where cus_cod = ?', (cellPhone, cod))
    dict_connection['connection'].commit()

    dict_connection['cursor'].close()
    dict_connection['connection'].close()

def selectAllClientInformation():
    dict_connection = dbConnection()
    dict_connection['cursor'].execute('select * from tblcustomer')

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
