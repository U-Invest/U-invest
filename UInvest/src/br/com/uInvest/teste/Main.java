package br.com.uInvest.teste;

import br.com.uInvest.beans.*;

import javax.swing.*;

public class Main {
    public static void main(String[] args) {

        String recebeSenha = JOptionPane.showInputDialog("Digite sua senha");
        String recebeSenhaEncriptada = "*SKJH!$GASKJH#TnHDSGAHDA";

        Administrador adm = new Administrador();
        Aulas aulas = new Aulas();
        Certificado certificado = new Certificado();
        Contato contato = new Contato();
        Conteudo conteudo = new Conteudo();
        Criptografia criptografia = new Criptografia(recebeSenha, recebeSenhaEncriptada);
        Cursos cursos = new Cursos();
        Feedback feedback = new Feedback();
        Instituicao instituicao = new Instituicao();
        Simulador simulador = new Simulador();
        Usuario usuario = new Usuario();

        System.out.println(criptografia.getSenha() + "\n" + criptografia.getSenhaEncriptada());

    }
}
