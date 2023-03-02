package service;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.URLEncoder;
import java.nio.charset.StandardCharsets;

import org.apache.http.HttpResponse;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.HttpClientBuilder;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;

public class YahooFinanceAPI {
    private static final String BASE_URL = "https://finance.yahoo.com/rss/headline?s=";

    public static void main(String[] args) {
        String symbol = "AAPL"; // símbolo da ação que queremos pesquisar
        String url = BASE_URL + URLEncoder.encode(symbol, StandardCharsets.UTF_8); // constrói a URL da API
        HttpClient client = HttpClientBuilder.create().build(); // cria o cliente HTTP
        HttpGet request = new HttpGet(url); // cria a solicitação HTTP GET

        try {
            HttpResponse response = client.execute(request); // executa a solicitação HTTP GET
            BufferedReader reader = new BufferedReader(new InputStreamReader(response.getEntity().getContent())); // lê a resposta da API
            String line;
            while ((line = reader.readLine()) != null) {
                System.out.println(line); // imprime a resposta no console
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    /*   Abaixo está um exemplo de como usar a Yahoo Finance API para listar as ações disponíveis em Java:

   Primeiro, você precisa se inscrever para obter uma chave de API da Yahoo Finance. Acesse o site Yahoo Developer Network (https://developer.yahoo.com) e siga as instruções para criar uma conta e obter uma chave de API gratuita.

   Em seguida, você pode fazer chamadas à API usando bibliotecas Java de terceiros, como o Apache HttpClient e o JsonSimple.

   O seguinte exemplo de código Java usa a biblioteca HttpClient para fazer uma chamada à API e recuperar uma lista de ações disponíveis:*/
    public void listarAcoes() throws IOException, ParseException {
        String apiKey = "YOUR_API_KEY_HERE";
        String url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/get-summary?region=US&lang=en";

        URL obj = new URL(url);
        HttpURLConnection con = (HttpURLConnection) obj.openConnection();

        con.setRequestMethod("GET");
        con.setRequestProperty("X-RapidAPI-Key", apiKey);
        con.setRequestProperty("Content-type", "application/json");

        BufferedReader in = new BufferedReader(new InputStreamReader(con.getInputStream()));
        String inputLine;
        StringBuffer response = new StringBuffer();

        while ((inputLine = in.readLine()) != null) {
            response.append(inputLine);
        }
        in.close();

        JSONParser parser = new JSONParser();
        JSONObject jsonObject = (JSONObject) parser.parse(response.toString());

        JSONArray symbolsArray = (JSONArray) jsonObject.get("marketSummaryAndSparkResponse");
        JSONObject symbolsObject = (JSONObject) symbolsArray.get(0);
        JSONArray resultArray = (JSONArray) symbolsObject.get("result");

        for (int i = 0; i < resultArray.size(); i++) {
            JSONObject symbolObject = (JSONObject) resultArray.get(i);
            String name = (String) symbolObject.get("shortName");
            String symbol = (String) symbolObject.get("symbol");
            System.out.println(name + " (" + symbol + ")");
        }
    }
}
