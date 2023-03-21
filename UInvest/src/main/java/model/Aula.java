package model;

public class Aula {
    private String tipo_conteudo;
    private String duracao;
    private String nome_aula;
    private String id_aula;
    private String conteudo;
    private int avaliacao;

    public Aula() {}

    public Aula(String tipo_conteudo, String duracao, String nome_aula, String id_aula, String conteudo, int avaliacao) {
        this.tipo_conteudo = tipo_conteudo;
        this.duracao = duracao;
        this.nome_aula = nome_aula;
        this.id_aula = id_aula;
        this.conteudo = conteudo;
        this.avaliacao = avaliacao;
    }

    public String getTipo_conteudo() {
        return tipo_conteudo;
    }

    public void setTipo_conteudo(String tipo_conteudo) {
        this.tipo_conteudo = tipo_conteudo;
    }

    public String getDuracao() {
        return duracao;
    }

    public void setDuracao(String duracao) {
        this.duracao = duracao;
    }

    public String getNome_aula() {
        return nome_aula;
    }

    public void setNome_aula(String nome_aula) {
        this.nome_aula = nome_aula;
    }

    public String getId_aula() {
        return id_aula;
    }

    public void setId_aula(String id_aula) {
        this.id_aula = id_aula;
    }

    public String getConteudo() {
        return conteudo;
    }

    public void setConteudo(String conteudo) {
        this.conteudo = conteudo;
    }

    public int getAvaliacao() {
        return avaliacao;
    }

    public void setAvaliacao(int avaliacao) {
        this.avaliacao = avaliacao;
    }

    @Override
    public String toString() {
        return "Aula{" +
                "tipo_conteudo='" + tipo_conteudo + '\'' +
                ", duracao='" + duracao + '\'' +
                ", nome_aula='" + nome_aula + '\'' +
                ", id_aula='" + id_aula + '\'' +
                ", conteudo='" + conteudo + '\'' +
                ", avaliacao=" + avaliacao +
                '}';
    }
}
