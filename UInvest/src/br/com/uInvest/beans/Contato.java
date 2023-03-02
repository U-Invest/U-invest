package br.com.uInvest.beans;

import javax.swing.*;

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
        setAssunto(JOptionPane.showInputDialog("Sobre qual assunto é sua dúvida?"));
        setMensagem(JOptionPane.showInputDialog("Digite sua dúvida/mensagem"));
        JOptionPane.showMessageDialog(null, "Obrigado por entrar em contato, respondemos em alguns instantes");
    }
}
