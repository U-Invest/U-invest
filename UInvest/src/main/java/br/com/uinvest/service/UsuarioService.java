package br.com.uinvest.service;

public class UsuarioService {
    public boolean validarDadosUsuario(String cpf, String email, String celular, String nome, String senha, String perfilInvestidor, String user, String nascimento) {
        boolean dadosValidos = true;

        // Validar o nome
        if (nome == null || nome.trim().equals("")) {
            dadosValidos = false;
        }

        // Validar o e-mail
        if (email == null || email.trim().equals("")) {
            dadosValidos = false;
        }

        // Validar a senha
        if (senha == null || senha.trim().equals("")) {
            dadosValidos = false;
        }

        // Validar o user
        if (user == null || user.trim().equals("")) {
            dadosValidos = false;
        }

        // Validar o celular
        if (celular == null || celular.trim().equals("")) {
            dadosValidos = false;
        }

        // Validar o CPF
        if (cpf == null || cpf.trim().equals("")) {
            dadosValidos = false;
        }

        // Validar o CPF
        if (nascimento == null || nascimento.trim().equals("")) {
            dadosValidos = false;
        }

        // Validar o perfil do investidor
        if (perfilInvestidor == null || perfilInvestidor.trim().equals("")) {
            dadosValidos = false;
        }

        return dadosValidos;
    }
}