package br.com.uInvest.beans;

public class Cursos {

    private String nomeProfessor;
    private String nomeUsuario;
    private int dataCurso;
    private String nomeCurso;
    private int cargaHoraria;
    private String descricaoCurso;

    public Cursos() {}

    public Cursos(String nomeProfessor, String nomeUsuario, int dataCurso, String nomeCurso, int cargaHoraria,
            String descricaoCurso) {
        this.nomeProfessor = nomeProfessor;
        this.nomeUsuario = nomeUsuario;
        this.dataCurso = dataCurso;
        this.nomeCurso = nomeCurso;
        this.cargaHoraria = cargaHoraria;
        this.descricaoCurso = descricaoCurso;
    }

    public String getNomeProfessor() {
        return nomeProfessor;
    }

    public void setNomeProfessor(String nomeProfessor) {
        this.nomeProfessor = nomeProfessor;
    }

    public String getNomeUsuario() {
        return nomeUsuario;
    }

    public void setNomeUsuario(String nomeUsuario) {
        this.nomeUsuario = nomeUsuario;
    }

    public int getDataCurso() {
        return dataCurso;
    }

    public void setDataCurso(int dataCurso) {
        this.dataCurso = dataCurso;
    }

    public String getNomeCurso() {
        return nomeCurso;
    }

    public void setNomeCurso(String nomeCurso) {
        this.nomeCurso = nomeCurso;
    }

    public int getCargaHoraria() {
        return cargaHoraria;
    }

    public void setCargaHoraria(int cargaHoraria) {
        this.cargaHoraria = cargaHoraria;
    }

    public String getDescricaoCurso() {
        return descricaoCurso;
    }

    public void setDescricaoCurso(String descricaoCurso) {
        this.descricaoCurso = descricaoCurso;
    }
}
