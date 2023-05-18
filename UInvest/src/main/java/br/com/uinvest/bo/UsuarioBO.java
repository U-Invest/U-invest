package br.com.uinvest.bo;

import br.com.uinvest.connection.Conexao;
import br.com.uinvest.controller.LoginController;
import br.com.uinvest.controller.UsuarioController;
import br.com.uinvest.dao.UsuarioDAO;
import br.com.uinvest.model.Usuario;
import com.google.gson.Gson;

import java.sql.Connection;

public class UsuarioBO {
    private UsuarioDAO ud;
    private UsuarioController uc;
    private LoginController lc;

    public String exibirDadosUsuarioBo() {
        Connection con = Conexao.abrirConexao();
        ud = new UsuarioDAO(con);
        Gson gson = new Gson();
        String json = gson.toJson(ud.exibirDadosUsuario());
        Conexao.fecharConexao(con);
        return json;
    }

    public Usuario loginBo(String json) {
        Connection con = Conexao.abrirConexao();
        ud = new UsuarioDAO(con);
        lc = new LoginController();
        UsuarioDAO.JsonDataLoggedIn dadosAutenticar = ud.login(json);
        Boolean responseAuth = lc.autenticarUsuario(dadosAutenticar.getNickNameOuEmail(), dadosAutenticar.getSenha());

        if(responseAuth){
            Usuario usuario = new Usuario();
            usuario = ud.buscarPorUserOuEmail(dadosAutenticar.getNickNameOuEmail());
            System.out.println(usuario);
            Conexao.fecharConexao(con);
            return usuario;
        }
        return null;
    }

    public Usuario cadastrarUsuarioBo(String json) {
        Connection con = Conexao.abrirConexao();
        ud = new UsuarioDAO(con);
        uc = new UsuarioController();
        Usuario dadosUsuario = ud.cadastro(json);
        return uc.cadastrarUsuarioFront(dadosUsuario);
    }


}
