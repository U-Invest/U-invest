from time import sleep
import controller

controller.limpaTerminal()

admValidated = controller.userAdminValidate()

while admValidated:
    escolha = controller.menuInicial()
    if escolha == '1':
        subEscolha = controller.subMenuUsuarios()
        if subEscolha == '1':
            controller.cadastro()
        elif subEscolha == '2':
            controller.mostraDados()
        elif subEscolha == '3':
            controller.usuariosCadastrados()
        elif subEscolha == '4':
            controller.relatorio()
        elif subEscolha == '5':
            controller.removerUsuario()
        elif subEscolha == '0':
            sleep(2)
            controller.menuInicial()#não funciona ainda
        else:
            controller.limpaTerminal()
            controller.criaBarra()
            print('\033[1;31m''Insira uma opção válida!''\033[0;0m')
            controller.criaBarra()

    elif escolha == '2':
        print('\033[1;36m''Em Desenvolvimento...''\033[0;0m')
        controller.subMenuCursos()
    elif escolha == '3':
        print('\033[1;36m''Em Desenvolvimento...''\033[0;0m')
        controller.subMenuDocs()
    elif escolha == '0':
        print('\033[1;36m''Fechando administração...''\033[0;0m')
        sleep(5)
        break
    else:
        controller.limpaTerminal()
        controller.criaBarra()
        print('\033[1;31m''Insira uma opção válida!''\033[0;0m')
        controller.criaBarra()
