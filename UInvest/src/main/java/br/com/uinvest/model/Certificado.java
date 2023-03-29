package br.com.uinvest.model;

public class Certificado extends Curso{

    private String nome_aluno;
    private String assinatura_plat;
    private String dt_emissao; //DDmmYYYY
    private String dt_conclusao; //DDmmYYYY
    private String id_certificado;

    public Certificado() {
    }

    public Certificado(int duracao, int avaliacao, String resumo, String professor, String nome, String id, int pontuacao, String nome_aluno, String assinatura_plat, String dt_emissao, String dt_conclusao, String id_certificado) {
        super(duracao, avaliacao, resumo, professor, nome, id, pontuacao);
        this.nome_aluno = nome_aluno;
        this.assinatura_plat = assinatura_plat;
        this.dt_emissao = dt_emissao;
        this.dt_conclusao = dt_conclusao;
        this.id_certificado = id_certificado;
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

    @Override
    public String toString() {
        return "Certificado{" +
                "nome_aluno='" + nome_aluno + '\'' +
                ", assinatura_plat='" + assinatura_plat + '\'' +
                ", dt_emissao='" + dt_emissao + '\'' +
                ", dt_conclusao='" + dt_conclusao + '\'' +
                ", id_certificado='" + id_certificado + '\'' +
                '}';
    }
}
