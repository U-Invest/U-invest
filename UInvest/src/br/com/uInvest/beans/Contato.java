package br.com.uInvest.beans;

import java.util.ArrayList;
import java.util.List;
import java.util.Properties;
import javax.mail.Address;
import javax.mail.Message;
import javax.mail.MessagingException;
import javax.mail.PasswordAuthentication;
import javax.mail.Session;
import javax.mail.Transport;
import javax.mail.internet.InternetAddress;
import javax.mail.internet.MimeMessage;
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

//        TENTATIVA DE ENVIO DE EMAIL AUTOMÁTICO PARA O USUÀRIO AO TIRAR DÚVIDAS

//        Properties props = new Properties();
//        /** Parâmetros de conexão com servidor Gmail */
//        props.put("mail.smtp.host", "smtp.gmail.com");
//        props.put("mail.smtp.socketFactory.port", "465");
//        props.put("mail.smtp.socketFactory.class",
//                "javax.net.ssl.SSLSocketFactory");
//        props.put("mail.smtp.auth", "true");
//        props.put("mail.smtp.port", "465");
//
//        Session session = Session.getDefaultInstance(props,
//                new javax.mail.Authenticator() {
//                    protected PasswordAuthentication getPasswordAuthentication()
//                    {
//                        return new PasswordAuthentication("matpierro570@gmail.com",
//                                "matheus9");
//                    }
//                });
//
//        /** Ativa Debug para sessão */
//        session.setDebug(true);
//
//        try {
//
//            Message message = new MimeMessage(session);
//            message.setFrom(new InternetAddress("matpierro570@gmail.com"));
//            //Remetente
//
//            Address[] toUser = InternetAddress //Destinatário(s)
//                    .parse(emailResposta);
//
//            message.setRecipients(Message.RecipientType.TO, toUser);
//            message.setSubject("Enviando email com JavaMail");//Assunto
//            message.setText("Enviei este email utilizando JavaMail com minha conta GMail!");
//            /**Método para enviar a mensagem criada*/
//            Transport.send(message);
//
//            System.out.println("Feito!!!");
//
//        } catch (MessagingException e) {
//            throw new RuntimeException(e);
//        }
    }
}
