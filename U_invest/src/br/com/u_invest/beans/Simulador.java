package br.com.u_invest.beans;

public class Simulador {

    // O que o usuario deverá responder.
    private double valorInvestido;
    private String tempoInvestido;
    private double investimentoMensal;
    private String experienciaUsuario;

    // O que iremos disponibilizar para o usuarios.
    private String empresasDisponiveis;  
    private double valorAcao;
    private double taxaInvestimento;
    
    // Resultado da simulação do usuario 
    private double resultadoMinimo;
    private double resultadoEsperado;
    private double resultadoMaximo;
    
    public Simulador() {}

    public Simulador(double valorInvestido, String tempoInvestido, double investimentoMensal, String experienciaUsuario,
            String empresasDisponiveis, double valorAcao, double taxaInvestimento, double resultadoMinimo,
            double resultadoEsperado, double resultadoMaximo) {
        this.valorInvestido = valorInvestido;
        this.tempoInvestido = tempoInvestido;
        this.investimentoMensal = investimentoMensal;
        this.experienciaUsuario = experienciaUsuario;
        this.empresasDisponiveis = empresasDisponiveis;
        this.valorAcao = valorAcao;
        this.taxaInvestimento = taxaInvestimento;
        this.resultadoMinimo = resultadoMinimo;
        this.resultadoEsperado = resultadoEsperado;
        this.resultadoMaximo = resultadoMaximo;
    }

    public double getValorInvestido() {
        return valorInvestido;
    }
    public void setValorInvestido(double valorInvestido) {
        this.valorInvestido = valorInvestido;
    }
    public String getTempoInvestido() {
        return tempoInvestido;
    }
    public void setTempoInvestido(String tempoInvestido) {
        this.tempoInvestido = tempoInvestido;
    }
    public double getInvestimentoMensal() {
        return investimentoMensal;
    }
    public void setInvestimentoMensal(double investimentoMensal) {
        this.investimentoMensal = investimentoMensal;
    }
    public String getExperienciaUsuario() {
        return experienciaUsuario;
    }
    public void setExperienciaUsuario(String experienciaUsuario) {
        this.experienciaUsuario = experienciaUsuario;
    }
    public String getEmpresasDisponiveis() {
        return empresasDisponiveis;
    }
    public void setEmpresasDisponiveis(String empresasDisponiveis) {
        this.empresasDisponiveis = empresasDisponiveis;
    }
    public double getValorAcao() {
        return valorAcao;
    }
    public void setValorAcao(double valorAcao) {
        this.valorAcao = valorAcao;
    }
    public double getTaxaInvestimento() {
        return taxaInvestimento;
    }
    public void setTaxaInvestimento(double taxaInvestimento) {
        this.taxaInvestimento = taxaInvestimento;
    }
    public double getResultadoMinimo() {
        return resultadoMinimo;
    }
    public void setResultadoMinimo(double resultadoMinimo) {
        this.resultadoMinimo = resultadoMinimo;
    }
    public double getResultadoEsperado() {
        return resultadoEsperado;
    }
    public void setResultadoEsperado(double resultadoEsperado) {
        this.resultadoEsperado = resultadoEsperado;
    }
    public double getResultadoMaximo() {
        return resultadoMaximo;
    }
    public void setResultadoMaximo(double resultadoMaximo) {
        this.resultadoMaximo = resultadoMaximo;
    }
    
    /*
    METODOS
    */ 
}
