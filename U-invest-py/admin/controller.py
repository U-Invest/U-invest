import service
import datetime
import os
from time import sleep
import tempfile
import shutil



def limpaTerminal():
    return os.system('cls' if os.name == 'nt' else 'clear')


def criaBarra():
    return print('-' * 32)


data = datetime.datetime.now()
dia = data.day
mes = data.month
ano = data.year

def menuInicial():
    limpaTerminal()
    print('=============== <<< ''\033[1;96m''U-Invest''\033[0;0m'' >>> ===============')
    print('|  [''\033[1;36m''1''\033[0;0m''] Usuários                                |')
    print('|  [''\033[1;36m''2''\033[0;0m''] Cursos e Aulas                          |')
    print('|  [''\033[1;36m''3''\033[0;0m''] Documentação Técnica da Plataforma      |')
    print('|  [''\033[1;36m''0''\033[0;0m''] Sair                                    |')
    print('------------------------------------------------')
    x = input('\033[1;36m''Insira a opção: ''\033[0;0m')
    print('------------------------------------------------')
    return x

def subMenuUsuarios():
    limpaTerminal()
    print('========== <<< ''\033[1;96m''U-Invest''\033[0;0m'' >>> ==========')
    print(
        '|  [''\033[1;36m''1''\033[0;0m''] Cadastrar Usuário             |')
    print(
        '|  [''\033[1;36m''2''\033[0;0m''] Dados do Usuário              |')
    print(
        '|  [''\033[1;36m''3''\033[0;0m''] Mostrar Usuários              |')
    print('|  [''\033[1;36m''4''\033[0;0m''] Gerar Relatório de Usuarios   |')
    print(
        '|  [''\033[1;36m''5''\033[0;0m''] Remover Usuário               |')
    print('|  [''\033[1;36m''0''\033[0;0m''] Voltar                        |')
    print('--------------------------------------')
    x = input('\033[1;36m''Insira a opção: ''\033[0;0m')
    print('--------------------------------------')
    return x

def subMenuCursos():
    limpaTerminal()
    print('========== <<< ''\033[1;96m''U-Invest''\033[0;0m'' >>> ==========')
    print(
        '|  [''\033[1;36m''1''\033[0;0m''] Cadastrar Curso               |')
    print(
        '|  [''\033[1;36m''2''\033[0;0m''] Dados do Curso                |')
    print(
        '|  [''\033[1;36m''3''\033[0;0m''] Mostrar Curso                 |')
    print('|  [''\033[1;36m''4''\033[0;0m''] Gerar Relatorio de Cursos     |')
    print(
        '|  [''\033[1;36m''5''\033[0;0m''] Remover Curso                 |')
    print(
        '|  [''\033[1;36m''6''\033[0;0m''] Gerenciar Curso               |')
    print('|  [''\033[1;36m''0''\033[0;0m''] Voltar                        |')
    print('--------------------------------------')
    x = input('\033[1;36m''Insira a opção: ''\033[0;0m')
    print('--------------------------------------')
    return x

def subMenuDocs():
    limpaTerminal()
    print('============== <<< ''\033[1;96m''U-Invest''\033[0;0m'' >>> ==============')
    print('|  [''\033[1;36m''1''\033[0;0m''] Gerar Documentaçao                    |')
    print('|  [''\033[1;36m''2''\033[0;0m''] Imprimir Documentaçao                 |')
    print('|  [''\033[1;36m''3''\033[0;0m''] Visualizar Documentaçao na Web        |')
    print('|  [''\033[1;36m''4''\033[0;0m''] Acessar Protótipo da Plataforma Web   |')
    print('|  [''\033[1;36m''0''\033[0;0m''] Voltar                                |')
    print('----------------------------------------------')
    x = input('\033[1;36m''Insira a opção: ''\033[0;0m')
    print('----------------------------------------------')
    return x


''' Função de Cadastrar / Checar login existente / Adicionar dados no arquivo txt de logins '''


def cadastro():
    limpaTerminal()
    print('====== < ''\033[1;92m''Cadastrar Usuário''\033[0;0m'' > ======')
    nome = service.Nome()  # Retorna o nome validado
    login = service.Login()  # Retorna o login validado

    # --> Conferir se já existe o login cadastrado
    lerLogins = open('usuarios.txt', 'r')
    for linha in lerLogins.readlines():
        valores = linha.split('-')
        # Cria lista com valores da linha
        if login == valores[1].split(':')[1].strip():
            # Confere se o login cadastrado é igual ao login da linha
            limpaTerminal()
            criaBarra()
            print('\033[1;31m''Login ja existente!''\033[0;0m')
            criaBarra()
            return
    lerLogins.close()

    # Retornando valores validados
    senha = service.Senha()
    email = service.Email()
    data = service.Data()
    celular = service.Celular()
    endereco = service.Endereco()

    limpaTerminal()
    criaBarra()
    print('\033[1;32m''Usuario Cadastrado com sucesso!''\033[0;0m')
    criaBarra()

    # --> Adiciona usuário no banco de dados usuarios.txt
    logins = open('usuarios.txt', 'a')
    logins.write(
        f'Nome: {nome} -Login: {login} -Senha: {senha} -Email: {email} -Data de Nascimento: {data} -Numero de Celular: {celular} -Endereco: {endereco} \n')
    logins.close()
    return


''' Logar um usuário e printar seus dados cadastrados '''


def mostraDados():
    limpaTerminal()
    print('=== << ''\033[1; 33m''Dados do Usuario''\033[0;0m'' >> ===')
    criaBarra()
    print('\033[1;33m''Logue para acessar seus dados!''\033[0; 0m')
    criaBarra()
    userLogin = input('Login: ')
    userSenha = input('Senha: ')

    # Variavel de validação do login
    valida = False

    logins = open('usuarios.txt', 'r')
    for linha in logins. readlines():
        valores = linha.split('-')
        if userLogin == valores[1].split(':')[1].strip() and userSenha in valores[2].split(':')[1].strip():
            limpaTerminal()
            criaBarra()
            print('\033[1;32m''Usuario Logado! Dados do usuário: ''\033[0; 0m')
            criaBarra()
            for percorre in range(len(valores)):
                if valores[percorre].split(': ')[0] == 'Endereco':
                    dictEndereco = eval(
                        valores[percorre].split('Endereco:')[1])
                    for chave in dictEndereco:
                        print(f'{chave}: {dictEndereco [chave]}')
                else:
                    print(valores[percorre])
            criaBarra()
            valida = True
            logins.close()
            break

    if not valida:
        limpaTerminal()
        criaBarra()
        print('\033[1;31m''Erro! Login ou senha invalidos''\033[0; 0m')
        criaBarra()


def usuariosCadastrados():
    limpaTerminal()
    print('=== Usuarios Cadastrados ===')
    logins = open('usuarios.txt', 'r')
    for linha in logins.readlines():
        l = linha.split('-')
        print('\033[1;92m'f'{l[0]} | {l[1]}''\033[0;0m')
    criaBarra()
    return

def relatorio():
    countUsers = 0
    nomess = []
    
    logins = open('usuarios.txt', 'r')
    for linhas in logins.readlines():
        l = linhas.split('-')
        nomess.append(l[0])
        countUsers += 1
        
    limpaTerminal()
    arquivo = open('relatorio.txt', 'w+')
    arquivo.write('Relatorio de Usuarios \n')
    arquivo.write('\n')
    arquivo.write(f'A U-Invest possui {countUsers} usuarios \n')
    for i in range(len(nomess)):
        arquivo.write(str(f'{i + 1}.{nomess[i].split(":")[1]} \n'))
    arquivo.write(f'{dia}/{mes}/{ano}')
    criaBarra( )
    print('\033[1;32m'"Relatorio gerado em 'relatorio.txt'"'\033[0;0m')
    criaBarra()
    arquivo.close()
    return

def removerUsuario():
    limpaTerminal()
    print('=== << ''\033[1; 33m''Dados do Usuario''\033[0;0m'' >> ===')
    criaBarra()
    print('\033[1;33m''Logue para excluir seu usuario!''\033[0; 0m')
    criaBarra()
    userLogin = input('Login: ')
    userSenha = input('Senha: ')

    # Variavel de validação do login
    valida = False

    logins = open('usuarios.txt', 'r')
    for linha in logins.readlines():
        valores = linha.split('-')
        if userLogin == valores[1].split(':')[1].strip() and userSenha in valores[2].split(':')[1].strip():
            limpaTerminal()
            criaBarra()
            print('\033[1;32m''Usuario Logado! Excluindo... ''\033[0; 0m')
            criaBarra()
            sleep(5)
            
            with open('usuarios.txt', 'r+') as arquivo:
                newLinhas = arquivo.readlines()
                arquivo.seek(0)
                for newLinha in newLinhas:
                    if newLinha != linha:
                        arquivo.write(newLinha)
                arquivo.truncate()

            print('\033[1;32m''Usuario Excluido! ''\033[0; 0m')
            criaBarra()
            valida = True
            break

    if not valida:
        limpaTerminal()
        criaBarra()
        print('\033[1;31m''Erro! Login ou senha invalidos''\033[0; 0m')
        criaBarra()
    
def userAdminValidate():
    limpaTerminal()
    criaBarra()
    print('\033[1;96m''Logue com o user e senha do administrador para administrar a plataforma''\033[0;0m')
    criaBarra()
    userLogin = input('Login: ')
    userSenha = input('Senha: ')

    # Variavel de validação do login
    valida = False

    logins = open('adminUser.txt', 'r')
    for linha in logins.readlines():
        valores = linha.split('-')
        print(valores)
        if userLogin == valores[0].split(':')[1].strip() and userSenha in valores[1].split(':')[1].strip():
            limpaTerminal()
            criaBarra()
            print('\033[1;32m''Administrador Logado! Carregando dados...''\033[0; 0m')
            criaBarra()
            sleep(3)
            valida = True
            break

    if not valida:
        limpaTerminal()
        criaBarra()
        print('\033[1;31m''Erro! Login ou senha invalidos''\033[0; 0m')
        criaBarra()

    return valida