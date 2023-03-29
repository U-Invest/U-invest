package br.com.uinvest.model;

public class Login extends Usuario{

    private String id_sessao;
    private int hrs_plataforma;
    private String ultima_sessao; //DDmmYYYYhh
    private String hr_sessao_atual; //dd HH:mm:ss

    public Login() {}

    public Login(String nome, String email, String senha, String nickName, String celular, String cpf, String nascimento, String perfil_investidor, int saldo, String id_sessao, int hrs_plataforma, String ultima_sessao, String hr_sessao_atual) {
        super(nome, email, senha, nickName, celular, cpf, nascimento, perfil_investidor, saldo);
        this.id_sessao = id_sessao;
        this.hrs_plataforma = hrs_plataforma;
        this.ultima_sessao = ultima_sessao;
        this.hr_sessao_atual = hr_sessao_atual;
    }

    public String getId_sessao() {
        return id_sessao;
    }

    public void setId_sessao(String id_sessao) {
        this.id_sessao = id_sessao;
    }

    public int getHrs_plataforma() {
        return hrs_plataforma;
    }

    public void setHrs_plataforma(int hrs_plataforma) {
        this.hrs_plataforma = hrs_plataforma;
    }

    public String getUltima_sessao() {
        return ultima_sessao;
    }

    public void setUltima_sessao(String ultima_sessao) {
        this.ultima_sessao = ultima_sessao;
    }

    public String getHr_sessao_atual() {
        return hr_sessao_atual;
    }

    public void setHr_sessao_atual(String hr_sessao_atual) {
        this.hr_sessao_atual = hr_sessao_atual;
    }

    @Override
    public String toString() {
        return "Login{" +
                "id_sessao='" + id_sessao + '\'' +
                ", hrs_plataforma='" + hrs_plataforma + '\'' +
                ", ultima_sessao='" + ultima_sessao + '\'' +
                ", hr_sessao_atual='" + hr_sessao_atual + '\'' +
                '}';
    }
}
