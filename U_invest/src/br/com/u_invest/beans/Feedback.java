package br.com.u_invest.beans;

public class Feedback extends Cursos {
    private int data;
    private String avaliacao;
    private String nomeAvaliador;
    public Feedback() {}

    public Feedback(String receberNomeCurso, int receberCargaHoraria, int data, String avaliacao, String nomeAvaliador) {
        super(receberNomeCurso, receberCargaHoraria);
        this.data = data;
        this.avaliacao = avaliacao;
        this.nomeAvaliador = nomeAvaliador;
    }

    public int getData() {
        return data;
    }

    public void setData(int data) {
        this.data = data;
    }

    public String getAvaliacao() {
        return avaliacao;
    }

    public void setAvaliacao(String avaliacao) {
        this.avaliacao = avaliacao;
    }

    public String getNomeAvaliador() {
        return nomeAvaliador;
    }

    public void setNomeAvaliador(String nomeAvaliador) {
        this.nomeAvaliador = nomeAvaliador;
    }
}
