package br.com.uInvest.beans;

public class Contato {

    private String assunto;
    private String mensagem;

    public Contato() {}

    public Contato(String assunto, String mensagem) {
        this.assunto = assunto;
        this.mensagem = mensagem;
    }

    public String getAssunto() {
        return assunto;
    }

    public void setAssunto(String assunto) {
        this.assunto = assunto;
    }

    public String getMensagem() {
        return mensagem;
    }

    public void setMensagem(String mensagem) {
        this.mensagem = mensagem;
    }

    public void enviarMensagem() {
        System.out.println("Método para enviar a mensagem do usuario.");
    }
}
