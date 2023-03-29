package br.com.uinvest.teste;

import br.com.uinvest.model.*;

public class TesteInstanciandoClasses {
    public static void main(String[] args) {
        //Aula
        Aula aula = new Aula("Vídeo","010200","Componentização em React","12345678","Criando e usando funcionaliddades",8);

        System.out.println(aula.getTipo_conteudo());
        System.out.println(aula.getDuracao());
        System.out.println(aula.getNome());
        System.out.println(aula.getId());
        System.out.println(aula.getConteudo());
        System.out.println(aula.getAvaliacao() + "\n");

        //Modulo
        Modulo modulo = new Modulo("Vídeo","010200","Componentização em React","12345678","Criando e usando funcionaliddades",8, "Aqui iremos aprofundar nossos conhecimentos em react com componentização, utilizar props e states para uma melhor performance no codigo");

        System.out.println(modulo.getTipo_conteudo());
        System.out.println(modulo.getDuracao());
        System.out.println(modulo.getNome());
        System.out.println(modulo.getId());
        System.out.println(modulo.getConteudo());
        System.out.println(modulo.getAvaliacao());
        System.out.println(modulo.getResumo() + "\n");

        //Curso
        Curso curso = new Curso(40,8,"Aprenda os fundamentos de Java","Rafael Ronqui", "Fundamentos Java", "00000001", 1000);

        System.out.println(curso.getDuracao());
        System.out.println(curso.getAvaliacao());
        System.out.println(curso.getResumo());
        System.out.println(curso.getProfessor());
        System.out.println(curso.getNome());
        System.out.println(curso.getPontuacao() + "\n");

        //Certificado
        Certificado certificado = new Certificado(40,8,"Aprenda os fundamentos de Java","Rafael Ronqui", "Fundamentos Java", "00000001", 1000, "Matheus Pierro","RafaRonqui","03042023","29032023","00000002");

        System.out.println(certificado.getDuracao());
        System.out.println(certificado.getAvaliacao());
        System.out.println(certificado.getResumo());
        System.out.println(certificado.getProfessor());
        System.out.println(certificado.getNome());
        System.out.println(certificado.getPontuacao());
        System.out.println(certificado.getNome_aluno());
        System.out.println(certificado.getAssinatura_plat());
        System.out.println(certificado.getDt_emissao());
        System.out.println(certificado.getDt_conclusao());
        System.out.println(certificado.getId_certificado() + "\n");

        //Usuario
        Usuario usuario = new Usuario("Matheus Pierro","matpierro570@gmail.com","matmat96920","matpierro","11961065956","52867130840","08092003","Conservador",0);

        System.out.println(usuario.getNome());
        System.out.println(usuario.getEmail());
        System.out.println(usuario.getSenha());
        System.out.println(usuario.getNickName());
        System.out.println(usuario.getCelular());
        System.out.println(usuario.getCpf());
        System.out.println(usuario.getNascimento());
        System.out.println(usuario.getPerfil_investidor());
        System.out.println(usuario.getSaldo() + "\n");

        //Login
        Login login = new Login("Matheus Pierro","matpierro570@gmail.com","matmat96920","matpierro","11961065956","52867130840","08092003","Conservador", 0, "00000003", 12, "2903202314", "29 00:30:46");

        System.out.println(login.getNome());
        System.out.println(login.getEmail());
        System.out.println(login.getSenha());
        System.out.println(login.getNickName());
        System.out.println(login.getCelular());
        System.out.println(login.getCpf());
        System.out.println(login.getNascimento());
        System.out.println(login.getPerfil_investidor());
        System.out.println(login.getId_sessao());
        System.out.println(login.getHrs_plataforma());
        System.out.println(login.getUltima_sessao());
        System.out.println(login.getHr_sessao_atual() + "\n");

        //Progresso do Curso
        Pg_curso pg_curso = new Pg_curso("Matheus Pierro","matpierro570@gmail.com","matmat96920","matpierro","11961065956","52867130840","08092003","Conservador",0, 86, "2803202320", 450);

        System.out.println(pg_curso.getNome());
        System.out.println(pg_curso.getEmail());
        System.out.println(pg_curso.getSenha());
        System.out.println(pg_curso.getNickName());
        System.out.println(pg_curso.getCelular());
        System.out.println(pg_curso.getCpf());
        System.out.println(pg_curso.getNascimento());
        System.out.println(pg_curso.getPerfil_investidor());
        System.out.println(pg_curso.getProgresso_user());
        System.out.println(pg_curso.getUltimo_acesso());
        System.out.println(pg_curso.getU_coins() + "\n");
    }
}
