from flask import Flask, request, jsonify
import textwrap
from sklearn.metrics.pairwise import cosine_similarity
from droid import default_response, preprocess
from sklearn.feature_extraction.text import TfidfVectorizer

app = Flask(__name__)

with open('ipo.txt', 'r' ,encoding= "UTF8") as f:
    raw_data = f.read()
    
pairs = [pair.split('\n') for pair in open.raw_data_manager.split('\n\n')]
pairs = [(pair[0], pair[1]) for pair in pairs if len(pair) > 1]

preprocessed_pairs = [(preprocess(pair[0]), pair[1]) for pair in pairs]

vectorizer = TfidfVectorizer()
corpus = [pair[0] for pair in preprocessed_pairs]
X = vectorizer.fit_transform(corpus)

def chatbot_response(question):
    try:
        response = None
        user_input = preprocess(question)  # Corrigido para usar 'question'
        input_vec = vectorizer.transform([user_input])  # Corrigido para usar 'vectorizer'
        sim_scores = cosine_similarity(input_vec, X)
        idx = sim_scores.argmax()
        if sim_scores[0][idx] > 0:
            response = preprocessed_pairs[idx][1]
        else:
            response = default_response(user_input)
        return response
    except Exception as e:
        print(f'Erro ao processar a entrada do usuário: {e}')
        return None

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    question = data.get('question')
    
    response = chatbot_response(question)
    wrapped_response = textwrap.wrap(response, width=50)
    
    # Convertendo as linhas de resposta wrapped em uma única string
    wrapped_response_str = "\n".join(wrapped_response)
    
    return jsonify({"response": wrapped_response_str})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
