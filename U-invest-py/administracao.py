def main():
    usuarioTemporario = {'nome': 'Matheus', 'user': 'Matpierro', 'email': 'matheus@mail.com', 'idade': 19,
                         'endereco': 'av. Paulista', 'cpf': 52867130840, 'celular': 3128391283, 'senha': 'matheusLindo'}
    usuarios = {}

    cadastraUsuario(usuarioTemporario, usuarios)


def cadastraUsuario(usuarioTemporario, usuarios):
    usuarios[usuarioTemporario['user']] = {'nome': usuarioTemporario['nome'], 'user': usuarioTemporario['user'], 'email': usuarioTemporario['email'], 'idade': usuarioTemporario['idade'],
                                           'endereco': usuarioTemporario['endereco'], 'cpf': usuarioTemporario['cpf'], 'celular': usuarioTemporario['celular'], 'senha': usuarioTemporario['senha']}
    print(usuarios)
    return usuarios


if (__name__ == "__main__"):
    main()


# Função original para quando não formos usar mais o usuário temporário!
# def recebeDadosUsuario():
#     nome = input("Nome e Sobrenome: ")
#     user = input("Crie um User: ")
#     email = input("Digite seu E-Mail: ")
#     idade = int(input("Idade: "))
#     endereco = input("Endereço: ")
#     cpf = int(input("CPF(Apenas Números): "))
#     celular = int(input("Digite seu número de telefone: "))
#     senha = input("Crie uma senha: ")

#     usuario = {'nome': nome, 'user': user, 'email': email, 'idade': idade, 'endereco': endereco,
#                'cpf': cpf, 'celular': celular, 'senha': senha}
#     return usuario
