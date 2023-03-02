import controller


def Nome():
    while True:
        nome = input('Nome Completo: ')
        if nome == '':
            print('Error! Entrada vazia.')
            continue
        temp = ''.join(nome.split(' '))
        for i in temp:
            if i.isdigit():
                print('Digite um nome válido.')
                break
        else:
            return nome.strip(' ')


def Senha():
    while True:
        senha = input('Senha: ')
        if senha == '':
            print('Error! Entrada vazia.')
            continue
        return senha.strip(' ')


def Email():
    while True:
        email = input('Email: ')
        if email == '':
            print('Error! Entrada vazia.')
        elif '@' and '.com' in email:
            return email.strip(' ')
        else:
            print('Email Inválido! Deve conter "@" e ".com"')


def Login():
    while True:
        login = input('Login: ')
        if login == '':
            print('Error! Entrada vazia.')
            continue
        return login.strip(' ')


def Celular():
    while True:
        celular = input('Celular (Apenas Números): ')
        if celular == '':
            print('Error! Entrada vazia.')
            continue
        elif not celular.isnumeric():
            print('Insira apenas números.')
            continue
        else:
            if 9 <= len(celular) <= 11:
                return celular
            else:
                print('O número deve ter entre 9 - 11 dígitos.')


def Endereco():
    while True:
        print('=== < ''\033[1;32m''Seu Endereço Completo!''\033[0;0m'' > ===')
        dados = {
            'Rua': input('Rua: '),
            'Numero': input('Numero: '),
            'Complemento': input('Complemento: '),
            'Bairro': input('Bairro: '),
            'CEP': input('CEP: '),
            'Cidade': input('Cidade: '),
            'Referencia': input('Referencia: '),
        }

        return dados


def Data():
    while True:
        data = input('Nascimento (dd/mm/aaaa): ')
        if data == '':
            print('Error! Entrada vazia.')
            continue
        temp = ''.join(data.split('/'))  # Retorna string de valores sem '/'
        if not temp.isnumeric():  # Analisa se string tem caracteres
            print('Insira uma data válida')
            continue
        # Retorna o número de '/' na data
        if data.count('/') == 2 and data != '//':
            dia, mes, ano = data.split('/')
            if 1 <= int(dia) <= 31 and 1 <= int(mes) <= 12 and 1900 <= int(ano) <= 2022:
                return data.strip(' ')
            else:
                print('Dia/Mes/Ano Inválido(s)')
        else:
            print('A data deve seguir o padrão dd/mm/aaa')
