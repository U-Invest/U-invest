package br.com.uInvest.beans;

public class Certificado extends Cursos {

    private String dataConclusao;
    private String descricaoCertificado;
    private String referencias;

    public Certificado() {}

    public Certificado(String nomeProfessor, String nomeUsuario, int dataCurso, String nomeCurso, int cargaHoraria,
            String descricaoCurso, String dataConclusao, String descricaoCertificado, String referencias) {
        super(nomeProfessor, nomeUsuario, dataCurso, nomeCurso, cargaHoraria, descricaoCurso);
        this.dataConclusao = dataConclusao;
        this.descricaoCertificado = descricaoCertificado;
        this.referencias = referencias;
    }

    public String getDataConclusao() {
        return dataConclusao;
    }

    public void setDataConclusao(String dataConclusao) {
        this.dataConclusao = dataConclusao;
    }

    public String getDescricaoCertificado() {
        return descricaoCertificado;
    }

    public void setDescricaoCertificado(String descricaoCertificado) {
        this.descricaoCertificado = descricaoCertificado;
    }

    public String getReferencias() {
        return referencias;
    }

    public void setReferencias(String referencias) {
        this.referencias = referencias;
    }
}
