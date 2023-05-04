package br.com.uinvest.service;

import com.google.gson.Gson;
import com.google.gson.JsonObject;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;


public class UsuarioService {
    public boolean validarDadosUsuario(String cpf, String email, String celular, String nome, String senha, String perfilInvestidor, String nickName, String nascimento) {

        boolean dadosValidos = true;

        // Validar o nome
        if (nome == null || nome.trim().equals("")) {
            dadosValidos = validarNome(nome);
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

        // Validar o Nascimento
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

    public boolean validarNome(String nome) {

        try {
            for (int i = 0; i < nome.length(); i++) {
                char c = nome.charAt(i);
                if (!Character.isLetter(c) && !Character.isWhitespace(c)) {
                    return true;
                }
            }
        } catch (NullPointerException | IndexOutOfBoundsException e) {
            System.out.println("Erro: Nome inválido");
        }

        return false;
    }

    public static boolean validaData(String dataNascimento) {
        SimpleDateFormat sdf = new SimpleDateFormat("ddMMyyyy");
        sdf.setLenient(false);

        try {
            Date data = sdf.parse(dataNascimento);
            return true;
        } catch (ParseException e) {
            return false;
        }
    }

    public static boolean validaCpf(String cpf) {
        cpf = cpf.replaceAll("[^0-9]", ""); // Remove caracteres não numéricos

        if (cpf.length() != 11) {
            return false;
        }

        int[] digitos = new int[11];

        for (int i = 0; i < 11; i++) {
            digitos[i] = Character.getNumericValue(cpf.charAt(i));
        }

        // Verifica se todos os dígitos são iguais
        boolean todosDigitosIguais = true;

        for (int i = 1; i < 11; i++) {
            if (digitos[i] != digitos[0]) {
                todosDigitosIguais = false;
                break;
            }
        }

        if (todosDigitosIguais) {
            return false;
        }

        // Verifica o primeiro dígito verificador
        int soma = 0;

        for (int i = 0; i < 9; i++) {
            soma += digitos[i] * (10 - i);
        }

        int primeiroDigitoVerificador = 11 - (soma % 11);

        if (primeiroDigitoVerificador >= 10) {
            primeiroDigitoVerificador = 0;
        }

        if (primeiroDigitoVerificador != digitos[9]) {
            return false;
        }

        // Verifica o segundo dígito verificador
        soma = 0;

        for (int i = 0; i < 10; i++) {
            soma += digitos[i] * (11 - i);
        }

        int segundoDigitoVerificador = 11 - (soma % 11);

        if (segundoDigitoVerificador >= 10) {
            segundoDigitoVerificador = 0;
        }

        if (segundoDigitoVerificador != digitos[10]) {
            return false;
        }

        return true;
    }

    public static boolean isCelularValido(String numeroCelular) {
        // Remover caracteres não numéricos
        String numeroApenasDigitos = numeroCelular.replaceAll("[^0-9]", "");

        // Verificar o tamanho mínimo do número de celular com DDD
        if (numeroApenasDigitos.length() < 10) {
            return false;
        }

        // Extrair o DDD e o número do celular
        String ddd = numeroApenasDigitos.substring(0, 2);
        String numero = numeroApenasDigitos.substring(2);

        // Verificar se o DDD é válido (exemplo: DDDs do Brasil)
        String[] dddsValidos = { "11", "12", "13", "14", "15", "16", "17", "18", "19" }; // Adicione outros DDDs válidos conforme necessário

        boolean dddValido = false;
        for (String dddValidu : dddsValidos) {
            if (ddd.equals(dddValidu)) {
                dddValido = true;
                break;
            }
        }

        if (!dddValido) {
            return false;
        }

        // Verificar se o número do celular possui apenas dígitos (exemplo: sem caracteres especiais)
        if (!numero.matches("[0-9]+")) {
            return false;
        }

        // Verificar outras regras específicas, se necessário

        return true;
    }
}
