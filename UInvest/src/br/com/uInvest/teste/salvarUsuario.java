package br.com.uInvest.teste;

import br.com.uInvest.beans.Usuario;

import javax.swing.*;

public class salvarUsuario {
    public static void main(String[] args) {

        Usuario usuarioMocado = new Usuario();

        usuarioMocado.setNome(JOptionPane.showInputDialog("Cadastre seu nome"));
        usuarioMocado.setEmail(JOptionPane.showInputDialog("Cadastre seu E-mail"));
        usuarioMocado.setTelefone(JOptionPane.showInputDialog("Cadastre seu telefone"));
        usuarioMocado.setSenha(JOptionPane.showInputDialog("Cadastre sua senha"));
        usuarioMocado.setGenero(JOptionPane.showInputDialog("Cadastre seu gênero"));
        usuarioMocado.setDataNascimento(JOptionPane.showInputDialog("Cadastre sua data de nascimento"));
        usuarioMocado.setCep(Integer.parseInt(JOptionPane.showInputDialog("Cadastre seu CEP")));
        usuarioMocado.setLogradouro(JOptionPane.showInputDialog("Cadastre seu logradouro"));
        usuarioMocado.setBairro(JOptionPane.showInputDialog("Cadastre seu bairro"));
        usuarioMocado.setCidade(JOptionPane.showInputDialog("Cadastre sua cidade"));
        usuarioMocado.setEstado(JOptionPane.showInputDialog("Cadastre seu estado"));
        usuarioMocado.setCpf(JOptionPane.showInputDialog("Cadastre seu CPF"));

        usuarioMocado.cadastrar();
    }
}