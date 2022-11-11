package br.com.u_invest.beans;

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

    public void encriptacao() {
        System.out.println("Método para encriptar a senha");
    }

    public void decriptacao() {
        System.out.println("Método para decriptar a senha");
    }
}
