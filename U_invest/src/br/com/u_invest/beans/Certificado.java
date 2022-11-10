package br.com.u_invest.beans;

public class Certificado extends Cursos {

    private String tipoCertificado;
    private String nomeAluno;
    private String nomeProfessor;
    private String conteudoCertificado;

    public Certificado(){}

    public Certificado(String nomeCurso, int cargaHoraria, String tipoCertificado, String nomeAluno, String nomeProfessor, String conteudoCertificado) {
        super(nomeCurso, cargaHoraria);
        this.tipoCertificado = tipoCertificado;
        this.nomeAluno = nomeAluno;
        this.nomeProfessor = nomeProfessor;
        this.conteudoCertificado = conteudoCertificado;
    }

    public String getTipoCertificado() {
        return tipoCertificado;
    }

    public void setTipoCertificado(String tipoCertificado) {
        this.tipoCertificado = tipoCertificado;
    }

    public String getNomeAluno() {
        return nomeAluno;
    }

    public void setNomeAluno(String nomeAluno) {
        this.nomeAluno = nomeAluno;
    }

    public String getNomeProfessor() {
        return nomeProfessor;
    }

    public void setNomeProfessor(String nomeProfessor) {
        this.nomeProfessor = nomeProfessor;
    }

    public String getConteudoCertificado() {
        return conteudoCertificado;
    }

    public void setConteudoCertificado(String conteudoCertificado) {
        this.conteudoCertificado = conteudoCertificado;
    }
}
