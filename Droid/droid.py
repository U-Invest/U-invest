#nltk: Biblioteca para processamento de linguagem natural. Pode ser instalada usando o comando pip install nltk.
#scikit-learn: Biblioteca para aprendizado de máquina e processamento de dados. Pode ser instalada usando o comando pip install scikit-learn.
import nltk
import textwrap
import webbrowser
from nltk.chat.util import Chat, reflections
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.tokenize import sent_tokenize
from heapq import nlargest
#nltk.download('stopwords')#Caso seja nessesario
#nltk.download('punkt')    #Caso seja nessesario

stemmer = SnowballStemmer('portuguese')
stop_words = stopwords.words('portuguese')

with open('ipo.txt', 'r' ,encoding= "UTF8") as f:
    raw_data = f.read()

pairs = [pair.split('\n') for pair in raw_data.split('\n\n')]
pairs = [(pair[0], pair[1]) for pair in pairs if len(pair) > 1]

# Adiciona mensagem de boas-vindas
print("\033[1;34m" + "-" * 89)
print("-" * 89 + "\033[m")
print("\033[97;42mBem-vindo ao Droid! Eu sou um chatbot sobre IPOs. Como posso ajudá-lo?\033[m")
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
    print("\033[1;34mEscolha uma das opções abaixo:\033[m")
    print("\033[1m1 - Tirar dúvidas sobre IPO\033[m")
    print("\033[1m2 - Sumarizar o prospecto\033[m")
    print("\033[1m3 - Abrir pagina com prospectos\033[m")
    print("\033[1m4 - Sair\033[m")

# Função que trata a escolha do usuário
def handle_choice(choice):
    if choice == "1":
        question = input("\033[1;32mDigite sua pergunta: \033[m")
        response = chatbot_response(question)
        wrapped_response = textwrap.wrap(response, width=50)  # Limite de 50 caracteres por linha
        for line in wrapped_response:
            print(line)
        print()  # Pular linha adicional
    elif choice == "2":
        print("Em desenvolvimento")
    elif choice == "3":
        open_google()
    elif choice == "4":
        print("Até mais!")
        print("\033[1;34mPor favor, avalie o chatbot. Digite uma nota de 1 a 5 (sendo 1 a pior e 5 a melhor):\033[m")
        rating = input("\033[1;32mSua avaliação: \033[m")
        if rating.isdigit() and 1 <= int(rating) <= 5:
            # Aqui você pode fazer o processamento da avaliação, como armazenar em um banco de dados ou arquivo
            print("Avaliação enviada. Obrigado!")
            exit()
        else:
            print("\033[1;31mAvaliação inválida. Por favor, digite uma nota de 1 a 5.\033[m")
    elif choice.isdigit() and 1 <= int(choice) <= 5:
        print("Opção em desenvolvimento")
    elif choice.isdigit():
        print("\033[1;31mOpção inválida. Por favor, tente novamente.\033[m")
    else:
        print("\033[1;31mEntrada inválida. Por favor, tente novamente.\033[m")
def open_google():
    # Abrir a página do Google
    webbrowser.open('https://statusinvest.com.br/ipo/acoes')
    # Voltar para o menu
    show_menu()
    choice = input("\033[1;32mDigite sua escolha: \033[m")
    handle_choice(choice)

# Loop principal do chatbot
while True:
    show_menu()
    choice = input("\033[1;32mDigite sua escolha: \033[m")
    handle_choice(choice)