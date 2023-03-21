package model;

public class Usuario {

    private String cpf;
    private String email;
    private String celular;
    private String nome;
    private int saldo;
    private String senha;
    private String perfil_investidor;

    public Usuario() {}

    public Usuario(String cpf, String email, String celular, String nome, int saldo, String senha, String perfil_investidor) {
        this.cpf = cpf;
        this.email = email;
        this.celular = celular;
        this.nome = nome;
        this.saldo = saldo;
        this.senha = senha;
        this.perfil_investidor = perfil_investidor;
    }

    public String getCpf() {
        return cpf;
    }

    public void setCpf(String cpf) {
        this.cpf = cpf;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getCelular() {
        return celular;
    }

    public void setCelular(String celular) {
        this.celular = celular;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public int getSaldo() {
        return saldo;
    }

    public void setSaldo(int saldo) {
        this.saldo = saldo;
    }

    public String getSenha() {
        return senha;
    }

    public void setSenha(String senha) {
        this.senha = senha;
    }

    public String getPerfil_investidor() {
        return perfil_investidor;
    }

    public void setPerfil_investidor(String perfil_investidor) {
        this.perfil_investidor = perfil_investidor;
    }

    @Override
    public String toString() {
        return "Usuario{" +
                "cpf='" + cpf + '\'' +
                ", email='" + email + '\'' +
                ", celular='" + celular + '\'' +
                ", nome='" + nome + '\'' +
                ", saldo=" + saldo +
                ", senha='" + senha + '\'' +
                ", perfil_investidor='" + perfil_investidor + '\'' +
                '}';
    }
}
