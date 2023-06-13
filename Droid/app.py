# from flask import Flask, jsonify, render_template, request

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/api/saudacao', methods=['POST'])
# def saudacao():
#     nome = request.json.get('nome')
#     mensagem = f'Olá, {nome}! Bem-vindo à integração Python-Frontend.'
#     return jsonify({'mensagem': mensagem})

# if __name__ == '__main__':
#     app.run()

from flask import Flask

app = Flask(__name__)


@app.route('/api/chat', methods=['POST'])
def chat():
    # Lógica do chatbot aqui
    return 'Resposta do chatbot'


if __name__ == '__main__':
    app.run()
