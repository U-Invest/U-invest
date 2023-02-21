package service;

import org.json.simple.JSONObject;

import java.io.FileWriter;
import java.io.IOException;

public class JSONWriteService {
    @SuppressWarnings("unchecked")//Ver o que essa annotation faz!
    public static void userJSONWrite() {
        //Cria objeto JSON
        JSONObject jsonObject = new JSONObject();

        FileWriter writeFile = null;

        //Armazena dados em um Objeto JSON
        jsonObject.put("nome", "Lucas");
        jsonObject.put("sobrenome", "Pierro");
        jsonObject.put("pais", "Brasil");
        jsonObject.put("estado", "SP");

        try {
            writeFile = new FileWriter("src/br.com.uInvest/main/resources/users.json");

            //Escreve no arquivo o conteudo do Objeto JSON
            writeFile.write(jsonObject.toJSONString());
            writeFile.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
        //Imprimindo o Objeto JSON para leitura
        System.out.println(jsonObject);
    }
}
