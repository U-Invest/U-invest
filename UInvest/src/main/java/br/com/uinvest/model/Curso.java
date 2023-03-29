package br.com.uinvest.model;

public class Curso {
    private int duracao;
    private int avaliacao;
    private String resumo;
    private String professor;
    private String nome;
    private String id;
    private int pontuacao;

    public Curso() {
    }

    public Curso(int duracao, int avaliacao, String resumo, String professor, String nome, String id, int pontuacao) {
        this.duracao = duracao;
        this.avaliacao = avaliacao;
        this.resumo = resumo;
        this.professor = professor;
        this.nome = nome;
        this.id = id;
        this.pontuacao = pontuacao;
    }

    public int getDuracao() {
        return duracao;
    }

    public void setDuracao(int duracao) {
        this.duracao = duracao;
    }

    public int getAvaliacao() {
        return avaliacao;
    }

    public void setAvaliacao(int avaliacao) {
        this.avaliacao = avaliacao;
    }

    public String getResumo() {
        return resumo;
    }

    public void setResumo(String resumo) {
        this.resumo = resumo;
    }

    public String getProfessor() {
        return professor;
    }

    public void setProfessor(String professor) {
        this.professor = professor;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getId() {
        return id;
    }

    public void setId_curso(String id) {
        this.id = id;
    }

    public int getPontuacao() {
        return pontuacao;
    }

    public void setPontuacao(int pontuacao) {
        this.pontuacao = pontuacao;
    }

    @Override
    public String toString() {
        return "Curso{" +
                "duracao=" + duracao +
                ", avaliacao=" + avaliacao +
                ", resumo='" + resumo + '\'' +
                ", professor='" + professor + '\'' +
                ", nome='" + nome + '\'' +
                ", id='" + id + '\'' +
                ", pontuacao=" + pontuacao +
                '}';
    }
}
