package br.com.uinvest.controller;

import br.com.uinvest.connection.Conexao;
import br.com.uinvest.dao.LoginDAO;
import br.com.uinvest.dao.UsuarioDAO;
import br.com.uinvest.model.Login;
import br.com.uinvest.model.Usuario;

import javax.swing.*;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.sql.Connection;
import java.sql.SQLException;
import java.time.Duration;
import java.time.Instant;
import java.util.UUID;

import br.com.uinvest.service.LoginService;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpSession;

public class LoginController {

    private Instant inicioSessao;
    private Instant fimSessao;

    // Autentica um usuário com o nome ou email e a senha encriptada
    public boolean autenticarUsuario() {
        try (Connection con = Conexao.abrirConexao()) {
            UsuarioDAO usuarioDAO = new UsuarioDAO(con);

            String userOuEmail = JOptionPane.showInputDialog("Digite seu Nome de Usuario ou Email");
            String senha = JOptionPane.showInputDialog("Digite sua senha");

            Usuario usuario = usuarioDAO.buscarPorUserOuEmail(userOuEmail);
            if (usuario != null) {
                // Cria um objeto MessageDigest para calcular o hash SHA-256 da senha fornecida pelo usuário
                MessageDigest digest;
                try {
                    digest = MessageDigest.getInstance("SHA-256");
                } catch (NoSuchAlgorithmException e) {
                    e.printStackTrace();
                    return false;
                }

                // Encripta a senha fornecida pelo usuário usando o hash SHA-256
                byte[] hashSenha = digest.digest(senha.getBytes());

                // Converte o hash da senha para uma string hexadecimal
                StringBuilder hexString = new StringBuilder();
                for (int i = 0; i < hashSenha.length && i < 10; i++) {
                    String hex = Integer.toHexString(0xff & hashSenha[i]);
                    hexString.append(hex);
                }
                String senhaEncriptada = hexString.toString();

                // Compara a senha encriptada fornecida pelo usuário com a senha encriptada armazenada no banco de dados
                if (senhaEncriptada.equals(usuarioDAO.buscarSenha(senhaEncriptada))) {
                    registrarTempo("open"); // Inicia o cronômetro da sessao
                }
            }
            return false; // Autenticação mal-sucedida
        } catch (SQLException e) {
            e.printStackTrace();
            return false;
        }
    }

    public String criarIdSessao() {
        UUID uuid = UUID.randomUUID();
        String randomUUIDString = uuid.toString().replaceAll("-", "");
        return randomUUIDString.substring(0, 8);
    }

    public void logout() {
        Connection con = Conexao.abrirConexao();
        Login login = new Login();
        LoginDAO loginDAO = new LoginDAO(con);
        LoginService loginService = new LoginService();

        String id_sessao = criarIdSessao();
        String hrs_plataforma = "Em dev";
        String ultima_sessao = "Em dev";
        String hr_sessao_atual = "Em dev";

        if (loginService.formataDados()) {
            login.setId_sessao(id_sessao);
            login.setHrs_plataforma(hrs_plataforma);
            login.setUltima_sessao(ultima_sessao);
            login.setHr_sessao_atual(hr_sessao_atual);

            System.out.println(loginDAO.inserir(login));
        } else {
            System.out.println("Os dados do login não são válidos.");
        }
        Conexao.fecharConexao(con);
    }

    public Duration registrarTempo(String acao) {
        if (acao.equals("open")) {
            inicioSessao = Instant.now();
            System.out.println("Cronômetro iniciado.");
            return null;
        } else if (acao.equals("close")) {
            fimSessao = Instant.now();
            Duration registro = Duration.between(inicioSessao, fimSessao);
            System.out.println("Cronômetro parado. Tempo registrado: " + registro);
            return registro;
        } else {
            System.out.println("Ação inválida.");
            return null;
        }
    }
}


