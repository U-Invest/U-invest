package br.com.uinvest.userResource;

import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.core.MediaType;

@Path("/usuario")
public class UserResource {

    @GET
    @Produces(MediaType.TEXT_PLAIN)
    public String buscar() {
        return "Ola Mundo!";
    }
}
