package br.com.uinvest.service;

import com.google.gson.Gson;
import com.google.gson.JsonObject;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;


public class UsuarioService {
    public boolean validarDadosUsuario(String cpf, String email, String celular, String nome, String senha, String perfilInvestidor, String nickName, String nascimento) {
        boolean dadosValidos = true;

        // Validar o nome
        if (nome == null || nome.trim().equals("")) {
            dadosValidos = false;
        }

        // Validar o e-mail
        if (email == null || email.trim().equals("")) {
            dadosValidos = validaEmail(email);
        }

        // Validar a senha
        if (senha == null || senha.trim().equals("")) {
            dadosValidos = false;
        }

        // Validar o user
        if (nickName == null || nickName.trim().equals("")) {
            dadosValidos = false;
        }

        // Validar o celular
        if (celular == null || celular.trim().equals("")) {
            dadosValidos = false;
        }

        // Validar o CPF
        if (cpf == null || cpf.trim().equals("")) {
            dadosValidos = false;
        }

        // Validar o CPF
        if (nascimento == null || nascimento.trim().equals("")) {
            dadosValidos = false;
        }

        // Validar o perfil do investidor
        if (perfilInvestidor == null || perfilInvestidor.trim().equals("")) {
            dadosValidos = false;
        }

        return dadosValidos;
    }

    public boolean validaEmail(String email) {

        String apiKey = "92ddd0010a9620726efc46de85fb711291b86214";

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

            System.out.println(result);

            // Verifica se o e-mail é válido
            return !result.equals("deliverable");

        } catch (IOException e) {
            if (e.getMessage().contains("Server returned HTTP response code: 400")) {
                System.out.println("Erro de digitação: verifique se o endereço de e-mail foi digitado corretamente.");
            } else {
                e.printStackTrace();
            }
        }
        return true;
    }
}
