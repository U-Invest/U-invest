package br.com.uInvest.beans;

import com.fasterxml.jackson.databind.ObjectMapper;

import java.io.FileOutputStream;
import java.io.IOException;
import java.io.Serializable;
import java.util.ArrayList;
import java.util.List;

public class Usuario implements Serializable {
    private String nome;
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
    
    private String cpf;

    public Usuario() {}

    public Usuario(String nome, String email, String telefone, String senha, String genero, String dataNascimento,
            int cep, String logradouro, String bairro, String cidade, String estado, String cpf) {
        super();
        this.nome = nome;
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

    public String getCpf() {
        return cpf;
    }

    public void setCpf(String cpf) {
        this.cpf = cpf;
    }

    public void cadastrar(){
        List<Usuario> usuarios = new ArrayList<Usuario>();
        usuarios.add(new Usuario(getNome(), getEmail(), getTelefone(), getSenha(), getGenero(), getDataNascimento(), getCep(), getLogradouro(), getBairro(), getCidade(), getEstado(), getCpf()));

        for (Usuario usuario : usuarios){
            System.out.println(usuario);
        }

        String filename = "Usuarios.json";

        try{

            Usuarios listaUsuario = new Usuarios(usuarios);
            FileOutputStream fos = new FileOutputStream(filename);
            
            ObjectMapper mapper = new ObjectMapper();
            String jsonStr = mapper.writerWithDefaultPrettyPrinter().writeValueAsString(listaUsuario);
            fos.write(jsonStr.getBytes());

            fos.close();

        }catch (IOException e){
            e.printStackTrace();
        }
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
