package service;

import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import model.Usuario;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.JSONValue;

public class CadastroUsuarios {
    private List<Usuario> usuarios;
    private String arquivoUsuarios;

    public CadastroUsuarios(String arquivoUsuarios) {
        this.arquivoUsuarios = arquivoUsuarios;
        usuarios = new ArrayList<>();
    }

    public void cadastrarUsuario(Usuario usuario) {
        usuarios.add(usuario);
    }

    public void salvarUsuarios() {
        JSONArray listaUsuarios = new JSONArray();

        for (Usuario usuario : usuarios) {
            JSONObject jsonUsuario = new JSONObject();
            jsonUsuario.put("nome", usuario.getNome());
            jsonUsuario.put("login", usuario.getLogin());
            jsonUsuario.put("senha", usuario.getSenha());
            listaUsuarios.add(jsonUsuario);
        }

        try (FileWriter arquivo = new FileWriter(arquivoUsuarios)) {
            arquivo.write(listaUsuarios.toJSONString());
        } catch (IOException e) {
            System.out.println("Erro ao salvar os usuários.");
            e.printStackTrace();
        }
    }

    public void carregarUsuarios() {
        usuarios.clear();

        try {
            JSONArray listaUsuarios = (JSONArray) JSONValue.parseWithException(new FileReader(arquivoUsuarios));

            for (Object obj : listaUsuarios) {
                JSONObject jsonUsuario = (JSONObject) obj;
                String nome = (String) jsonUsuario.get("nome");
                String login = (String) jsonUsuario.get("login");
                String senha = (String) jsonUsuario.get("senha");
                Usuario usuario = new Usuario(nome, login, senha);
                usuarios.add(usuario);
            }
        } catch (Exception e) {
            System.out.println("Erro ao carregar os usuários.");
            e.printStackTrace();
        }
    }

    public void imprimirUsuarios() {
        for (Usuario usuario : usuarios) {
            System.out.println(usuario);
        }
    }
}
