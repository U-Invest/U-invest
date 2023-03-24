package br.com.uinvest.model;

public class Login {

    private String id_sessao;
    private String hrs_plataforma;
    private String ultima_sessao;
    private String hr_sessao_atual;

    public Login() {}

    public Login(String id_sessao, String hrs_plataforma, String ultima_sessao, String hr_sessao_atual) {
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

    public String getHrs_plataforma() {
        return hrs_plataforma;
    }

    public void setHrs_plataforma(String hrs_plataforma) {
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
