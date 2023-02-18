from time import sleep
import controller

controller.limpaTerminal()

while True:
    escolha = controller.menu()

    if escolha == '1':
        controller.cadastro()
    elif escolha == '2':
        controller.mostraDados()
    elif escolha == '3':
        controller.clientesCadastrados()
    elif escolha == '4':
        controller.relatorio()
    elif escolha == '5':
        controller.removerCliente()
    elif escolha == '0':
        print('\033[1;36m''Fechando administração...''\033[0;0m')
        sleep(5)
        break
    else:
        controller.limpaTerminal()
        controller.criaBarra()
        print('\033[1;31m''Insira uma opção válida!''\033[0;0m')
        controller.criaBarra()
