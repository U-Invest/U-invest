package br.com.uInvest.beans;

public class Feedback extends Cursos {

    private String avaliacao;
    private String comentario;

    public Feedback() {}

    public Feedback(String nomeProfessor, String nomeUsuario, int dataCurso, String nomeCurso, int cargaHoraria,
            String descricaoCurso, String avaliacao, String comentario) {
        super(nomeProfessor, nomeUsuario, dataCurso, nomeCurso, cargaHoraria, descricaoCurso);
        this.avaliacao = avaliacao;
        this.comentario = comentario;
    }

    public String getAvaliacao() {
        return avaliacao;
    }

    public void setAvaliacao(String avaliacao) {
        this.avaliacao = avaliacao;
    }

    public String getComentario() {
        return comentario;
    }

    public void setComentario(String comentario) {
        this.comentario = comentario;
    }
}
