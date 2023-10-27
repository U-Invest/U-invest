from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import nltk
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer

nltk.download('stopwords')
nltk.download('punkt')

stemmer = SnowballStemmer('portuguese')
stop_words = stopwords.words('portuguese')

with open('ipo.txt', 'r', encoding="UTF8") as f:
    raw_data = f.read()

pairs = [pair.split('\n') for pair in raw_data.split('\n\n')]
pairs = [(pair[0], pair[1]) for pair in pairs if len(pair) > 1]


def preprocess(text):
    tokens = nltk.word_tokenize(text.lower())
    tokens = [token for token in tokens if token not in stop_words]
    stemmed_tokens = [stemmer.stem(token) for token in tokens]
    return " ".join(stemmed_tokens)


preprocessed_pairs = [(preprocess(pair[0]), pair[1]) for pair in pairs]

vectorizer = TfidfVectorizer()
corpus = [pair[0] for pair in preprocessed_pairs]
X = vectorizer.fit_transform(corpus)


def chatbot_response(user_input):
    try:
        response = None
        user_input = preprocess(user_input)
        input_vec = vectorizer.transform([user_input])
        sim_scores = cosine_similarity(input_vec, X)
        idx = sim_scores.argmax()
        if sim_scores[0][idx] > 0:
            response = preprocessed_pairs[idx][1]
        else:
            response = default_response(user_input)
        return response
    except Exception as e:
        print(
            '\033[1;31m'f'Erro ao processar a entrada do usuário: {e}''\033[0; 0m')
        return None


def default_response(user_input):
    return 'Desculpe, não entendi. Pode reformular a pergunta?'
