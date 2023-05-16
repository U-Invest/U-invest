package br.com.uinvest.apiresource;

import javax.ws.rs.*;
import javax.ws.rs.core.*;

import br.com.uinvest.bo.UsuarioBO;
import br.com.uinvest.model.Usuario;

@Path("/usuarios")
public class UserResource {

    private UsuarioBO usuarioBO = new UsuarioBO();

    @GET
    @Produces(MediaType.APPLICATION_JSON_PATCH_JSON)
    public String buscarUsuarios() {
        return usuarioBO.exibirDadosUsuarioBo();
    }

//    @POST
//    @Consumes(MediaType.APPLICATION_JSON)
//    public Response cadastrar(Usuario usuario, @Context UriInfo uriInfo) {
//        usuarioBO.cadastrarUsuarioBo(usuario);
//        UriBuilder builder = uriInfo.getAbsolutePathBuilder();
//        builder.path(usuario.getCpf());
//        return Response.created(builder.build()).build();
//    }
}
