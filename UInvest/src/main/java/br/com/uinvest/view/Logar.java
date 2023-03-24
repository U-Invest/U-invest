package br.com.uinvest.view;

import br.com.uinvest.controller.LoginController;

public class Logar {
    public static void main(String[] args) {
        LoginController loginController = new LoginController();
        loginController.autenticarUsuario();
    }
}