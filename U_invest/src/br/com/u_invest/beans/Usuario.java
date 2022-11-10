package br.com.u_invest.beans;

public class Usuario extends Instituicao {

    private String nomeUsuario;
    private int cpf;
    private int telefone;
    private String email;
    public Usuario(){}

    public Usuario(String nomeInstituicao, String nomeUsuario, int cpf, int telefone, String email) {
        super(nomeInstituicao);
        this.nomeUsuario = nomeUsuario;
        this.cpf = cpf;
        this.telefone = telefone;
        this.email = email;
    }

    public String getNomeUsuario() {
        return nomeUsuario;
    }

    public void setNomeUsuario(String nomeUsuario) {
        this.nomeUsuario = nomeUsuario;
    }

    public int getCpf() {
        return cpf;
    }

    public void setCpf(int cpf) {
        this.cpf = cpf;
    }

    public int getTelefone() {
        return telefone;
    }

    public void setTelefone(int telefone) {
        this.telefone = telefone;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
}
