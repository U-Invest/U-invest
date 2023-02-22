package test;

import model.Usuario;
import service.CadastroUsuarios;

public class Test{
    public static void main(String[] args) {
        CadastroUsuarios cadastro = new CadastroUsuarios("src/main/resources/usuarios.json");

        cadastro.cadastrarUsuario(new Usuario("João", "joao123", "senha123"));
        cadastro.cadastrarUsuario(new Usuario("Maria", "maria456", "senha456"));
        cadastro.cadastrarUsuario(new Usuario("Pedro", "pedro789", "senha789"));

        cadastro.salvarUsuarios();

        cadastro.carregarUsuarios();
        cadastro.imprimirUsuarios();
    }
}
