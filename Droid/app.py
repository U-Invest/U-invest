import textwrap
from duvidas import chatbot_response
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/droid', methods=['POST'])
def postOption():
    data = request.get_json()  # Obtém o JSON enviado no corpo da requisição
    if data is None:
        return jsonify({'error': 'Nenhum dado encontrado'})

    duvida = data.get('duvida', '')  # Obtém o valor da chave 'duvida' no JSON

    response = chatbot_response(duvida)
    wrapped_response = textwrap.wrap(response, width=50)

    finalResponse = ""

    for line in wrapped_response:
        finalResponse += line

    response_data = {'response': f'{finalResponse}'}
    return jsonify(response_data)


if __name__ == '__main__':
    app.run()
