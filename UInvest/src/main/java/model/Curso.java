package model;

public class Curso {
    private int duracao;
    private int avaliacao;
    private String resumo;
    private String nome_professor;
    private String nome;
    private String id_curso;
    private int recompensa;

    public Curso() {}

    public Curso(int duracao, int avaliacao, String resumo, String nome_professor, String nome, String id_curso, int recompensa) {
        this.duracao = duracao;
        this.avaliacao = avaliacao;
        this.resumo = resumo;
        this.nome_professor = nome_professor;
        this.nome = nome;
        this.id_curso = id_curso;
        this.recompensa = recompensa;
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

    public String getNome_professor() {
        return nome_professor;
    }

    public void setNome_professor(String nome_professor) {
        this.nome_professor = nome_professor;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getId_curso() {
        return id_curso;
    }

    public void setId_curso(String id_curso) {
        this.id_curso = id_curso;
    }

    public int getRecompensa() {
        return recompensa;
    }

    public void setRecompensa(int recompensa) {
        this.recompensa = recompensa;
    }

    @Override
    public String toString() {
        return "Curso{" +
                "duracao=" + duracao +
                ", avaliacao=" + avaliacao +
                ", resumo='" + resumo + '\'' +
                ", nome_professor='" + nome_professor + '\'' +
                ", nome='" + nome + '\'' +
                ", id_curso='" + id_curso + '\'' +
                ", recompensa=" + recompensa +
                '}';
    }
}
