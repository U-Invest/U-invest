package br.com.uinvest.dao;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import br.com.uinvest.model.Usuario;

public class UsuarioDAO {
    private Connection con;

    public final Connection getCon() {
        return con;
    }

    public final void setCon(Connection con) {
        this.con = con;
    }

    public UsuarioDAO(Connection con) {
        setCon(con);
    }

    public String inserir(Usuario usuario) {
        String sql = "insert into usuario(nome, email, senha, nickName, celular, cpf, nascimento, perfil_investidor, saldo) values (?,?,?,?,?,?,?,?,?)";
        try {
            PreparedStatement ps = getCon().prepareStatement(sql);
            ps.setString(1, usuario.getNome());
            ps.setString(2, usuario.getEmail());
            ps.setString(3, usuario.getSenha());
            ps.setString(4, usuario.getNickName());
            ps.setString(5, usuario.getCelular());
            ps.setString(6, usuario.getCpf());
            ps.setString(7, usuario.getNascimento());
            ps.setString(8, usuario.getPerfil_investidor());
            ps.setInt(9, usuario.getSaldo());
            if (ps.executeUpdate() > 0) {
                return "Inserido com sucesso.";
            } else {
                return "Erro ao inserir.";
            }
        } catch (SQLException e) {
            return e.getMessage();
        }
    }

    public Usuario buscarPorUserOuEmail(String nickNameOuEmail) {
        String sql = "SELECT * FROM usuario WHERE nickName = ? OR email = ?";
        try {
            PreparedStatement stmt = con.prepareStatement(sql);
            stmt.setString(1, nickNameOuEmail);
            stmt.setString(2, nickNameOuEmail);
            ResultSet rs = stmt.executeQuery();
            if (rs.next()) {
                Usuario usuario = new Usuario();
                usuario.setNome(rs.getString("nome"));
                usuario.setEmail(rs.getString("email"));
                usuario.setSenha(rs.getString("senha"));
                usuario.setNickName(rs.getString("nickName"));
                usuario.setCelular(rs.getString("celular"));
                usuario.setCpf(rs.getString("cpf"));
                usuario.setNascimento(rs.getString("nascimento"));
                usuario.setPerfil_investidor(rs.getString("perfil_investidor"));
                usuario.setSaldo(rs.getInt("saldo"));
                return usuario;
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return null;
    }

    public String buscarSenha(String senha) {
        String sql = "SELECT * FROM usuario WHERE senha = ?";
        try {
            PreparedStatement stmt = con.prepareStatement(sql);
            stmt.setString(1, senha);
            ResultSet rs = stmt.executeQuery();
            if (rs.next()) {
                return senha;
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return null;
    }
}