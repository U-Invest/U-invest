package br.com.uinvest.apiresource;

import br.com.uinvest.bo.UsuarioBO;
import br.com.uinvest.dao.UsuarioDAO;
import br.com.uinvest.model.Usuario;

import javax.ws.rs.Consumes;
import javax.ws.rs.POST;
import javax.ws.rs.Path;
import javax.ws.rs.core.*;


@Path("/login")
public class LoginResource {
    private UsuarioBO usuarioBO = new UsuarioBO();

    @POST
    @Consumes(MediaType.APPLICATION_JSON)
    public Response logar(String json, @Context UriInfo uriInfo) {
//        String jsonTeste = "{\"nickNameOuEmail\": \"sasaOri\", \"senha\":\"matheus9\"}";
        Usuario logando = usuarioBO.loginBo(json);
        UriBuilder builder = uriInfo.getAbsolutePathBuilder();
        builder.path((logando.getNickName()));

        return Response.created(builder.build()).build();
    }
}
