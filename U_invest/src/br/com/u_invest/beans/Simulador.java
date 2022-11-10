package br.com.u_invest.beans;

public class Simulador {
    private int valorInvestimento;
    private int taxaJuros;
    private int total;

    public Simulador() {}

    public Simulador(int valorInvestimento, int taxaJuros, int total) {
        this.valorInvestimento = valorInvestimento;
        this.taxaJuros = taxaJuros;
        this.total = total;
    }

    public int getValorInvestimento() {
        return valorInvestimento;
    }

    public void setValorInvestimento(int valorInvestimento) {
        this.valorInvestimento = valorInvestimento;
    }

    public int getTaxaJuros() {
        return taxaJuros;
    }

    public void setTaxaJuros(int taxaJuros) {
        this.taxaJuros = taxaJuros;
    }

    public int getTotal() {
        return total;
    }

    public void setTotal(int total) {
        this.total = total;
    }
}
