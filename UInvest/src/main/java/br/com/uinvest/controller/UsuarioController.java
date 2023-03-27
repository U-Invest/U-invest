package br.com.uinvest.controller;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.sql.Connection;

import br.com.uinvest.connection.Conexao;
import br.com.uinvest.dao.UsuarioDAO;
import br.com.uinvest.model.Usuario;
import br.com.uinvest.service.UsuarioService;

import javax.swing.*;

public class UsuarioController {
    public void cadastrarUsuario(){
        Connection con = Conexao.abrirConexao();
        Usuario usuario = new Usuario();
        UsuarioDAO usuarioDAO = new UsuarioDAO(con);
        UsuarioService usuarioService = new UsuarioService();

        String nome = JOptionPane.showInputDialog("Qual é o seu nome?");
        String email =JOptionPane.showInputDialog("Qual é o seu email?");
        String senha = JOptionPane.showInputDialog("Qual é a sua senha?");
        String user = JOptionPane.showInputDialog("Qual é o seu user?");
        String celular = JOptionPane.showInputDialog("Qual é o seu celular?");
        String cpf = JOptionPane.showInputDialog("Qual é o seu cpf?");
        String nascimento = JOptionPane.showInputDialog("Qual é a sua Data de Nascimento?");
        String perfil_investidor = JOptionPane.showInputDialog("Qual é o seu nivel de investidor?");

        // Cria um objeto MessageDigest para calcular o hash SHA-256 da senha
        MessageDigest digest;
        try {
            digest = MessageDigest.getInstance("SHA-256");
        } catch (NoSuchAlgorithmException e) {
            e.printStackTrace();
            return;
        }

        // Encripta a senha usando o hash SHA-256
        byte[] hashSenha = digest.digest(senha.getBytes());

        // Converte o hash da senha para uma string hexadecimal de 20 caracteres
        StringBuilder hexString = new StringBuilder();
        for (int i = 0; i < hashSenha.length && i < 10; i++) {
            String hex = Integer.toHexString(0xff & hashSenha[i]);
            hexString.append(hex);
        }
        String senhaEncriptada = hexString.toString();

        if (usuarioService.validarDadosUsuario(cpf, email, celular, nome, senha, perfil_investidor, user, nascimento)) {
            usuario.setNome(nome);
            usuario.setEmail(email);
            usuario.setSenha(senhaEncriptada);
            usuario.setUser(user);
            usuario.setCelular(celular);
            usuario.setCpf(cpf);
            usuario.setNascimento(nascimento);
            usuario.setPerfil_investidor(perfil_investidor);
            usuario.setSaldo(0);

            System.out.println(usuarioDAO.inserir(usuario));
        } else {
            System.out.println("Os dados do usuário não são válidos.");
        }
        Conexao.fecharConexao(con);
    }
}
