package br.com.u_invest.beans;

public class Criptografia {
    private int chaveCriptografica;
    public Criptografia() {}

    public Criptografia(int chaveCriptografica) {
        this.chaveCriptografica = chaveCriptografica;
    }

    public int getChaveCriptografica() {
        return chaveCriptografica;
    }

    public void setChaveCriptografica(int chaveCriptografica) {
        this.chaveCriptografica = chaveCriptografica;
    }
}
