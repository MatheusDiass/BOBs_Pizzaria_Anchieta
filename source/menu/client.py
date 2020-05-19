from source.menu.principal import principal, headermenu

def clientmenu():

    optionClient = 0

    print('\nMenu Cliente\n')
    print('[0] - Voltar')
    print('[1] - Cadastro')
    print('[2] - Manutenção')
    print('[3] - Deletar')

    optionClient = int(input('Digite a opção desejada:  '))

    while (optionClient >= 0 or optionClient <= 3):
        if(optionClient == 0):
            headermenu()
            principal()
            break

        elif(optionClient == 1):
            headermenu()
            clientcadastre()
            break





def clientcadastre():

    print('\nCadastro de Cliente\n')

    clientName = str(input('Digite o nome: '))
    clientAddress = str(input('Digite o endereço: '))
    clientComple = str(input('Digite o complemento: '))
    clientDistr = str(input('Digite o bairro: '))
    clientCity = str(input('Digite a cidade: '))
    clientUf = str(input('Digite o UF: '))
    clientCep = str(input('Digite o CEP: '))
    clientPhone = str(input('Digite o número de telefone: '))
    clientCell = str(input('Digte o número de telefone celular: '))