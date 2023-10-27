import os
import textwrap
from flask import Flask, jsonify, request
from imports import chatbot_response, selecionar_arquivo_por_id
from flask_cors import CORS

app = Flask(__name__)

CORS(app)


@app.route('/introducao', methods=['GET'])
def introducao():
    try:
        boas_vindas = "Bem-vindo ao Droid! Eu sou um chatbot sobre IPOs. Como posso ajudá-lo?"
        opcoes = [
            "1 - Tirar dúvidas sobre IPO",
            "2 - Sumarizar o prospecto",
            "3 - Abrir pagina com prospectos",
        ]
        mensagem_completa = boas_vindas + "\n" + '\n'.join(opcoes)
        return jsonify({"mensagem": mensagem_completa})
    except Exception as e:
        return jsonify({"error": f"Um erro ocorreu: {e}"})


@app.route('/escolha', methods=['GET'])
def escolha():
    try:
        valor = request.args.get('valor')

        if valor is None or not valor.isdigit() or int(valor) < 1 or int(valor) > 3:
            return jsonify({"error": "Valor inválido. Por favor, forneça um valor entre 1 e 3."})

        valor = int(valor)
        mensagens = {
            1: "Você escolheu tirar dúvidas sobre IPO. Como podemos ajudá-lo hoje?",
            2: "Você escolheu sumarizar o prospecto. Por favor, aguarde enquanto processamos...",
            3: "Você escolheu abrir a página com prospectos. O navegador será aberto com a página desejada.",
        }

        return jsonify({"mensagem": mensagens[valor]})

    except Exception as e:
        return jsonify({"error": f"Um erro ocorreu: {e}"})


@app.route('/duvida', methods=['POST'])
def ask():
    try:
        data = request.get_json()
        question = data.get('question')
        response = chatbot_response(question)
        cleaned_response = response[3:]
        wrapped_response = textwrap.wrap(cleaned_response, width=50)
        wrapped_response_str = " ".join(wrapped_response)
        return jsonify({"response": wrapped_response_str})
    except Exception as e:
        return jsonify({"error": f"Um erro ocorreu: {e}"})


@app.route('/prospectos', methods=['GET'])
def listar_prospectos():
    try:
        caminho_pasta = "prospectos"
        if os.path.exists(caminho_pasta):
            prospectos = os.listdir(caminho_pasta)
            return jsonify({"prospectos": prospectos})
        else:
            return jsonify({"error": "Diretório de prospectos não encontrado."})
    except Exception as e:
        return jsonify({"error": f"Um erro ocorreu: {e}"})


@app.route('/sumarizar', methods=['GET'])
def sumarizar():
    try:
        # Obtendo o ID do prospecto da requisição
        id_prospecto = request.args.get('id')

        # Validando o ID do prospecto
        if id_prospecto is None or not id_prospecto.isdigit():
            return jsonify({"error": "ID inválido."})

        id_prospecto = int(id_prospecto)

        # Definindo os caminhos das pastas
        caminho_pasta = "prospectos"
        caminho_pasta_txt = "indices"
        caminho_pasta_saida = "paginas"

        # Chamando a função selecionar_arquivo_por_id e obtendo o resultado
        resultado = selecionar_arquivo_por_id(
            id_prospecto, caminho_pasta, caminho_pasta_txt, caminho_pasta_saida)

        # Retornando o resultado como uma resposta JSON
        return jsonify(resultado)

    except Exception as e:
        # Caso ocorra algum erro, retornar uma mensagem de erro como uma resposta JSON
        return jsonify({"error": f"Um erro ocorreu: {e}"})


if __name__ == '__main__':
    app.run(debug=True)
