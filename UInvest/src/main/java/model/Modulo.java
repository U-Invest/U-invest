package model;

public class Modulo {
    private String resumo;
    private String id_modulo;
    private String nome;

    public Modulo() {}

    public Modulo(String resumo, String id_modulo, String nome) {
        this.resumo = resumo;
        this.id_modulo = id_modulo;
        this.nome = nome;
    }

    public String getResumo() {
        return resumo;
    }

    public void setResumo(String resumo) {
        this.resumo = resumo;
    }

    public String getId_modulo() {
        return id_modulo;
    }

    public void setId_modulo(String id_modulo) {
        this.id_modulo = id_modulo;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    @Override
    public String toString() {
        return "Modulo{" +
                "resumo='" + resumo + '\'' +
                ", id_modulo='" + id_modulo + '\'' +
                ", nome='" + nome + '\'' +
                '}';
    }
}
