package br.com.uinvest.model;

public class Modulo extends Aula{
    private String resumo;

    public Modulo() {
    }

    public Modulo(String tipo_conteudo, String duracao, String nome_aula, String id, String conteudo, int avaliacao, String resumo) {
        super(tipo_conteudo, duracao, nome_aula, id, conteudo, avaliacao);
        this.resumo = resumo;
    }

    public String getResumo() {
        return resumo;
    }

    public void setResumo(String resumo) {
        this.resumo = resumo;
    }

    @Override
    public String toString() {
        return "Modulo{" +
                "resumo='" + resumo + '\'' +
                '}';
    }
}
