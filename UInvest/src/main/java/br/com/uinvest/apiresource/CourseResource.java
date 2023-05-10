package br.com.uinvest.apiresource;

import br.com.uinvest.connection.Conexao;

import br.com.uinvest.dao.CursoDAO;
import com.google.gson.Gson;

import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.core.MediaType;
import java.sql.Connection;

@Path("/cursos")
public class CourseResource {

    @GET
    @Produces(MediaType.APPLICATION_JSON_PATCH_JSON)
    public String buscarCursos() {
        Connection con = Conexao.abrirConexao();
        CursoDAO cursodao = new CursoDAO(con);
        Gson gson = new Gson();
        String json = gson.toJson(cursodao.exibirDadosCursos());
        Conexao.fecharConexao(con);
        return json; 
    }
}
