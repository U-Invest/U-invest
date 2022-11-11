'''
v0.1
'''

saida = 1

saidaLogin = 1

uInvest = {}

while (saida != 0):
    print("1 - Cadastro de Usuario")
    print("2 - Login Usuario")
    print("3 - Login Admin")
    opcao = int(input("Digite a opção desejada: "))
    if (opcao == 1):
        nome = input("Nome e Sobrenome: ")
        user = input("Crie um UserName: ")
        email = input("Digite seu E-Mail: ")
        idade = int(input("Idade: "))
        endereco = input("Endereço: ")
        cpf = int(input("CPF(Apenas Números): "))
        numCelular = int(input("Digite seu número de telefone: "))
        senha = input("Crie uma senha: ")
        uInvest[user] = {'nome': nome, 'user': user, 'email': email, 'idade': idade, 'endereco': endereco,
                          'cpf': cpf, 'celular': numCelular, 'senha': senha}
    elif (opcao == 2):
        user = input("Digite seu UserName: ")
        if (user in uInvest):
            senha = input("Digite sua senha: ")
            if (senha in uInvest[user]['senha']):
                print("Você esta logado!")
            else:
                print("Senha errada! Tente novamente")
            while (saidaLogin != 0):
                print("1 - Editar usuario")
                print("2 - ")
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
                saidaLogin = int(input("Deseja Continuar Logado? (1-SIM / 0-NÃO): "))
    elif (opcao == 3):
        user = input("Digite seu User Administrador: ")
        if (0):
            print("Teste")
        else:
            print("User errado, ou você não é um Admin.")

    saida = int(input("Deseja Continuar? (1-SIM / 0-NÃO): "))

