package br.com.u_invest.beans;

public class Usuario {

    private String nomeUsuario;
    private String email;
    private String telefone;
    private String senha;
    private String genero;
    private String dataNascimento;
    private int cep;
    private String logradouro;
    private String bairro;
    private String cidade;
    private String estado;
    
    private int cpf;

    public Usuario() {}

    public Usuario(String nomeUsuario, String email, String telefone, String senha, String genero, String dataNascimento,
            int cep, String logradouro, String bairro, String cidade, String estado, int cpf) {
        this.nomeUsuario = nomeUsuario;
        this.email = email;
        this.telefone = telefone;
        this.senha = senha;
        this.genero = genero;
        this.dataNascimento = dataNascimento;
        this.cep = cep;
        this.logradouro = logradouro;
        this.bairro = bairro;
        this.cidade = cidade;
        this.estado = estado;
        this.cpf = cpf;
    }

    public String getNomeUsuario() {
        return nomeUsuario;
    }

    public void setNomeUsuario(String nomeUsuario) {
        this.nomeUsuario = nomeUsuario;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getTelefone() {
        return telefone;
    }

    public void setTelefone(String telefone) {
        this.telefone = telefone;
    }

    public String getSenha() {
        return senha;
    }

    public void setSenha(String senha) {
        this.senha = senha;
    }

    public String getGenero() {
        return genero;
    }

    public void setGenero(String genero) {
        this.genero = genero;
    }

    public String getDataNascimento() {
        return dataNascimento;
    }

    public void setDataNascimento(String dataNascimento) {
        this.dataNascimento = dataNascimento;
    }

    public int getCep() {
        return cep;
    }

    public void setCep(int cep) {
        this.cep = cep;
    }

    public String getLogradouro() {
        return logradouro;
    }

    public void setLogradouro(String logradouro) {
        this.logradouro = logradouro;
    }

    public String getBairro() {
        return bairro;
    }

    public void setBairro(String bairro) {
        this.bairro = bairro;
    }

    public String getCidade() {
        return cidade;
    }

    public void setCidade(String cidade) {
        this.cidade = cidade;
    }

    public String getEstado() {
        return estado;
    }

    public void setEstado(String estado) {
        this.estado = estado;
    }

    public int getCpf() {
        return cpf;
    }

    public void setCpf(int cpf) {
        this.cpf = cpf;
    }

    public void cadastrar(){
        System.out.println("Método de cadastro de usuário");
    }

    public void alterarDados(){
        System.out.println("Método de alterar dados do usuário");
    }

    public void excluirConta(){
        System.out.println("Método de excluir conta");
    }

    public void loginUser(){
        System.out.println("Método de login do usuário");
    }
}
