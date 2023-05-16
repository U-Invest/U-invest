package br.com.uinvest.apiresource;

import java.sql.Connection;

import javax.ws.rs.*;
import javax.ws.rs.core.*;

import br.com.uinvest.bo.UsuarioBO;
import br.com.uinvest.model.Usuario;
import com.google.gson.Gson;

import br.com.uinvest.connection.Conexao;
import br.com.uinvest.dao.UsuarioDAO;


@Path("/usuarios")
public class UserResource {

    private UsuarioBO usuarioBO = new UsuarioBO();

    @GET
    @Produces(MediaType.APPLICATION_JSON_PATCH_JSON)
    public String buscarUsuarios() {
        return usuarioBO.exibirDadosUsuarioBo();
    }

    @POST
    @Consumes(MediaType.APPLICATION_JSON)
    public Response cadastrar(Usuario usuario, @Context UriInfo uriInfo) {
        usuarioBO.cadastrarUsuarioBo(usuario);
        UriBuilder builder = uriInfo.getAbsolutePathBuilder();
        builder.path(usuario.getCpf());
        return Response.created(builder.build()).build();
    }
}
