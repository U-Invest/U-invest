package br.com.uinvest.view;

import com.google.gson.Gson;
import com.google.gson.JsonObject;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

public class HunterEmailValidator {

    public static void main(String[] args) {

        String apiKey = "92ddd0010a9620726efc46de85fb711291b86214";
        String email = "matpierro570@gmail.com";

        try {
            // Cria a URL de chamada da API do Hunter
            URL url = new URL("https://api.hunter.io/v2/email-verifier?email=" + email + "&api_key=" + apiKey);

            // Abre a conexão com a API do Hunter
            HttpURLConnection con = (HttpURLConnection) url.openConnection();

            // Define o método de requisição para GET
            con.setRequestMethod("GET");

            // Lê a resposta da API do Hunter
            BufferedReader in = new BufferedReader(new InputStreamReader(con.getInputStream()));
            String inputLine;
            StringBuffer response = new StringBuffer();
            while ((inputLine = in.readLine()) != null) {
                response.append(inputLine);
            }
            in.close();

            // Converte a resposta da API do Hunter em um objeto JSON
            Gson gson = new Gson();
            JsonObject jsonObject = gson.fromJson(response.toString(), JsonObject.class);

            // Extrai a informação de validação do e-mail do objeto JSON
            String result = jsonObject.get("data").getAsJsonObject().get("result").getAsString();

            // Verifica se o e-mail é válido
            if (result.equals("deliverable")) {
                System.out.println("O e-mail " + email + " é válido.");
            } else {
                System.out.println("O e-mail " + email + " é inválido ou não pôde ser verificado.");
            }

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

