package br.com.uinvest.model;

public class Usuario {
    private String nome;
    private String email;
    private String senha;
    private String nickName;
    private String celular;
    private String cpf;
    private String nascimento; //DDmmYYYY
    private String perfil_investidor;
    private int saldo;

    public Usuario() {}

    public Usuario(String nome, String email, String senha, String nickName, String celular, String cpf, String nascimento, String perfil_investidor, int saldo) {
        this.nome = nome;
        this.email = email;
        this.senha = senha;
        this.nickName = nickName;
        this.celular = celular;
        this.cpf = cpf;
        this.nascimento = nascimento;
        this.perfil_investidor = perfil_investidor;
        this.saldo = saldo;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getSenha() {
        return senha;
    }

    public void setSenha(String senha) {
        this.senha = senha;
    }

    public String getNickName() {
        return nickName;
    }

    public void setNickName(String nickName) {
        this.nickName = nickName;
    }

    public String getCelular() {
        return celular;
    }

    public void setCelular(String celular) {
        this.celular = celular;
    }

    public String getCpf() {
        return cpf;
    }

    public void setCpf(String cpf) {
        this.cpf = cpf;
    }

    public String getNascimento() {
        return nascimento;
    }

    public void setNascimento(String nascimento) {
        this.nascimento = nascimento;
    }

    public String getPerfil_investidor() {
        return perfil_investidor;
    }

    public void setPerfil_investidor(String perfil_investidor) {
        this.perfil_investidor = perfil_investidor;
    }

    public int getSaldo() {
        return saldo;
    }

    public void setSaldo(int saldo) {
        this.saldo = saldo;
    }

    @Override
    public String toString() {
        return "Usuario{" +
                "nome='" + nome + '\'' +
                ", email='" + email + '\'' +
                ", senha='" + senha + '\'' +
                ", nickName='" + nickName + '\'' +
                ", celular='" + celular + '\'' +
                ", cpf='" + cpf + '\'' +
                ", nascimento='" + nascimento + '\'' +
                ", perfil_investidor='" + perfil_investidor + '\'' +
                ", saldo=" + saldo +
                '}';
    }
}
