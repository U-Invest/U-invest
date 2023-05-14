import nltk
from nltk.chat.util import Chat, reflections
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.tokenize import sent_tokenize
from heapq import nlargest


stemmer = SnowballStemmer('portuguese')
stop_words = stopwords.words('portuguese')

with open('ipo.txt', 'r' ,encoding= "UTF8") as f:
    raw_data = f.read()

pairs = [pair.split('\n') for pair in raw_data.split('\n\n')]
pairs = [(pair[0], pair[1]) for pair in pairs if len(pair) > 1]

# Adiciona mensagem de boas-vindas
print("\033[1;34m" + "-" * 89)
print("-" * 89 + "\033[m")
print("\033[1;32;7mBem-vindo ao Droid! Eu sou um chatbot sobre IPOs. Como posso ajudá-lo?\033[m")
print("\033[1;34m" + "-" * 89)
print("-" * 89 + "\033[m")

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
        print(f"\033[1;31mErro ao processar a entrada do usuário: {e}\033[m")
        return None

# Função de resposta padrão
def default_response(user_input):
    return "\033[1;31mDesculpe, não entendi. Pode reformular a pergunta?\033[m"
# Função que mostra as opções disponíveis
def show_menu():
    print("\033[34m\033[1mEscolha uma das opções abaixo:\033[m")
    print("\033[1m1 - Tirar dúvidas sobre IPO\033[m")
    print("\033[1m2 - Sumarizar o prospecto\033[m")
    print("\033[1m3 - Sair\033[m")

# Função que trata a escolha do usuário
def handle_choice(choice):
    if choice == "1":
        question = input("\033[1;32mDigite sua pergunta: \033[m")
        response = chatbot_response(question)
        print(response)
    elif choice == "2":
        print("em desenvolvimento")
    elif choice == "3":
        print("Até mais!")
        exit()
    else:
        print("\033[1;31mOpção inválida. Por favor, tente novamente.\033[m")

# Loop principal do chatbot
while True:
    show_menu()
    choice = input("\033[1;32mDigite sua escolha: \033[m")
    handle_choice(choice)