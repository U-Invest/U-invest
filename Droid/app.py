import os
import textwrap
from flask import Flask, jsonify, request
from imports import chatbot_response
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

        return jsonify({
            "boas_vindas": boas_vindas,
            "opcoes": opcoes
        })

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
    data = request.get_json()
    question = data.get('question')
    response = chatbot_response(question)
    wrapped_response = textwrap.wrap(response, width=50)
    wrapped_response_str = " ".join(wrapped_response)
    return jsonify({"response": wrapped_response_str})


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


@app.route('/prospecto', methods=['GET'])
def obter_prospecto():
    try:
        # Obtém o ID do parâmetro de query
        id_prospecto = request.args.get('id')

        if id_prospecto is None or not id_prospecto.isdigit() or int(id_prospecto) < 1 or int(id_prospecto) > 5:
            return jsonify({"error": "ID inválido. Por favor, forneça um ID entre 1 e 5."})

        caminho_pasta = "prospectos"
        prospectos = os.listdir(caminho_pasta)
        prospectos.sort()  # Certificando-se de que os prospectos estão em ordem

        index = int(id_prospecto) - 1  # Convertendo ID para índice base zero

        if index < len(prospectos):
            nome_prospecto = prospectos[index]
            return jsonify({"prospecto_selecionado": nome_prospecto})
        else:
            return jsonify({"error": "Nenhum prospecto encontrado com o ID fornecido."})

    except Exception as e:
        return jsonify({"error": f"Um erro ocorreu: {e}"})


if __name__ == '__main__':
    app.run(debug=True)
