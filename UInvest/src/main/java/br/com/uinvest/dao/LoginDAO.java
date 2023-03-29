package br.com.uinvest.dao;

import br.com.uinvest.model.Login;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class LoginDAO {

    private Connection con;

    public final Connection getCon() {
        return con;
    }

    public final void setCon(Connection con) {
        this.con = con;
    }

    public LoginDAO(Connection con) {
        setCon(con);
    }

    public String inserir(Login login) {
        String sql = "insert into login(id_sessao, hrs_plataforma, ultima_sessao, hr_sessao_atual) values (?,?,?,?)";
        try {
            PreparedStatement ps = getCon().prepareStatement(sql);
            ps.setString(1, login.getId_sessao());
            ps.setInt(2, login.getHrs_plataforma());
            ps.setString(3, login.getUltima_sessao());
            ps.setString(4, login.getHr_sessao_atual());
            if (ps.executeUpdate() > 0) {
                return "Inserido com sucesso.";
            } else {
                return "Erro ao inserir.";
            }
        } catch (SQLException e) {
            return e.getMessage();
        }
    }

}
