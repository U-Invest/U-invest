package br.com.uinvest.teste;

import br.com.uinvest.controller.LoginController;

public class Logar {
    public static void main(String[] args) throws InterruptedException {
        LoginController loginController = new LoginController();
        loginController.autenticarUsuario();

        Thread.sleep(10000);
        loginController.logout();
    }
}