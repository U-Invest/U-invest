import textwrap
from flask import Flask, jsonify, request

from imports import chatbot_response

app = Flask(__name__)


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


if __name__ == '__main__':
    app.run(debug=True)
