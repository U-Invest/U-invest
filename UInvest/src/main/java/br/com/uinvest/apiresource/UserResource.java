package br.com.uinvest.apiresource;

import java.sql.Connection;

import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.core.MediaType;

import com.google.gson.Gson;

import br.com.uinvest.connection.Conexao;
import br.com.uinvest.dao.UsuarioDAO;


@Path("/usuarios")
public class UserResource {

    @GET
    @Produces(MediaType.APPLICATION_JSON_PATCH_JSON)
    public String buscarUsuarios() {
        Connection con = Conexao.abrirConexao();
        UsuarioDAO usuariodao = new UsuarioDAO(con);
        Gson gson = new Gson();
        String json = gson.toJson(usuariodao.exibirDadosUsuario());
        return json;
    }
}
