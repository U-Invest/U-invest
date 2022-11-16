'''
v0.1
'''

saida = 1

saidaLogin = 1

saidaAdm = 1

uInvest = {}

while (saida != 0):
    print("1 - Cadastro de Usuario")
    print("2 - Login Usuario")
    print("3 - Exibir Usuarios")
    print("4 - Deletar Minha Conta")
    opcao = int(input("Digite a opção desejada: "))
    if (opcao == 1):
        nome = input("Nome e Sobrenome: ")
        user = input("Crie um User: ")
        email = input("Digite seu E-Mail: ")
        idade = int(input("Idade: "))
        endereco = input("Endereço: ")
        cpf = int(input("CPF(Apenas Números): "))
        numCelular = int(input("Digite seu número de telefone: "))
        senha = input("Crie uma senha: ")
        uInvest[user] = {'nome': nome, 'user': user, 'email': email, 'idade': idade, 'endereco': endereco,
                          'cpf': cpf, 'celular': numCelular, 'senha': senha}
    elif (opcao == 2):
        user = input("Digite seu User: ")
        if (user in uInvest):
            senha = input("Digite sua senha: ")
        else:
            print("User não encontrado, Tente novamente")
        if (senha in uInvest[user]['senha']):
            print("Você esta logado!")
            while (saidaLogin != 0):
                print("1 - Editar usuario")
                print("2 - Ver meu perfil")
                opcaoLogin = int(input("Digite a opção desejada: "))
                if (opcaoLogin == 1):
                    user = input("Digite seu User: ")
                    if (user in uInvest):
                        uInvest[user]['nome'] = input("Edite seu Nome e Sobrenome: ")
                        uInvest[user]['email'] = input("Edite seu E-Mail:")
                        uInvest[user]['idade'] = int(input("Edite sua Idade: "))
                        uInvest[user]['endereco'] = input("Edite seu Endereço: ")
                        uInvest[user]['cpf'] = int(input("Edite seu CPF: "))
                        uInvest[user]['celular'] = int(input("Edite seu número de telefone: "))
                        uInvest[user]['senha'] = input("Edite sua Senha: ")
                if (opcaoLogin == 2):
                    print(uInvest[user])
                saidaLogin = int(input("Deseja Continuar Logado? (1-SIM / 0-NÃO): "))
    elif (opcao == 3):
        print(uInvest)
    elif (opcao == 4):
        user = input("Digite seu User: ")
        if (user in uInvest):
            senha = input("Digite sua senha: ")
            if (senha in uInvest[user]['senha']):
                print("Você tem certeza que deseja deletar sua conta?")
                opcaoDelete = input("Digite (Sim) caso tenha certeza: ")
                if (opcaoDelete == "Sim") or (opcaoDelete == "s") or (opcaoDelete == "sim"):
                    user = input("Digite seu User para deletar sua conta: ")
                    del uInvest[user]
                    print("Sua conta foi deletada com sucesso")
                else:
                    print("Você cancelou a operação ou errou seu User, tente novamente caso deseje excluir sua conta.") 

    saida = int(input("Deseja Continuar? (1-SIM / 0-NÃO): "))
    saidaLogin = 1
    saidaAdm = 1