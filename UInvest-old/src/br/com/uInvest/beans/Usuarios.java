package br.com.uInvest.beans;

import java.util.List;

public class Usuarios {
    private List<Usuario> usuario;

    public Usuarios(List<Usuario> usuario) {
        this.usuario = usuario;
    }

    public  Usuarios(){}

    public List<Usuario> getUsuario() {
        return usuario;
    }

    public void setUsuario(List<Usuario> usuario) {
        this.usuario = usuario;
    }
}
