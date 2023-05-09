package br.com.uinvest.controller;

import br.com.uinvest.connection.Conexao;
import br.com.uinvest.dao.CursoDAO;
import br.com.uinvest.dao.UsuarioDAO;
import br.com.uinvest.model.Curso;
import br.com.uinvest.model.Usuario;
import br.com.uinvest.service.CursoService;
import br.com.uinvest.service.UsuarioService;

import javax.swing.*;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.sql.Connection;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Random;

public class CursoController {
    public void cadastrarCurso(){
        Connection con = Conexao.abrirConexao();
        Curso curso = new Curso();
        CursoDAO cursoDAO = new CursoDAO(con);
        CursoService cursoService = new CursoService();
        List<Integer> avaliacoes = Arrays.asList(5, 4, 3, 5, 2, 5, 6, 7, -1);

        String nome = JOptionPane.showInputDialog("Digite o nome do curso");
        String professor =JOptionPane.showInputDialog("Digite o nome do professor que ministra o curso");
        String resumo = JOptionPane.showInputDialog("Breve resumo sobre o curso");
        int duracao = Integer.parseInt(JOptionPane.showInputDialog("Digite o tempo de formação do curso"));
        int pontuacao = pontuacaoCurso(duracao);
        int avaliacao = avaliacaoCurso(avaliacoes);
        String id = gerarCodigoCurso();

        if (cursoService.validarDadosCurso(/**duracao, avaliacao, resumo, professor, nome, id, pontuacao*/)) {
            curso.setDuracao(duracao);
            curso.setAvaliacao(avaliacao);
            curso.setResumo(resumo);
            curso.setProfessor(professor);
            curso.setNome(nome);
            curso.setId_curso(id);
            curso.setPontuacao(pontuacao);

            System.out.println(cursoDAO.inserir(curso));
        } else {
            System.out.println("Os dados do usuário não são válidos.");
        }
        Conexao.fecharConexao(con);
    }

    public static int pontuacaoCurso(int duracaoCurso) {
        int pontuacao;
        if (duracaoCurso < 10) {
            pontuacao = (int) (duracaoCurso * 0.5);
        } else if (duracaoCurso < 20) {
            pontuacao = (int) (duracaoCurso * 0.75);
        } else if (duracaoCurso < 30) {
            pontuacao = duracaoCurso;
        } else {
            pontuacao = (int) (duracaoCurso * 1.25);
        }
        return pontuacao;
    }

    public static int avaliacaoCurso(List<Integer> avaliacoes) {
        if (avaliacoes.isEmpty()) {
            return 0;
        }

        List<Integer> avaliacoesFiltradas = new ArrayList<>();
        for (int nota : avaliacoes) {
            if (nota >= 0 && nota <= 5) {
                avaliacoesFiltradas.add(nota);
            }
        }

        if (avaliacoesFiltradas.isEmpty()) {
            return 0;
        }

        int totalAvaliacoes = 0;
        for (int nota : avaliacoesFiltradas) {
            totalAvaliacoes += nota;
        }

        int mediaAvaliacoes = totalAvaliacoes / avaliacoesFiltradas.size();

        return mediaAvaliacoes;
    }

    public static String gerarCodigoCurso() {
        Random rand = new Random();
        int codigo = rand.nextInt(100000000);
        while (Integer.toString(codigo).length() < 8) {
            codigo = Integer.parseInt("0" + Integer.toString(codigo));
        }
        return Integer.toString(codigo);
    }
}
