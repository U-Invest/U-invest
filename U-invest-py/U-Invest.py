'''
v0.2
'''


def main():
    saida = 1
    saidaLogin = 1

    usuarios = {}

    while (saida != 0):
        print("1 - Cadastro de Usuario")
        print("2 - Login Usuario")
        print("3 - Exibir Usuarios")
        print("4 - Deletar Minha Conta")
        print("5 - Simulador de Investimentos (Em Breve)")
        opcao = int(input("Digite a opção desejada: "))
        if (opcao == 1):
            cadastraUsuario(recebeDadosUsuario(), usuarios)
        elif (opcao == 2):
            user = input("Digite seu User: ")
            if (user in usuarios):
                senha = input("Digite sua senha: ")
            else:
                print("User não encontrado, Tente novamente")
            if (senha in usuarios[user]['senha']):
                print("Você esta logado!")
                while (saidaLogin != 0):
                    print("1 - Editar usuario")
                    print("2 - Ver meu perfil")
                    opcaoLogin = int(input("Digite a opção desejada: "))
                    if (opcaoLogin == 1):
                        user = input("Digite seu User: ")
                        if (user in usuarios):
                            usuarios[user]['nome'] = input(
                                "Edite seu Nome e Sobrenome: ")
                            usuarios[user]['email'] = input(
                                "Edite seu E-Mail:")
                            usuarios[user]['idade'] = int(
                                input("Edite sua Idade: "))
                            usuarios[user]['endereco'] = input(
                                "Edite seu Endereço: ")
                            usuarios[user]['cpf'] = int(
                                input("Edite seu CPF: "))
                            usuarios[user]['celular'] = int(
                                input("Edite seu número de telefone: "))
                            usuarios[user]['senha'] = input(
                                "Edite sua Senha: ")
                    if (opcaoLogin == 2):
                        print(usuarios[user])
                    saidaLogin = int(
                        input("Deseja Continuar Logado? (1-SIM / 0-NÃO): "))
        elif (opcao == 3):
            print(usuarios)
        elif (opcao == 4):
            user = input("Digite seu User: ")
            if (user in usuarios):
                senha = input("Digite sua senha: ")
                if (senha in usuarios[user]['senha']):
                    print("Você tem certeza que deseja deletar sua conta?")
                    opcaoDelete = input("Digite (Sim) caso tenha certeza: ")
                    if (opcaoDelete == "Sim") or (opcaoDelete == "s") or (opcaoDelete == "sim"):
                        user = input(
                            "Digite seu User para deletar sua conta: ")
                        del usuarios[user]
                        print("Sua conta foi deletada com sucesso")
                    else:
                        print(
                            "Você cancelou a operação ou errou seu User, tente novamente caso deseje excluir sua conta.")
        elif (opcao == 5):
            print("No momento estamos contrução, como uma ação sobe e desce todos os dias e a taxa da bolsa tambem, " "\n"
                  "para realizarmos o calculo teriamos que ter api's que deixem nosso sistema conectado em tempo real com a B3. " "\n")
        # qntInvestir = float(input("Quanto você irá investir? "))
        # tempoEstimado = int(input("Qual é o tempo desejado? (Digite o/os meses em numeros)"))
        # investimentoMensal = input("Deseja investir mensalmente? Se deseja, digite quanto investira mensalmente:")
        # resultadoInvestimento =

        saida = int(input("Deseja Continuar? (1-SIM / 0-NÃO): "))
        saidaLogin = 1


def recebeDadosUsuario():
    nome = input("Nome e Sobrenome: ")
    user = input("Crie um User: ")
    email = input("Digite seu E-Mail: ")
    idade = int(input("Idade: "))
    endereco = input("Endereço: ")
    cpf = int(input("CPF(Apenas Números): "))
    numCelular = int(input("Digite seu número de telefone: "))
    senha = input("Crie uma senha: ")

    usuario = {'nome': nome, 'user': user, 'email': email, 'idade': idade, 'endereco': endereco,
               'cpf': cpf, 'celular': numCelular, 'senha': 'matheusLindo'}
    return usuario


def cadastraUsuario(usuario, usuarios):
    usuarios[usuario['user']] = {'nome': usuario['nome'], 'user': usuario['user'], 'email': usuario['email'], 'idade': usuario['idade'],
                                 'endereco': usuario['endereco'], 'cpf': usuario['cpf'], 'celular': usuario['numCelular'], 'senha': usuario['senha']}


if (__name__ == "__main__"):
    main()

    {'nome': 'Matheus', 'user': 'Matpierro', 'email': 'matheus@mail.com', 'idade': 19,
        'endereco': 'av. Paulista', 'cpf': 52867130840, 'celular': 3128391283, 'senha': senha}