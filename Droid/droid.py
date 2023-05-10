import nltk
from nltk.chat.util import Chat, reflections
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('stopwords')
nltk.download('punkt')

stemmer = SnowballStemmer('portuguese')
stop_words = stopwords.words('portuguese')

with open('ipo.txt', 'r') as f:
    raw_data = f.read()

pairs = [pair.split('\n') for pair in raw_data.split('\n\n')]
pairs = [(pair[0], pair[1]) for pair in pairs if len(pair) > 1]

# Adiciona mensagem de boas-vindas
pairs.insert(0, ("iniciar", "Olá, eu sou um chatbot sobre IPOs. Como posso ajudá-lo?"))

def preprocess(text):
    # Tokenização
    tokens = nltk.word_tokenize(text.lower())

    # Remoção de stop words
    tokens = [token for token in tokens if token not in stop_words]

    # Stemming
    stemmed_tokens = [stemmer.stem(token) for token in tokens]

    return " ".join(stemmed_tokens)

# Pré-processa as perguntas e respostas
preprocessed_pairs = [(preprocess(pair[0]), pair[1]) for pair in pairs]

# Cria o modelo TF-IDF
vectorizer = TfidfVectorizer()
corpus = [pair[0] for pair in preprocessed_pairs]
X = vectorizer.fit_transform(corpus)

# Cria o chatbot
def chatbot_response(user_input):
    response = None
    user_input = preprocess(user_input)
    input_vec = vectorizer.transform([user_input])
    sim_scores = cosine_similarity(input_vec, X)
    idx = sim_scores.argmax()
    if sim_scores[0][idx] > 0:
        response = preprocessed_pairs[idx][1]
    return response

# Função de resposta padrão
def default_response(user_input):
    return "Desculpe, não entendi. Pode reformular a pergunta?"

chatbot = Chat(pairs, reflections)
chatbot.respond = chatbot_response
chatbot.default_response = default_response
chatbot.converse()
