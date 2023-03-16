import controller

def main():
    controller.limpaTerminal()
    admValidated = controller.userAdminValidate()

    while admValidated:
        controller.menuInicial()

if __name__ == "__main__":
    main()