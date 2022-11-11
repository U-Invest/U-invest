package br.com.u_invest.beans;

public class Conteudo {

    private String cursos;
    private String noticias;

    public Conteudo() {}

    public Conteudo(String cursos, String noticias) {
        this.cursos = cursos;
        this.noticias = noticias;
    }

    public String getCursos() {
        return cursos;
    }

    public void setCursos(String cursos) {
        this.cursos = cursos;
    }

    public String getNoticias() {
        return noticias;
    }

    public void setNoticias(String noticias) {
        this.noticias = noticias;
    }
}
