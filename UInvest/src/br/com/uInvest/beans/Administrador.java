package br.com.uInvest.beans;

public class Administrador extends Usuario{
    
    private String admId;

    public Administrador() {}

    public Administrador(String nomeUsuario, String email, String telefone, String senha, String genero,
            String dataNascimento, int cep, String logradouro, String bairro, String cidade, String estado, int cpf,
            String admId) {
        super(nomeUsuario, email, telefone, senha, genero, dataNascimento, cep, logradouro, bairro, cidade, estado,
                cpf);
        this.admId = admId;
    }

    public String getAdmId() {
        return admId;
    }

    public void setAdmId(String admId) {
        this.admId = admId;
    }

    public void adicionarConteudo(){
        System.out.println("Método de Adicionar conteúdo");
    }
    
    public void excluirConteudo(){
        System.out.println("Método de excluir conteúdo");
    }

    public void alterarConteudo(){
        System.out.println("Método de alterar conteúdo");
    }

    public void loginAdm(){
        System.out.println("Método de Login do Administrador");
    }
}
