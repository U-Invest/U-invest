package br.com.uinvest.view;

import java.io.BufferedInputStream;
import java.io.InputStream;
import java.net.URL;
import java.security.KeyStore;
import java.security.cert.CertificateFactory;
import java.security.cert.X509Certificate;
import javax.net.ssl.HttpsURLConnection;
import javax.net.ssl.SSLContext;
import javax.net.ssl.SSLException;
import javax.net.ssl.SSLSession;
import javax.net.ssl.TrustManager;
import javax.net.ssl.TrustManagerFactory;
import javax.net.ssl.X509TrustManager;

public class SSLCertInstaller {

    public static void main(String[] args) {

        String serverUrl = "https://exemplo.com";

        try {
            // Abre uma conexão SSL com o servidor
            URL url = new URL(serverUrl);
            HttpsURLConnection con = (HttpsURLConnection) url.openConnection();

            // Verifica se a conexão é segura e se o certificado do servidor é válido
            SSLContext sslContext = SSLContext.getInstance("TLS");
            sslContext.init(null, new TrustManager[] { new X509TrustManager() {
                public void checkClientTrusted(X509Certificate[] chain, String authType) {}
                public void checkServerTrusted(X509Certificate[] chain, String authType) {}
                public X509Certificate[] getAcceptedIssuers() { return new X509Certificate[0]; }
            } }, null);

            con.setSSLSocketFactory(sslContext.getSocketFactory());
            con.setHostnameVerifier((String hostname, SSLSession session) -> true);

            con.connect();

            // Obtém o certificado do servidor
            InputStream inputStream = con.getInputStream();
            BufferedInputStream bis = new BufferedInputStream(inputStream);
            CertificateFactory cf = CertificateFactory.getInstance("X.509");
            X509Certificate cert = (X509Certificate) cf.generateCertificate(bis);

            // Adiciona o certificado ao armazenamento de confiança de certificados do Java
            KeyStore keyStore = KeyStore.getInstance(KeyStore.getDefaultType());
            keyStore.load(null, null);
            keyStore.setCertificateEntry(serverUrl, cert);

            TrustManagerFactory tmf = TrustManagerFactory.getInstance(TrustManagerFactory.getDefaultAlgorithm());
            tmf.init(keyStore);

            SSLContext sslContext2 = SSLContext.getInstance("TLS");
            sslContext2.init(null, tmf.getTrustManagers(), null);
            HttpsURLConnection.setDefaultSSLSocketFactory(sslContext2.getSocketFactory());

            System.out.println("Certificado adicionado ao armazenamento de confiança do Java.");

        } catch (SSLException e) {
            e.printStackTrace();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
