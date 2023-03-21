package model;

public class Certificado {

    private String nome_curso;
    private String nome_aluno;
    private String assinatura_plat;
    private String carga_horaria;
    private String dt_emissao;
    private String dt_conclusao;
    private String id_certificado;
    private String nome_professor;

    public Certificado() {}

    public Certificado(String nome_curso, String nome_aluno, String assinatura_plat, String carga_horaria, String dt_emissao, String dt_conclusao, String id_certificado, String nome_professor) {
        this.nome_curso = nome_curso;
        this.nome_aluno = nome_aluno;
        this.assinatura_plat = assinatura_plat;
        this.carga_horaria = carga_horaria;
        this.dt_emissao = dt_emissao;
        this.dt_conclusao = dt_conclusao;
        this.id_certificado = id_certificado;
        this.nome_professor = nome_professor;
    }

    public String getNome_curso() {
        return nome_curso;
    }

    public void setNome_curso(String nome_curso) {
        this.nome_curso = nome_curso;
    }

    public String getNome_aluno() {
        return nome_aluno;
    }

    public void setNome_aluno(String nome_aluno) {
        this.nome_aluno = nome_aluno;
    }

    public String getAssinatura_plat() {
        return assinatura_plat;
    }

    public void setAssinatura_plat(String assinatura_plat) {
        this.assinatura_plat = assinatura_plat;
    }

    public String getCarga_horaria() {
        return carga_horaria;
    }

    public void setCarga_horaria(String carga_horaria) {
        this.carga_horaria = carga_horaria;
    }

    public String getDt_emissao() {
        return dt_emissao;
    }

    public void setDt_emissao(String dt_emissao) {
        this.dt_emissao = dt_emissao;
    }

    public String getDt_conclusao() {
        return dt_conclusao;
    }

    public void setDt_conclusao(String dt_conclusao) {
        this.dt_conclusao = dt_conclusao;
    }

    public String getId_certificado() {
        return id_certificado;
    }

    public void setId_certificado(String id_certificado) {
        this.id_certificado = id_certificado;
    }

    public String getNome_professor() {
        return nome_professor;
    }

    public void setNome_professor(String nome_professor) {
        this.nome_professor = nome_professor;
    }

    @Override
    public String toString() {
        return "Certificado{" +
                "nome_curso='" + nome_curso + '\'' +
                ", nome_aluno='" + nome_aluno + '\'' +
                ", assinatura_plat='" + assinatura_plat + '\'' +
                ", carga_horaria='" + carga_horaria + '\'' +
                ", dt_emissao='" + dt_emissao + '\'' +
                ", dt_conclusao='" + dt_conclusao + '\'' +
                ", id_certificado='" + id_certificado + '\'' +
                ", nome_professor='" + nome_professor + '\'' +
                '}';
    }
}
