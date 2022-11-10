package br.com.u_invest.beans;

public class Assinatura {
    private String plano;
    public Assinatura(){}

    public Assinatura(String plano) {
        this.plano = plano;
    }

    public String getPlano() {
        return plano;
    }

    public void setPlano(String plano) {
        this.plano = plano;
    }
}
