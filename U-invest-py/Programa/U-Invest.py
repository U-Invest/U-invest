'''
v0.1
'''

saida = 1

uInvest = {}

while (saida != 0):
    print("1 - Cadastrar")
    print("2 - Logar")
    print("3 - Editar Perfil do Usuario")
    print("4 - Exibir Usuarios Cadastrados")
    opcao = int(input("Digite a opcao desejada: "))
    if (opcao == 1):
        nome = input("Nome e Sobrenome: ")
        user = input("Crie um UserName: ")
        idade = int(input("Idade: "))
        endereco = input("Endereço: ")
        cpf = int(input("CPF(Apenas Números): "))
        senha = input("Crie uma senha: ")
        uInvest[user] = {'nome': nome, 'user': user, 'idade': idade, 'endereco': endereco,
                          'cpf': cpf, 'senha': senha}
    elif (opcao == 2):
        user = input("Digite seu UserName: ")
        if (user in uInvest):
            senha = input("Digite sua senha: ")
            if (senha in uInvest[user]['senha']):
                print("Você esta logado!")
            else:
                print("Senha errada! Tente novamente")
    elif (opcao == 3):
        user = input("Digite seu User: ")
        if (user in uInvest):
            uInvest[user]['nome'] = input("Edite seu Nome e Sobrenome: ")
            uInvest[user]['idade'] = int(input("Edite sua Idade: "))
            uInvest[user]['endereco'] = input("Edite seu Endereço: ")
            uInvest[user]['cpf'] = int(input("Edite seu CPF: "))
            uInvest[user]['senha'] = input("Edite sua Senha: ")
        else:
            print("User não encontrado.")
    elif (opcao == 4):
        print(uInvest)

    saida = int(input("Deseja Continuar (1-SIM / 0-NÃO): "))

