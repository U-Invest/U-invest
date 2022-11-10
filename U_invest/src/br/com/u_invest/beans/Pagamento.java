package br.com.u_invest.beans;

public class Pagamento extends Assinatura {
    private String formaPagamento;
    public Pagamento(){}

    public Pagamento(String plano, String formaPagamento) {
        super(plano);
        this.formaPagamento = formaPagamento;
    }

    public String getFormaPagamento() {
        return formaPagamento;
    }

    public void setFormaPagamento(String formaPagamento) {
        this.formaPagamento = formaPagamento;
    }
}