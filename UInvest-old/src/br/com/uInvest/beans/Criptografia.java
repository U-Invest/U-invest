package br.com.uInvest.beans;

import java.math.BigInteger;
import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;

public class Criptografia {

    private String senha;
    private String senhaEncriptada;

    public Criptografia() {
    }

    public Criptografia(String senha, String senhaEncriptada) {
        this.senha = senha;
        this.senhaEncriptada = senhaEncriptada;
    }

    public String getSenha() {
        return senha;
    }

    public void setSenha(String senha) {
        this.senha = senha;
    }

    public String getSenhaEncriptada() {
        return senhaEncriptada;
    }

    public void setSenhaEncriptada(String senhaEncriptada) {
        this.senhaEncriptada = senhaEncriptada;
    }

    public static String encriptacao(String senha) {
        String retorno = "";
        MessageDigest md;
        try {
            md = MessageDigest.getInstance("MD5");
            BigInteger hash = new BigInteger(1, md.digest(senha.getBytes()));
            retorno = hash.toString(16);
        }
        catch (Exception e){}

        return retorno;
    }

    public void decriptacao() {
        System.out.println("Método para decriptar a senha");
    }
}
