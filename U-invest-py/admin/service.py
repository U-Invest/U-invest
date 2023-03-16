from prettytable import PrettyTable

def PerfilInvestidor():
    tabela = PrettyTable()
    tabela.field_names = ["Iniciante", "Conservador", "Experiente"]
    # Adiciona linhas à tabela
    tabela.add_row(["CDB", "CDB", "Ações e Fundos de Ações"])
    tabela.add_row(["Tesouro Direto", "Tesouro Direto", "CDB e Tesouro Direto"])
    tabela.add_row(["Fundos de Renda Fixa", "Fundos de Renda Fixa e Fundos Multimercado", "Fundos Imobiliários e Fundos Multimercado"])
    tabela.add_row([" "," ","Fundos Cambiais e Fundos de Renda Fixa"])
    print(tabela)
    while True:
        print('Qual perfil de investidor você se identificou?')
        try:
            perfil = int(input("1 - Iniciante \n2 - Conservador \n3 - Experiente\n"))
            if (perfil > 0) and (perfil < 4):
                if(perfil == 1):
                    perfil = "Iniciante"
                elif (perfil == 2):
                    perfil = "Conservador"
                else:
                    perfil = "Experiente"
                return perfil
            else: 
                print("Error! Digite um perfil de investidor válido.")
        except :
            print("Error! Digite um perfil de investidor válido.")

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


def User():
    while True:
        login = input('User: ')
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

def Cpf():
    while True:
        try:
            cpf = input('CPF (Apenas Números): ')
            if len(cpf) == 11:
                return cpf
            else:
                print("Error! Quantidade de caracteres incorreta.")
        except ValueError:
           print("Error! Digite valores válidos!")

def Saldo():
    return 0