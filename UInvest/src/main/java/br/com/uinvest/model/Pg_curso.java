package br.com.uinvest.model;

public class Pg_curso extends Usuario{
    private int progresso_user;
    private String ultimo_acesso; //DDmmYYYYhh
    private int u_coins;

    public Pg_curso() {}

    public Pg_curso(String nome, String email, String senha, String nickName, String celular, String cpf, String nascimento, String perfil_investidor, int saldo, int progresso_user, String ultimo_acesso, int u_coins) {
        super(nome, email, senha, nickName, celular, cpf, nascimento, perfil_investidor, saldo);
        this.progresso_user = progresso_user;
        this.ultimo_acesso = ultimo_acesso;
        this.u_coins = u_coins;
    }

    public int getProgresso_user() {
        return progresso_user;
    }

    public void setProgresso_user(int progresso_user) {
        this.progresso_user = progresso_user;
    }

    public String getUltimo_acesso() {
        return ultimo_acesso;
    }

    public void setUltimo_acesso(String ultimo_acesso) {
        this.ultimo_acesso = ultimo_acesso;
    }

    public int getU_coins() {
        return u_coins;
    }

    public void setU_coins(int u_coins) {
        this.u_coins = u_coins;
    }

    @Override
    public String toString() {
        return "Pg_curso{" +
                "progresso_user=" + progresso_user +
                ", ultimo_acesso='" + ultimo_acesso + '\'' +
                ", u_coins=" + u_coins +
                '}';
    }
}
