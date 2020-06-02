# Importa a função de conexão do arquivo de conexão
from source.db.connection import dbConnection

# Realiza o cadastro do cliente
def save(data_client):
    dict_connection = dbConnection()
    dict_connection['cursor'].execute('insert into tblcustomer(cus_name, cus_address, cus_number, cus_complement, cus_district, cus_city, cus_uf, cus_cep, cus_phone, cus_cellphone) \
                    values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', data_client)

    dict_connection['connection'].commit()

    dict_connection['cursor'].close()
    dict_connection['connection'].close()

# Atualiza o nome
def updateName(cod, name):
    dict_connection = dbConnection()
    dict_connection['cursor'].execute('update tblcustomer set cus_name = ? where cus_cod = ?', (name, cod))
    dict_connection['connection'].commit()

    dict_connection['cursor'].close()
    dict_connection['connection'].close()

# Atualiza o endereço
def updateAddress(cod, address):
    dict_connection = dbConnection()
    dict_connection['cursor'].execute('update tblcustomer set cus_address = ? where cus_cod = ?', (address, cod))
    dict_connection['connection'].commit()

    dict_connection['cursor'].close()
    dict_connection['connection'].close()

# Atualiza o complemento
def updateComplement(cod, complement):
    dict_connection = dbConnection()
    dict_connection['cursor'].execute('update tblcustomer set cus_complement = ? where cus_cod = ?', (complement, cod))
    dict_connection['connection'].commit()

    dict_connection['cursor'].close()
    dict_connection['connection'].close()

# Atualiza o bairro
def updateDistrict(cod, district):
    dict_connection = dbConnection()
    dict_connection['cursor'].execute('update tblcustomer set cus_district = ? where cus_cod = ?', (district, cod))
    dict_connection['connection'].commit()

    dict_connection['cursor'].close()
    dict_connection['connection'].close()

# Atualiza a cidade
def updateCity(cod, city):
    dict_connection = dbConnection()
    dict_connection['cursor'].execute('update tblcustomer set cus_city = ? where cus_cod = ?', (city, cod))
    dict_connection['connection'].commit()

    dict_connection['cursor'].close()
    dict_connection['connection'].close()

# Atualiza o UF
def updateUf(cod, uf):
    dict_connection = dbConnection()
    dict_connection['cursor'].execute('update tblcustomer set cus_uf = ? where cus_cod = ?', (uf, cod))
    dict_connection['connection'].commit()

    dict_connection['cursor'].close()
    dict_connection['connection'].close()

# Atualiza o CEP
def updateCep(cod, cep):
    dict_connection = dbConnection()
    dict_connection['cursor'].execute('update tblcustomer set cus_cep = ? where cus_cod = ?', (cep, cod))
    dict_connection['connection'].commit()

    dict_connection['cursor'].close()
    dict_connection['connection'].close()

# Atualiza o telefone
def updatePhone(cod, phone):
    dict_connection = dbConnection()
    dict_connection['cursor'].execute('update tblcustomer set cus_phone = ? where cus_cod = ?', (phone, cod))
    dict_connection['connection'].commit()

    dict_connection['cursor'].close()
    dict_connection['connection'].close()

# Atualiza o telefone celular
def updateCellPhone(cod, cellPhone):
    dict_connection = dbConnection()
    dict_connection['cursor'].execute('update tblcustomer set cus_cellphone = ? where cus_cod = ?', (cellPhone, cod))
    dict_connection['connection'].commit()

    dict_connection['cursor'].close()
    dict_connection['connection'].close()

# Deleta o cliente
def delete(cod):
    dict_connection = dbConnection()
    dict_connection['cursor'].execute('delete from tblcustomer where cus_cod = ?', (cod,))
    dict_connection['connection'].commit()

    dict_connection['cursor'].close()
    dict_connection['connection'].close()

# Busca todos os clientes junto de todas as suas informações
def selectAllCustomertInformation():
    dict_connection = dbConnection()
    dict_connection['cursor'].execute('select * from tblcustomer')

    listAllClientInformation = dict_connection['cursor'].fetchall()

    dict_connection['cursor'].close()
    dict_connection['connection'].close()

    return listAllClientInformation

# Busca apenas um cliente
def selectCustomerByCod(cod):
    dict_connection = dbConnection()
    dict_connection['cursor'].execute('select * from tblcustomer where cus_cod = ?', (cod,))

    oneCustomer = dict_connection['cursor'].fetchone()

    dict_connection['cursor'].close()
    dict_connection['connection'].close()

    return oneCustomer

# Informa o quantidade de clientes cadastrados
def quantityCustomer():
    dict_connection = dbConnection()
    dict_connection['cursor'].execute('select count(cus_cod) from tblcustomer')

    qttCustomer = dict_connection['cursor'].fetchone()

    dict_connection['cursor'].close()
    dict_connection['connection'].close()

    return qttCustomer

# Busca o cliente pelo telefone ou telefone celular
def searchClientByPhone(phoneClient):
    dict_connection = dbConnection()
    dict_connection['cursor'].execute('select * from tblcustomer where cus_phone like ? or cus_cellphone like ?',
                   ('%' + phoneClient + '%', '%' + phoneClient + '%'))

    oneClient = dict_connection['cursor'].fetchone()

    dict_connection['cursor'].close()
    dict_connection['connection'].close()

    return oneClient
