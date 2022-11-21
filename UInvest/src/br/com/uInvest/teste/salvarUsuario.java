package br.com.uInvest.teste;

import br.com.uInvest.beans.Usuario;

import javax.swing.*;

public class salvarUsuario {
    public static void main(String[] args) {

        Usuario usuario = new Usuario();

        int nUsuarios = 3;
        for (int i = 0; i < nUsuarios; i++) {
            usuario.cadastrar(usuario);
        }

    }
}