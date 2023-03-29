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
import java.time.*;
import java.time.format.DateTimeFormatter;
import java.util.UUID;

import br.com.uinvest.service.LoginService;

public class LoginController {
    private LocalDateTime inicioSessao;
    private LocalDateTime fimSessao;

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
                    // inicia a sessão
                    registrarTempo("open");
                    System.out.println("Sessão iniciada para o usuário " + usuario);
                    System.out.println(inicioSessao);
                    Conexao.fecharConexao(con);
                } else {
                    Conexao.fecharConexao(con);
                    return false; // Autenticação mal-sucedida
                }
            }
        } catch (SQLException e) {
            e.printStackTrace();
            return false;
        }
        return false;
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

        String duracaoSessao = registrarTempo("close");
        if (duracaoSessao == null) {
            System.out.println("A duração da sessão é nula");
        }

        String id_sessao = criarIdSessao();
        int hrs_plataforma = 0;
        String ultima_sessao = "Em dev";
        System.out.println(duracaoSessao);

        if (loginService.formataDados()) {
            login.setId_sessao(id_sessao);
            login.setHrs_plataforma(hrs_plataforma);
            login.setUltima_sessao(ultima_sessao);
            login.setHr_sessao_atual(duracaoSessao);

            System.out.println(loginDAO.inserir(login));
        } else {
            System.out.println("Os dados do login não são válidos.");
        }
        Conexao.fecharConexao(con);
    }

    public String registrarTempo(String acao) {
        if (acao.equals("open")) {
            if (inicioSessao != null) {
                System.out.println("O cronômetro já foi iniciado.");
                return null;
            }
            inicioSessao = LocalDateTime.now();
            System.out.println("Cronômetro iniciado.");
            return null;
        } else if (acao.equals("close")) {
            if (inicioSessao == null) {
                System.out.println("O cronômetro ainda não foi iniciado.");
                return null;
            }
            fimSessao = LocalDateTime.now();
            Duration registro = Duration.between(inicioSessao, fimSessao);
            System.out.println("Cronômetro parado. Tempo registrado: " + registro);


            LocalDateTime referencia = inicioSessao.withHour(0).withMinute(0).withSecond(0).withNano(0); // define uma hora de referência, com os campos de hora, minuto, segundo e nanos zerados
            LocalDateTime dataHoraRegistro = referencia.plus(registro); // adiciona a duração ao instante de referência, para obter a data e hora final

            DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd HH:mm:ss");
            String dataHoraFormatada = formatter.format(dataHoraRegistro);

            // Reseta a variável para permitir que o cronômetro seja iniciado novamente
            inicioSessao = null;

            return dataHoraFormatada;
        } else {
            System.out.println("Ação inválida.");
            return null;
        }
    }
}


