package br.com.uinvest.controller;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.sql.Connection;

import br.com.uinvest.connection.Conexao;
import br.com.uinvest.dao.UsuarioDAO;
import br.com.uinvest.model.Usuario;
import br.com.uinvest.service.UsuarioService;
import com.google.gson.Gson;

import javax.swing.*;

public class UsuarioController {
    public void cadastrarUsuario(){
        Connection con = Conexao.abrirConexao();
        Usuario usuario = new Usuario();
        UsuarioDAO usuarioDAO = new UsuarioDAO(con);
        UsuarioService usuarioService = new UsuarioService();

        String nome = JOptionPane.showInputDialog("Qual é o seu nome?");
        String email =JOptionPane.showInputDialog("Qual é o seu email? Ex: email@gmail.com");
        String senha = JOptionPane.showInputDialog("Qual é a sua senha?");
        String nickName = JOptionPane.showInputDialog("Qual é o seu nick name?");
        String celular = JOptionPane.showInputDialog("Qual é o seu celular? (Com DDD)");
        String cpf = JOptionPane.showInputDialog("Qual é o seu cpf? Ex: 12345678910");
        String nascimento = JOptionPane.showInputDialog("Qual é a sua Data de Nascimento? (DDmmYYYY)");
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

        if (usuarioService.validarDadosUsuario(cpf, email, celular, nome, senha, perfil_investidor, nickName, nascimento)) {
            usuario.setNome(nome);
            usuario.setEmail(email);
            usuario.setSenha(senhaEncriptada);
            usuario.setNickName(nickName);
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

    public boolean cadastrarUsuarioFront(String json){
        Connection con = Conexao.abrirConexao();
        UsuarioDAO usuarioDAO = new UsuarioDAO(con);
        UsuarioService usuarioService = new UsuarioService();
        Gson gson = new Gson();
        Usuario usuario = gson.fromJson(json, Usuario.class);

        String nome = usuario.getNome();
        String email = usuario.getEmail();
        String senha = usuario.getSenha();
        String nickName = usuario.getNickName();
        String celular = usuario.getCelular();
        String cpf = usuario.getCpf();
        String nascimento = usuario.getNascimento();
        String perfil_investidor = usuario.getPerfil_investidor();

        // Cria um objeto MessageDigest para calcular o hash SHA-256 da senha
        MessageDigest digest;
        try {
            digest = MessageDigest.getInstance("SHA-256");
        } catch (NoSuchAlgorithmException e) {
            e.printStackTrace();
            return false;
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

        if (usuarioService.validarDadosUsuario(cpf, email, celular, nome, senha, perfil_investidor, nickName, nascimento)) {
            usuario.setNome(nome);
            usuario.setEmail(email);
            usuario.setSenha(senhaEncriptada);
            usuario.setNickName(nickName);
            usuario.setCelular(celular);
            usuario.setCpf(cpf);
            usuario.setNascimento(nascimento);
            usuario.setPerfil_investidor(perfil_investidor);
            usuario.setSaldo(0);

            System.out.println(usuarioDAO.inserir(usuario));

        } else {
            System.out.println("Os dados do usuário não são válidos.");
            return false;
        }
        Conexao.fecharConexao(con);
        return true;
    }

//    public void meuPerfil(){
//        Connection con = Conexao.abrirConexao();
//        UsuarioDAO usuariodao = new UsuarioDAO(con);
//        ArrayList<Usuario> lista = usuariodao.exibirDadosUsuario();
//        if(lista != null) {
//            for(Usuario usuario : lista ) {
//                System.out.print(usuario.getNome() + " ");
//                System.out.print(usuario.getEmail() + " ");
//                System.out.print(usuario.getSenha() + " ");
//                System.out.print(usuario.getNickName() + " ");
//                System.out.print(usuario.getCelular() + " ");
//                System.out.print(usuario.getCpf() + " ");
//                System.out.print(usuario.getNascimento() + " ");
//                System.out.print(usuario.getPerfil_investidor() + " ");
//                System.out.println(usuario.getSaldo());
//            }
//        }
//        else {
//            System.out.println();
//        }
//    }
}
