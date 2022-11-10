package br.com.u_invest.beans;

public class Aulas extends Cursos {
    private String materia;
    private int tempo;
    public Aulas(){}

    public Aulas(String nomeCurso, int cargaHoraria, String materia, int tempo) {
        super(nomeCurso, cargaHoraria);
        this.materia = materia;
        this.tempo = tempo;
    }

    public String getMateria() {
        return materia;
    }

    public void setMateria(String materia) {
        this.materia = materia;
    }

    public int getTempo() {
        return tempo;
    }

    public void setTempo(int tempo) {
        this.tempo = tempo;
    }
}
