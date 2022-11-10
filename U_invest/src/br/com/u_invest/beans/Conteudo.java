package br.com.u_invest.beans;

public class Conteudo {

    private String noticias;
    private String descricao;

    public Conteudo(){}

    public Conteudo(String noticias, String descricao) {
        this.noticias = noticias;
        this.descricao = descricao;
    }

    public String getNoticias() {
        return noticias;
    }

    public void setNoticias(String noticias) {
        this.noticias = noticias;
    }

    public String getDescricao() {
        return descricao;
    }

    public void setDescricao(String descricao) {
        this.descricao = descricao;
    }
}
