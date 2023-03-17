import sys
import service
import datetime
import os
from time import sleep

def limpaTerminal():
    return os.system('cls' if os.name == 'nt' else 'clear')

def criaBarra():
    return print('-' * 32)

data = datetime.datetime.now()
dia = data.day
mes = data.month
ano = data.year

def menuInicial():
    print('=============== <<< ''\033[1;96m''U-Invest''\033[0;0m'' >>> ===============')
    print('|  [''\033[1;36m''1''\033[0;0m''] Usuários                                |')
    print('|  [''\033[1;36m''2''\033[0;0m''] Cursos e Aulas                          |')
    print('|  [''\033[1;36m''3''\033[0;0m''] Documentação Técnica da Plataforma      |')
    print('|  [''\033[1;36m''0''\033[0;0m''] Sair                                    |')
    print('------------------------------------------------')
    try:
        escolha = int(input('\033[1;36m''Insira a opção: ''\033[0;0m'))
    except ValueError:
        limpaTerminal()
        criaBarra()
        print('\033[1;31m''Insira uma opção válida!''\033[0;0m')
        criaBarra()
        menuInicial()
        return
    print('------------------------------------------------')

    if escolha == 1:
        limpaTerminal()
        subMenuUsuarios()
    elif escolha == 2:
        limpaTerminal()
        subMenuCursos()
    elif escolha == 3:
        limpaTerminal()
        subMenuDocs()
    elif escolha == 0:
        print('\033[1;36m''Fechando administração...''\033[0;0m')
        sleep(3)
        sys.exit()
    else:
        limpaTerminal()
        criaBarra()
        print('\033[1;31m''Insira uma opção válida!''\033[0;0m')
        criaBarra()
        menuInicial()

def subMenuUsuarios():
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
    try:
        escolha = int(input('\033[1;36m''Insira a opção: ''\033[0;0m'))
    except ValueError:
        limpaTerminal()
        criaBarra()
        print('\033[1;31m''Insira uma opção válida!''\033[0;0m')
        criaBarra()
        subMenuUsuarios()
        return
    print('--------------------------------------')
    if escolha == 1:
        cadastro()
        subMenuUsuarios()
    elif escolha == 2:
        mostraDados()
        subMenuUsuarios()
    elif escolha == 3:
        usuariosCadastrados()
        subMenuUsuarios()
    elif escolha == 4:
        relatorio()
        subMenuUsuarios()
    elif escolha == 5:
        removerUsuario()
        subMenuUsuarios()
    elif escolha == 0:
        sleep(1)
        limpaTerminal()
        menuInicial()
    else:
        limpaTerminal()
        criaBarra()
        print('\033[1;31m''Insira uma opção válida!''\033[0;0m')
        criaBarra()
        subMenuUsuarios()

def subMenuCursos():
    print('========== <<< ''\033[1;96m''U-Invest''\033[0;0m'' >>> ==========')
    print('|  [''\033[1;36m''1''\033[0;0m''] Cadastrar Curso               |')
    print('|  [''\033[1;36m''2''\033[0;0m''] Dados do Curso                |')
    print('|  [''\033[1;36m''3''\033[0;0m''] Mostrar Cursos                |')
    print('|  [''\033[1;36m''4''\033[0;0m''] Gerar Relatorio de Cursos     |')
    print('|  [''\033[1;36m''5''\033[0;0m''] Gerenciar Curso               |')
    print('|  [''\033[1;36m''6''\033[0;0m''] Remover Curso                 |')
    print('|  [''\033[1;36m''0''\033[0;0m''] Voltar                        |')
    print('--------------------------------------')
    try:
        escolha = int(input('\033[1;36m''Insira a opção: ''\033[0;0m'))
    except ValueError:
        limpaTerminal()
        criaBarra()
        print('\033[1;31m''Insira uma opção válida!''\033[0;0m')
        criaBarra()
        subMenuCursos()
        return
    print('--------------------------------------')
    if escolha == 1:
        cadastroCurso()
        subMenuCursos()
    elif escolha == 2:
        dadosCurso()
        subMenuCursos()
    elif escolha == 3:
        mostrarCursos()
        subMenuCursos()
    elif escolha == 4:
        relatorioCurso()
        subMenuCursos()
    elif escolha == 5:
        gerenciarCurso()
        subMenuCursos()
    elif escolha == 6:
        removeCurso()
        subMenuCursos()
    elif escolha == 0:
        sleep(1)
        limpaTerminal()
        menuInicial()
    else:
        limpaTerminal()
        criaBarra()
        print('\033[1;31m''Insira uma opção válida!''\033[0;0m')
        criaBarra()
        subMenuCursos()

def subMenuDocs():
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
    login = service.User()  # Retorna o login validado

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
    cpf = service.Cpf()
    data = service.Data()
    celular = service.Celular()
    perfilInvestidor = service.PerfilInvestidor()
    saldo = service.Saldo()

    limpaTerminal()
    criaBarra()
    print('\033[1;32m''Usuario Cadastrado com sucesso!''\033[0;0m')
    criaBarra()

    # --> Adiciona usuário no banco de dados usuarios.txt
    logins = open('usuarios.txt', 'a')
    logins.write(
        f'Nome: {nome} -Login: {login} -Senha: {senha} -Email: {email} -Cpf: {cpf} -Data de Nascimento: {data} -Numero de Celular: {celular} -Perfil de Investidor: {perfilInvestidor} -Saldo: {saldo}\n')
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
        subMenuUsuarios()


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
        subMenuUsuarios()
    
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

def cadastroCurso():
    limpaTerminal()
    print('====== < ''\033[1;92m''Cadastrar Curso''\033[0;0m'' > ======')
    nome = service.NomeCurso()
    nomeProfessor = service.Professor() 
    duracao = service.DuracaoCurso()
    resumo = service.ResumoCurso()
    pontuacao = service.PontuacaoCurso(duracao)
    avaliacao = service.AvaliacaoCurso([5, 4, 3, 5, 2, 5, 6, 7, -1])
    cdCurso = service.CdCurso()  

    limpaTerminal()
    criaBarra()
    print('\033[1;32m''Curso Cadastrado com sucesso!''\033[0;0m')
    criaBarra()

    Cursos = open('cursos.txt', 'a')
    Cursos.write(
        f'Curso: {nome} -Professor: {nomeProfessor} -Duração: {duracao} -Resumo: {resumo} -Pontuação: {pontuacao} -Avaliação: {avaliacao} -Identitificação: {cdCurso}\n')
    Cursos.close()
    subMenuCursos()

def dadosCurso():
    limpaTerminal()
    print('=== << ''\033[1; 33m''Dados do Curso''\033[0;0m'' >> ===')
    criaBarra()
    print('\033[1;33m''Digite o código do Curso para ver dados!''\033[0; 0m')
    criaBarra()
    codigo = input('Código: ')

    # Variavel de validação do codigo
    valida = False
    
    cursos = open('cursos.txt', 'r')
    for linha in cursos. readlines():
        valores = linha.split('-')
        if codigo == valores[6].split(':')[1].strip():
            limpaTerminal()
            criaBarra()
            print('\033[1;32m''Curso encontrado! Dados do Curso: ''\033[0; 0m')
            criaBarra()
            for percorre in range(len(valores)):
                print(valores[percorre])
            criaBarra()
            valida = True
            cursos.close()
            subMenuCursos()

    if not valida:
        limpaTerminal()
        criaBarra()
        print('\033[1;31m''Erro! Código não encontrado ou inexistente.''\033[0; 0m')
        criaBarra()
        subMenuCursos()

def mostrarCursos():
    limpaTerminal()
    print('=== Cursos Cadastrados ===')
    cursos = open('cursos.txt', 'r')
    for linha in cursos.readlines():
        l = linha.split('-')
        print('\033[1;92m'f'{l[0]} | {l[1]}''\033[0;0m')
    criaBarra()
    subMenuCursos()

def relatorioCurso():
    countUsers = 0
    nomess = []
    
    cursos = open('cursos.txt', 'r')
    for linhas in cursos.readlines():
        l = linhas.split('-')
        nomess.append(l[0])
        countUsers += 1
        
    limpaTerminal()
    arquivo = open('relatorioCursos.txt', 'w+')
    arquivo.write('Relatorio de Cursos \n')
    arquivo.write('\n')
    arquivo.write(f'A U-Invest possui {countUsers} cursos \n')
    for i in range(len(nomess)):
        arquivo.write(str(f'{i + 1}.{nomess[i].split(":")[1]} \n'))
    criaBarra( )
    print('\033[1;32m'"Relatorio gerado em 'relatorioCursos.txt'"'\033[0;0m')
    criaBarra()
    arquivo.close()
    subMenuCursos()

def gerenciarCurso():
    limpaTerminal()
    print("Em desenvolvimento!")
    subMenuCursos()

def removeCurso():
    limpaTerminal()
    print('=== << ''\033[1; 33m''Dados do Curso''\033[0;0m'' >> ===')
    criaBarra()
    print('\033[1;33m''Digite o código do Curso para excluir''\033[0; 0m')
    criaBarra()
    codigo = input('Código: ')
    
    valida = False

    cursos = open('cursos.txt', 'r')
    for linha in cursos.readlines():
        valores = linha.split('-')
        if codigo == valores[6].split(':')[1].strip():
            limpaTerminal()
            criaBarra()
            print('\033[1;32m''Curso encontrado! Excluindo... ''\033[0; 0m')
            criaBarra()
            sleep(5)
            
            with open('cursos.txt', 'r+') as arquivo:
                newLinhas = arquivo.readlines()
                arquivo.seek(0)
                for newLinha in newLinhas:
                    if newLinha != linha:
                        arquivo.write(newLinha)
                arquivo.truncate()

            print('\033[1;32m''Curso Excluido! ''\033[0; 0m')
            criaBarra()
            valida = True
            subMenuCursos()

    if not valida:
        limpaTerminal()
        criaBarra()
        print('\033[1;31m''Erro! Código não encontrado ou inexistente.''\033[0; 0m')
        criaBarra()
        subMenuCursos()