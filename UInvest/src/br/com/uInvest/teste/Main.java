package br.com.uInvest.teste;

import br.com.uInvest.beans.*;

import javax.swing.*;
import java.util.Random;

public class Main {
    public static void main(String[] args) {

// Administrador
        String recebeAdmId = JOptionPane.showInputDialog("Digite o ID de administrador");

// Aulas
        String recebeNomeAula = JOptionPane.showInputDialog("Digite o nome da aula");
        int recebeDuracao = Integer.parseInt(JOptionPane.showInputDialog("Digite sua duração"));
        String recebeDescricaoAula = JOptionPane.showInputDialog("Digite a descrição da aula");

// Certificado
        String recebeDataConclusao = JOptionPane.showInputDialog("Digite a data de conclusão");
        String recebeDescricaoCertificado = JOptionPane.showInputDialog("Digite a descrição do certificado");
        String recebeReferencias = JOptionPane.showInputDialog("Digite as referências");

// Contato
        String recebeAssunto = JOptionPane.showInputDialog("Digite o assunto");
        String recebeMensagem = JOptionPane.showInputDialog("Digite sua mensagem");

// Conteudo
        String recebeCursos = JOptionPane.showInputDialog("Digite os cursos");
        String recebeNoticias = JOptionPane.showInputDialog("Digite as Noticias");

// Criptografia
        String recebeSenha = JOptionPane.showInputDialog("Digite sua senha");
        String recebeSenhaEncriptada = "*SKJH!$GASKJH#TnHDSGAHDA";

// Cursos
        String recebeNomeProfessor = JOptionPane.showInputDialog("Digite o nome do professor");
        String recebeNomeUsuario = JOptionPane.showInputDialog("Digite o nome do usuario");
        int recebeDataCurso = Integer.parseInt(JOptionPane.showInputDialog("Digite a data do curso"));
        String recebeNomeCurso = JOptionPane.showInputDialog("Digite o nome do curso");
        int recebeCargaHoraria = Integer.parseInt(JOptionPane.showInputDialog("Digite sua carga horária"));
        String recebeDescricaoCurso = JOptionPane.showInputDialog("Digite a descrição do curso");

// Feedback
        String recebeAvaliacao = JOptionPane.showInputDialog("Digite sua avaliação");
        String recebeComentario = JOptionPane.showInputDialog("Digite seu comentário");


// Instituiçao
        String recebeInstituicaoId = JOptionPane.showInputDialog("Digite o Id da instituição");
        int recebeCnpj = Integer.parseInt(JOptionPane.showInputDialog("Digite seu cnpj"));

// Simulador
        double recebeValorInvestido = Double.parseDouble(JOptionPane.showInputDialog("Digite o valor investido"));
        String recebeTempoInvestido = JOptionPane.showInputDialog("Digite o tempo investido");
        double recebeInvestimentoMensal = Double.parseDouble(JOptionPane.showInputDialog("Digite o investimento mensal"));
        String recebeExperienciaUsuario = JOptionPane.showInputDialog("Digite a experiência do usuário");
        String recebeEmpresasDisponiveis = JOptionPane.showInputDialog("Digite as empresas disponíveis");
        double recebeValorAcao = Double.parseDouble(JOptionPane.showInputDialog("Digite o valor da ação"));
        double recebeTaxaInvestimento = Double.parseDouble(JOptionPane.showInputDialog("Digite a taxa de investimento"));
        double recebeResultadoMinimo = Double.parseDouble(JOptionPane.showInputDialog("Digite o resultado mínimo"));
        double recebeResultadoEsperado = Double.parseDouble(JOptionPane.showInputDialog("Digite o resultado esperado"));
        double recebeResultadoMaximo = Double.parseDouble(JOptionPane.showInputDialog("Digite o resultado máximo"));

// Usuario
        String recebeNome = JOptionPane.showInputDialog("Digite o seu nome");
        String recebeEmail = JOptionPane.showInputDialog("Digite o seu E-mail");
        String recebeTelefone = JOptionPane.showInputDialog("Digite o seu telefone");
        String recebeGenero = JOptionPane.showInputDialog("Digite o seu gênero");
        String recebeDataNascimento = JOptionPane.showInputDialog("Digite sua data de nascimento");
        int recebeCep = Integer.parseInt(JOptionPane.showInputDialog("Digite o seu CEP"));
        String recebeLogradouro = JOptionPane.showInputDialog("Digite o seu logradouro");
        String recebeBairro = JOptionPane.showInputDialog("Digite o seu bairro");
        String recebeCidade = JOptionPane.showInputDialog("Digite a sua cidade");
        String recebeEstado = JOptionPane.showInputDialog("Digite o seu estado");
        String recebeCpf = JOptionPane.showInputDialog("Digite o seu cpf");

//      Instâncias
        Administrador administrador = new Administrador(recebeNome, recebeEmail, recebeTelefone, recebeSenha, recebeGenero, recebeDataNascimento, recebeCep, recebeLogradouro, recebeBairro, recebeCidade, recebeEstado, recebeCpf, recebeAdmId);
        Aulas aulas = new Aulas(recebeNomeProfessor, recebeNomeUsuario,recebeDataCurso,recebeNomeCurso,recebeCargaHoraria,recebeDescricaoCurso,recebeNomeAula, recebeDuracao, recebeDescricaoAula);
        Certificado certificado = new Certificado(recebeNomeProfessor, recebeNomeUsuario,recebeDataCurso,recebeNomeCurso,recebeCargaHoraria,recebeDescricaoCurso, recebeDataConclusao,recebeDescricaoCertificado,recebeReferencias);
        Contato contato = new Contato(recebeAssunto, recebeMensagem);
        Conteudo conteudo = new Conteudo(recebeCursos, recebeNoticias);
        Criptografia criptografia = new Criptografia(recebeSenha, recebeSenhaEncriptada);
        Cursos cursos = new Cursos(recebeNomeProfessor,recebeNomeUsuario,recebeDataCurso,recebeNomeCurso,recebeCargaHoraria,recebeDescricaoCurso);
        Feedback feedback = new Feedback(recebeNomeProfessor,recebeNomeUsuario,recebeDataCurso,recebeNomeCurso,recebeCargaHoraria,recebeDescricaoCurso, recebeAvaliacao,recebeComentario);
        Instituicao instituicao = new Instituicao(recebeNome, recebeEmail, recebeTelefone, recebeSenha, recebeGenero, recebeDataNascimento, recebeCep, recebeLogradouro, recebeBairro, recebeCidade, recebeEstado, recebeCpf, recebeInstituicaoId,recebeCnpj);
        Simulador simulador = new Simulador(recebeValorInvestido,recebeTempoInvestido,recebeInvestimentoMensal,recebeExperienciaUsuario,recebeEmpresasDisponiveis,recebeValorAcao,recebeTaxaInvestimento,recebeResultadoMinimo,recebeResultadoEsperado,recebeResultadoMaximo);
        Usuario usuario = new Usuario(recebeNome, recebeEmail, recebeTelefone, recebeSenha, recebeGenero, recebeDataNascimento, recebeCep, recebeLogradouro, recebeBairro, recebeCidade, recebeEstado, recebeCpf);

        System.out.println(administrador.getAdmId());
        System.out.println(aulas.getNomeAula() + "\n" + aulas.getDuracao() + "\n" + aulas.getDescricaoAula());
        System.out.println(certificado.getDataConclusao() + "\n" + certificado.getDescricaoCertificado() + "\n" + certificado.getReferencias());
        System.out.println(contato.getAssunto() + "\n" + contato.getMensagem());
        System.out.println(conteudo.getCursos() + "\n" + conteudo.getNoticias());
        System.out.println(criptografia.getSenha() + "\n" + criptografia.getSenhaEncriptada());
        System.out.println(cursos.getNomeProfessor() + "\n" + cursos.getNomeUsuario() + "\n" + cursos.getDataCurso() + "\n" + cursos.getNomeCurso() + "\n" + cursos.getCargaHoraria() + "\n" + cursos.getDescricaoCurso());
        System.out.println(feedback.getAvaliacao() + "\n" + feedback.getComentario());
        System.out.println(instituicao.getInstituicaoId() + "\n" + instituicao.getCnpj());
        System.out.println(simulador.getValorInvestido() + "\n" + simulador.getTempoInvestido() + "\n" + simulador.getInvestimentoMensal() + "\n" + simulador.getExperienciaUsuario() + "\n" + simulador.getEmpresasDisponiveis() + "\n" + simulador.getValorAcao() + "\n" + simulador.getTaxaInvestimento() + "\n" + simulador.getResultadoMinimo() + "\n" + simulador.getResultadoEsperado() + "\n" + simulador.getResultadoMaximo());
        System.out.println(usuario.getNome() + "\n" + usuario.getEmail() + "\n" + usuario.getTelefone() + "\n" + usuario.getGenero() + "\n" + usuario.getDataNascimento() + "\n" + usuario.getCep() + "\n" + usuario.getLogradouro() + "\n" + usuario.getBairro() + "\n" + usuario.getCidade() + "\n" + usuario.getEstado() + "\n" + usuario.getCpf());
    }
}