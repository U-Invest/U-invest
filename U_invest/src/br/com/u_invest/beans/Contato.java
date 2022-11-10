package br.com.u_invest.beans;

public class Contato {

    private String contato;
    private int telefone;
    private String redeSocial;

    public Contato(){
    }

    public Contato(String contato, int telefone, String redeSocial) {
        this.contato = contato;
        this.telefone = telefone;
        this.redeSocial = redeSocial;
    }

    public String getContato() {
        return contato;
    }

    public void setContato(String contato) {
        this.contato = contato;
    }

    public int getTelefone() {
        return telefone;
    }

    public void setTelefone(int telefone) {
        this.telefone = telefone;
    }

    public String getRedeSocial() {
        return redeSocial;
    }

    public void setRedeSocial(String redeSocial) {
        this.redeSocial = redeSocial;
    }
}
