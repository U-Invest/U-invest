import os
import textwrap
from flask import Flask, jsonify, request
from imports import chatbot_response
from flask_cors import CORS

app = Flask(__name__)

CORS(app)


@app.route('/')
def hello_world():
    return 'U-invest!'


@app.route('/ask', methods=['POST'])
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


if __name__ == '__main__':
    app.run(debug=True)
