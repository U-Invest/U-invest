import service
import datetime
import os


def limpaTerminal():
    return os.system('cls' if os.name == 'nt' else 'clear')


def criaBarra():
    return print('-' * 32)


data = datetime.datetime.now()
dia = data.day
mes = data.month
ano = data.year


def menu():
    print('====== <<< ''\033[1;96m''U-Invest''\033[0;0m'' >>> ======')
    print('|  [''\033[1;36m''1''\033[0;0m''] Cadastrar Cliente     |')
    print('|  [''\033[1;36m''2''\033[0;0m''] Dados do Cliente      |')
    print('|  [''\033[1;36m''3''\033[0;0m''] Mostrar Clientes      |')
    print('|  [''\033[1;36m''4''\033[0;0m''] Gerar Relatório       |')
    print('|  [''\033[1;36m''5''\033[0;0m''] Remover Cliente       |')
    print('|  [''\033[1;36m''0''\033[0;0m''] Sair                  |')
    print('--------------------------------')
    x = input('\033[1;36m''Insira a opção: ''\033[0;0m')
    print('--------------------------------')
    return x


''' Função de Cadastrar / Checar login existente / Adicionar dados no arquivo txt de logins '''


def cadastro():
    limpaTerminal()
    print('====== < ''\033[1;92m''Cadastrar Usuário''\033[0;0m'' > ======')
    nome = service.Nome()  # Retorna o nome validado
    login = service.Login()  # Retorna o login validado

    # --> Conferir se já existe o login cadastrado
    lerLogins = open('logins.txt', 'r')
    for linha in lerLogins.readlines():
        valores = linha.split('-')
        # Cria lista com valores da linha
        if login == valores[1].split(':')[1].strip():
            # Confere se o login cadastrado é igual ao login da linha
            limpaTerminal()
            criaBarra()
            print('\033[1;31m''Login já existente!''\033[0;0m')
            criaBarra()
            return
    lerLogins.close()

    # Retornando valores validados
    senha = service.Senha()
    email = service.Email()
    data = service.Data()
