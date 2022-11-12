package br.com.uInvest.beans;

public class Instituicao extends Usuario{
    private String nomeInstituicao;
    private String instituicaoId;
    private int cnpj;
    
    public Instituicao() {}

    public Instituicao(String nomeUsuario, String email, String telefone, String senha, String genero,
            String dataNascimento, int cep, String logradouro, String bairro, String cidade, String estado, int cpf,
            String nomeInstituicao, String instituicaoId, int cnpj) {
        super(nomeUsuario, email, telefone, senha, genero, dataNascimento, cep, logradouro, bairro, cidade, estado,
                cpf);
        this.nomeInstituicao = nomeInstituicao;
        this.instituicaoId = instituicaoId;
        this.cnpj = cnpj;
    }

    public String getNomeInstituicao() {
        return nomeInstituicao;
    }

    public void setNomeInstituicao(String nomeInstituicao) {
        this.nomeInstituicao = nomeInstituicao;
    }

    public String getInstituicaoId() {
        return instituicaoId;
    }

    public void setInstituicaoId(String instituicaoId) {
        this.instituicaoId = instituicaoId;
    }

    public int getCnpj() {
        return cnpj;
    }

    public void setCnpj(int cnpj) {
        this.cnpj = cnpj;
    }
    
    public void loginEmpresa(){
        System.out.println("Método de login empresa");
    }

    public void filtrarUsers(){
        System.out.println("Método de filtrar users");
    }

    public void visualizarUser(){
        System.out.println("Método de visualizar usuário");
    }
}