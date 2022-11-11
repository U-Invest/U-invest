package br.com.u_invest.beans;

public class Aulas extends Cursos {
    
    private String nomeAula;
    private int duracao;
    private String descricaoAula;

    public Aulas() {}

    public Aulas(String nomeProfessor, String nomeUsuario, int dataCurso, String nomeCurso, int cargaHoraria,
            String descricaoCurso, String nomeAula, int duracao, String descricaoAula) {
        super(nomeProfessor, nomeUsuario, dataCurso, nomeCurso, cargaHoraria, descricaoCurso);
        this.nomeAula = nomeAula;
        this.duracao = duracao;
        this.descricaoAula = descricaoAula;
    }

    public String getNomeAula() {
        return nomeAula;
    }

    public void setNomeAula(String nomeAula) {
        this.nomeAula = nomeAula;
    }

    public int getDuracao() {
        return duracao;
    }

    public void setDuracao(int duracao) {
        this.duracao = duracao;
    }

    public String getDescricaoAula() {
        return descricaoAula;
    }

    public void setDescricaoAula(String descricaoAula) {
        this.descricaoAula = descricaoAula;
    }
}
