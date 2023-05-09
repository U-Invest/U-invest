package br.com.uinvest.dao;

import br.com.uinvest.model.Curso;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;

public class CursoDAO {

    private Connection con;
    public final Connection getCon() {
        return con;
    }
    public final void setCon(Connection con) {
        this.con = con;
    }
    public CursoDAO(Connection con) {
        setCon(con);
    }

    /**
     * Insere um novo curso no banco de dados.
     *
     * @param curso O curso a ser inserido
     * @return Uma mensagem indicando se a inserção foi bem-sucedida ou não
     */
    public String inserir(Curso curso) {
        String sql = "insert into curso(duracao, avaliacao, resumo, professor, nome, id_curso, pontuacao) values (?,?,?,?,?,?,?)";
        try {
            PreparedStatement ps = getCon().prepareStatement(sql);
            ps.setInt(1, curso.getDuracao());
            ps.setInt(2, curso.getAvaliacao());
            ps.setString(3, curso.getResumo());
            ps.setString(4, curso.getProfessor());
            ps.setString(5, curso.getNome());
            ps.setString(6, curso.getId());
            ps.setInt(7, curso.getPontuacao());
            if (ps.executeUpdate() > 0) {
                return "Inserido com sucesso.";
            } else {
                return "Erro ao inserir.";
            }
        } catch (SQLException e) {
            return e.getMessage();
        }
    }

    /**
     * Retorna uma lista de todos os cursos registrados no banco de dados.
     *
     * @return Uma lista de objetos Curso representando os cursos registrados, ou null se nenhum curso for encontrado.
     */
    public ArrayList<Curso> exibirDadosCursos() {
        String sql = "select * from curso";
        ArrayList<Curso> cursos = new ArrayList<>();
        try {
            PreparedStatement ps = getCon().prepareStatement(sql);
            ResultSet rs = ps.executeQuery();
            if (rs != null) {
                while (rs.next()) {
                    Curso curso = new Curso();
                    curso.setNome(rs.getString(5));
                    curso.setProfessor(rs.getString(4));
                    curso.setResumo(rs.getString(3));
                    curso.setPontuacao(rs.getInt(7));
                    curso.setAvaliacao(rs.getInt(2));
                    curso.setDuracao(rs.getInt(1));
                    curso.setId_curso(rs.getString(7));
                    cursos.add(curso);
                }
                return cursos;
            } else {
                return null;
            }
        } catch (SQLException e) {
            return null;
        }
    }
}
