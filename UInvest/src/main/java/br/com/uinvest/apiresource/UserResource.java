package br.com.uinvest.apiresource;

import javax.ws.rs.*;
import javax.ws.rs.core.*;

import br.com.uinvest.bo.UsuarioBO;
import br.com.uinvest.model.Usuario;

@Path("/usuario")
public class UserResource {

    private UsuarioBO usuarioBO = new UsuarioBO();

    @GET
    @Produces(MediaType.APPLICATION_JSON_PATCH_JSON)
    public String buscarUsuarios() {
        return usuarioBO.exibirDadosUsuarioBo();
    }

    @POST
    @Consumes(MediaType.APPLICATION_JSON)
    public Response cadastraUsuario(String json, @Context UriInfo uriInfo) {
        System.out.println(json);
        Usuario cadastrando = usuarioBO.cadastrarUsuarioBo(json);
        UriBuilder builder = uriInfo.getAbsolutePathBuilder();
        builder.path((cadastrando.getNickName()));
        return Response.created(builder.build()).build();
    }
}
