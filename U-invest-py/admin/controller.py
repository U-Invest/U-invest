import oracledb
import sys
import service
import datetime
import os
from time import sleep

try:
    dnStr = oracledb.makedsn("oracle.fiap.com.br", "1521", "ORCL")
    conn = oracledb.connect(user='rm96920', password='080903', dsn=dnStr)
    inst_SQL = conn.cursor()
except Exception as e:
    print("Erro: ", e)
    conexao = False
    inst_SQL = ""
    conn = ""
else:
    conexao = True


def limpaTerminal():
    return os.system('cls' if os.name == 'nt' else 'clear')


def criaBarra():
    return print('-' * 32)


data = datetime.datetime.now()
dia = data.day
mes = data.month
ano = data.year


def menuInicial():
    print(
        '=============== <<< ''\033[1;96m''U-Invest''\033[0;0m'' >>> ===============')
    print(
        '|  [''\033[1;36m''1''\033[0;0m''] Usuários                                |')
    print(
        '|  [''\033[1;36m''2''\033[0;0m''] Cursos e Aulas                          |')
    print(
        '|  [''\033[1;36m''3''\033[0;0m''] Documentação Técnica da Plataforma      |')
    print(
        '|  [''\033[1;36m''0''\033[0;0m''] Sair                                    |')
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
        conn.close()
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
        if (conexao == True):
            cadastro()
            subMenuUsuarios()
        else:
            print('\033[1;31m''Database was not connect!''\033[0;0m')
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
    print(
        '============== <<< ''\033[1;96m''U-Invest''\033[0;0m'' >>> ==============')
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


def confereLoginExistente(nome, login):
    dados = f"""SELECT * FROM usuario WHERE nome = '{nome}' OR nickname = '{login}'"""
    inst_SQL.execute(dados)
    listaUsuario = inst_SQL.fetchall()
    if (len(listaUsuario) != 0):
        return True
    else:
        return False


def cadastro():
    try:
        limpaTerminal()
        print('====== < ''\033[1;92m''Cadastrar Usuário''\033[0;0m'' > ======')

        nome = service.Nome()  # Retorna o nome validado
        login = service.User()  # Retorna o login validado

        if (confereLoginExistente(nome, login)):
            print('\033[1;31m''Login ja existente!''\033[0;0m')
            criaBarra()
            return

        # Retornando valores validados
        senha = service.Senha()
        email = service.Email()
        cpf = service.Cpf()

        data = ''.join(service.Data().split('/'))

        celular = service.Celular()
        perfilInvestidor = service.PerfilInvestidor()
        saldo = service.Saldo()

        # Executa o insert na tabela do sql
        cadastro = f"""INSERT INTO usuario (cpf, email, celular, nome, saldo, senha, perfil_investidor, nickname, nascimento) VALUES ('{cpf}','{email}','{celular}','{nome}',{saldo},'{senha}','{perfilInvestidor}','{login}','{data}')"""
        inst_SQL.execute(cadastro)
        conn.commit()
        conn.close()

        limpaTerminal()
        criaBarra()
        print('\033[1;32m''Usuario Cadastrado com sucesso!''\033[0;0m')
        criaBarra()
        return
    except ValueError:
        print("Digite valores numéricos")
    except:
        print('\033[1;31m''Erro de transação com o BD''\033[0;0m')


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

    dados = f"""SELECT * FROM usuario WHERE nickname = '{userLogin}' AND senha = '{userSenha}'"""
    inst_SQL.execute(dados)
    listaUsuario = inst_SQL.fetchall()
    if (len(listaUsuario) != 0):
        limpaTerminal()
        criaBarra()
        print('\033[1;32m''Usuario Logado! Dados do usuário: ''\033[0; 0m')
        criaBarra()
        # Dados do usuario
        for usuario in listaUsuario:
            print(f'''\033[1;36mNome: \033[0;0m{usuario[3]}''')
            print(f'''\033[1;36mEmail: \033[0;0m{usuario[1]}''')
            print(f'''\033[1;36mLogin: \033[0;0m{usuario[7]}''')
            print(f'''\033[1;36mCelular: \033[0;0m{usuario[2]}''')
            print(f'''\033[1;36mCpf: \033[0;0m{usuario[0]}''')
            print(f'''\033[1;36mData de Nascimento: \033[0;0m{usuario[8]}''')
            print(f'''\033[1;36mNível de Investidor: \033[0;0m{usuario[6]}''')
            print(f'''\033[1;36mSaldo: \033[0;0m{usuario[4]}''')
        criaBarra()
        valida = True
    else:
        valida = False

    if not valida:
        limpaTerminal()
        criaBarra()
        print('\033[1;31m''Erro! Login ou senha invalidos''\033[0; 0m')
        criaBarra()
        subMenuUsuarios()


def usuariosCadastrados():
    limpaTerminal()
    print('''\033[1;36m=== Usuarios Cadastrados ===\033[0;0m''')
    # Usuarios
    dados = f"""SELECT * FROM usuario"""
    inst_SQL.execute(dados)
    listaUsuario = inst_SQL.fetchall()
    for usuario in listaUsuario:
        nome = usuario[3]
        user = usuario[7]
        print(
            f'''\033[1;36mNome: \033[0;0m{nome} | \033[1;36mLogin: \033[0;0m{user}''')
    criaBarra()
    return


def relatorio():
    limpaTerminal()
    arquivo = open('relatorio.txt', 'w+')
    arquivo.write('Relatorio de Usuarios \n')
    arquivo.write('\n')

    # Consulta SQL para obter os nomes dos usuários
    dados = """SELECT nome FROM usuario"""
    inst_SQL.execute(dados)
    listaNomes = inst_SQL.fetchall()

    countUsers = len(listaNomes)
    arquivo.write(f'A U-Invest possui {countUsers} usuarios \n')
    for i, nome in enumerate(listaNomes, start=1):
        arquivo.write(f'{i}.{nome[0]} \n')
    arquivo.write(f'{dia}/{mes}/{ano}')
    criaBarra()
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

    dados = f"""SELECT * FROM usuario WHERE nickname = '{userLogin}' AND senha = '{userSenha}'"""
    inst_SQL.execute(dados)
    listaUsuario = inst_SQL.fetchall()
    if (len(listaUsuario) != 0):
        limpaTerminal()
        criaBarra()
        print('\033[1;32m''Usuario Logado! Excluindo... ''\033[0; 0m')
        criaBarra()
        sleep(5)
        # Excluir usuario que logou
        delete_query = f"""DELETE FROM usuario WHERE nickname = '{userLogin}'"""
        inst_SQL.execute(delete_query)
        conn.commit()
        print('\033[1;32m''Usuario Excluido! ''\033[0; 0m')
        criaBarra()
        valida = True
    else:
        valida = False

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
            print(
                '\033[1;32m''Administrador Logado! Carregando dados...''\033[0; 0m')
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
    try:
        limpaTerminal()
        print('====== < ''\033[1;92m''Cadastrar Curso''\033[0;0m'' > ======')
        nome = service.NomeCurso()
        nomeProfessor = service.Professor()
        duracao = service.DuracaoCurso()
        resumo = service.ResumoCurso()
        pontuacao = service.PontuacaoCurso(duracao)
        avaliacao = service.AvaliacaoCurso([5, 4, 3, 5, 2, 5, 6, 7, -1])
        cdCurso = service.CdCurso()

        print(duracao, avaliacao, resumo,
              nomeProfessor, nome, cdCurso, pontuacao)
        print(type(duracao), type(avaliacao), type(resumo), type(
            nomeProfessor), type(nome), type(cdCurso), type(pontuacao))

        # Executa o insert na tabela do sql
        cadastro = f"""INSERT INTO curso (duracao, avaliacao, resumo, professor, nome, id_curso, pontuacao) VALUES ({duracao},{avaliacao},'{resumo}','{nomeProfessor}','{nome}','{cdCurso}',{pontuacao})"""
        inst_SQL.execute(cadastro)
        conn.commit()
        conn.close()

        limpaTerminal()
        criaBarra()
        print('\033[1;32m''Curso Cadastrado com sucesso!''\033[0;0m')
        criaBarra()
        subMenuCursos()
    except ValueError:
        print("Digite valores numéricos")
    except:
        print('\033[1;31m''Erro de transação com o BD''\033[0;0m')


def dadosCurso():
    limpaTerminal()
    print('=== << ''\033[1; 33m''Dados do Curso''\033[0;0m'' >> ===')
    criaBarra()
    print('\033[1;33m''Digite o código do Curso para ver dados!''\033[0; 0m')
    criaBarra()
    codigo = input('Código: ')

    # Variavel de validação do login
    valida = False

    dados = f"""SELECT * FROM curso WHERE id_curso = '{codigo}'"""
    inst_SQL.execute(dados)
    listaCurso = inst_SQL.fetchall()
    if (len(listaCurso) != 0):
        limpaTerminal()
        criaBarra()
        print('\033[1;32m''Curso encontrado! Dados do Curso: ''\033[0; 0m')
        criaBarra()
        for curso in listaCurso:
            print(f'''\033[1;36mNome: \033[0;0m{curso[4]}''')
            print(f'''\033[1;36mProfessor: \033[0;0m{curso[3]}''')
            print(f'''\033[1;36mDuração: \033[0;0m{curso[0]}''')
            print(f'''\033[1;36mAvaliação: \033[0;0m{curso[1]}''')
            print(f'''\033[1;36mResumo: \033[0;0m{curso[2]}''')
            print(f'''\033[1;36mPontuação: \033[0;0m{curso[6]}''')
            print(f'''\033[1;36mCódigo: \033[0;0m{curso[5]}''')

        criaBarra()
        valida = True
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
    dados = f"""SELECT * FROM curso"""
    inst_SQL.execute(dados)
    listaCursos = inst_SQL.fetchall()
    for curso in listaCursos:
        nome = curso[4]
        professor = curso[3]
        duracao = curso[0]
        print(
            f'''\033[1;36mNome: \033[0;0m{nome} | \033[1;36mProfessor: \033[0;0m{professor} | \033[1;36mDuração: \033[0;0m{duracao}''')
    criaBarra()
    return

def relatorioCurso():
    limpaTerminal()
    arquivo = open('relatorioCursos.txt', 'w+', encoding='utf-8')
    arquivo.write('Relatorio de Cursos \n')
    arquivo.write('\n')

    # Consulta SQL para obter os nomes dos usuários
    dados = """SELECT nome FROM curso"""
    inst_SQL.execute(dados)
    listaNomes = inst_SQL.fetchall()

    countUsers = len(listaNomes)
    arquivo.write(f'A U-Invest possui {countUsers} cursos \n')
    for i, nome in enumerate(listaNomes, start=1):
        arquivo.write(f'{i}.{nome[0]} \n')
    criaBarra()
    print('\033[1;32m'"Relatorio gerado em 'relatorioCursos.txt'"'\033[0;0m')
    criaBarra()
    arquivo.close()
    return

def gerenciarCurso():
    limpaTerminal()
    lista_dados = []
    id = int(input(f'''\033[1;36mDigite o código do curso que deseja gerenciar: \033[0;0m'''))
    consulta = f"""SELECT * FROM curso WHERE id_curso = '{id}'"""
    inst_SQL.execute(consulta)
    dados = inst_SQL.fetchall()

    for dado in dados:
        lista_dados.append(dado)

        if (len(lista_dados) == 0):
            print('\033[1;31m''Erro! Código não encontrado ou inexistente.''\033[0; 0m')
        else:
            try:
                nome = input(f'''\033[1;36mDigite o novo nome do curso: \033[0;0m''')
                professor = input(f'''\033[1;36mDigite o nome do novo professor: \033[0;0m''')
                duracao = int(input(f'''\033[1;36mDigite a nova duração do curso: \033[0;0m'''))
                resumo = input(f'''\033[1;36mDigite a nova descrição do curso: \033[0;0m''')
                pontuacao = int(input(f'''\033[1;36mDigite a nova pontuação para o curso: \033[0;0m'''))
            except ValueError:
                print('\033[1;31m''Digite valores numericos''\033[0; 0m')
            else:
                try:
                    str_update = f"""UPDATE curso SET nome='{nome}',professor='{professor}',duracao={duracao},resumo='{resumo}',pontuacao={pontuacao} WHERE id_curso='{id}'"""
                    inst_SQL.execute(str_update)
                    conn.commit()
                except:
                    print('\033[1;31m''Erro de transacao com o BD''\033[0; 0m')
                else:
                    print(f'''\033[1;32mDados alterados com sucesso\033[0;0m''')
    subMenuCursos()


def removeCurso():
    limpaTerminal()
    print('=== << ''\033[1; 33m''Dados do Curso''\033[0;0m'' >> ===')
    criaBarra()
    print('\033[1;33m''Digite o código do Curso para excluir''\033[0; 0m')
    criaBarra()
    codigo = input('Código: ')

    valida = False

    dados = f"""SELECT * FROM curso WHERE id_curso = '{codigo}'"""
    inst_SQL.execute(dados)
    listaCurso = inst_SQL.fetchall()
    if (len(listaCurso) != 0):
        limpaTerminal()
        criaBarra()
        print('\033[1;32m''Curso encontrado! Excluindo... ''\033[0; 0m')
        criaBarra()
        sleep(5)
        # Excluir curso
        delete_query = f"""DELETE FROM curso WHERE id_curso = '{codigo}'"""
        inst_SQL.execute(delete_query)
        conn.commit()
        print('\033[1;32m''Curso Excluido! ''\033[0; 0m')
        criaBarra()
        valida = True
    else:
        valida = False

    if not valida:
        limpaTerminal()
        criaBarra()
        print('\033[1;31m''Erro! Código inválido ou inexistente''\033[0; 0m')
        criaBarra()
        subMenuCursos()
