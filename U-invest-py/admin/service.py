from prettytable import PrettyTable
import random


def PerfilInvestidor():
    tabela = PrettyTable()
    tabela.field_names = ["Iniciante", "Conservador", "Experiente"]
    # Adiciona linhas à tabela
    tabela.add_row(["CDB", "CDB", "Ações e Fundos de Ações"])
    tabela.add_row(
        ["Tesouro Direto", "Tesouro Direto", "CDB e Tesouro Direto"])
    tabela.add_row(["Fundos de Renda Fixa", "Fundos de Renda Fixa e Fundos Multimercado",
                   "Fundos Imobiliários e Fundos Multimercado"])
    tabela.add_row([" ", " ", "Fundos Cambiais e Fundos de Renda Fixa"])
    print(tabela)
    while True:
        print('Qual perfil de investidor você se identificou?')
        try:
            perfil = int(
                input("1 - Iniciante \n2 - Conservador \n3 - Experiente\n"))
            if (perfil > 0) and (perfil < 4):
                if (perfil == 1):
                    perfil = "Iniciante"
                elif (perfil == 2):
                    perfil = "Conservador"
                else:
                    perfil = "Experiente"
                return perfil
            else:
                print("Error! Digite um perfil de investidor válido.")
        except:
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


def Professor():
    while True:
        nome = input('Nome e Sobrenome do Professor que ministra as aulas: ')
        if nome.strip() == "":
            print("Error! Digite um nome válido!")
        else:
            return nome


def CdCurso():
    codigo = random.randint(0, 99999999)
    while len(str(codigo)) < 8:
        codigo = '0' + str(codigo)
    return str(codigo)


def DuracaoCurso():
    while True:
        duracao = input("Qual é a duração do curso? (em horas) ")
        try:
            duracao = int(duracao)
            if duracao <= 0:
                print("A duração do curso deve ser maior do que zero. Tente novamente.")
            elif duracao > 100:
                print("A duração do curso não pode exceder 100 horas. Tente novamente.")
            else:
                return duracao
        except ValueError:
            print(
                "Por favor, insira um número inteiro válido para a duração do curso. Tente novamente.")


def NomeCurso():
    while True:
        nomeCurso = input('Digite o Nome do Curso: ')
        if nomeCurso.strip() == "":
            print('Error! Entrada Vazia!')
        else:
            return nomeCurso


def PontuacaoCurso(duracaoCurso):
    if duracaoCurso < 10:
        pontuacao = duracaoCurso * 0.5
    elif duracaoCurso < 20:
        pontuacao = duracaoCurso * 0.75
    elif duracaoCurso < 30:
        pontuacao = duracaoCurso * 1.0
    else:
        pontuacao = duracaoCurso * 1.25
    return int(pontuacao)


def AvaliacaoCurso(avaliacoes):
    if not avaliacoes:
        return 0

    avaliacoesFiltradas = [
        nota for nota in avaliacoes if nota >= 0 and nota <= 5]

    if not avaliacoesFiltradas:
        return 0

    totalAvaliacoes = sum(avaliacoesFiltradas)
    mediaAvaliacoes = totalAvaliacoes / len(avaliacoesFiltradas)

    return int(mediaAvaliacoes)


def ResumoCurso():
    while True:
        resumo = input("Faça um breve resumo com relação ao Curso:\n")
        if resumo.strip() == "":
            print('Digite uma descrição válida.')
        else:
            return resumo
