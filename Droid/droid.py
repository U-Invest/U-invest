import nltk
import textwrap
import webbrowser
import json
from nltk.chat.util import Chat, reflections
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.tokenize import sent_tokenize
from heapq import nlargest
nltk.download('stopwords')
nltk.download('punkt')   

stemmer = SnowballStemmer('portuguese')
stop_words = stopwords.words('portuguese')

with open('ipo.txt', 'r' ,encoding= "UTF8") as f:
    raw_data = f.read()

pairs = [pair.split('\n') for pair in raw_data.split('\n\n')]
pairs = [(pair[0], pair[1]) for pair in pairs if len(pair) > 1]

print("\033[1;34m" + "-" * 89)
print("-" * 89 + "\033[m")
print("\033[97;42mBem-vindo ao Droid! Eu sou um chatbot sobre IPOs. Como posso ajudá-lo?\033[m")
print("\033[1;34m" + "-" * 89)
print("-" * 89 + "\033[m")

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
        print(f"\033[1;31mErro ao processar a entrada do usuário: {e}\033[m")
        return None
    
def default_response(user_input):
    return "\033[1;31mDesculpe, não entendi. Pode reformular a pergunta?\033[m"

def show_menu():
    print("\033[1;34mEscolha uma das opções abaixo:\033[m")
    print("\033[1m1 - Tirar dúvidas sobre IPO\033[m")
    print("\033[1m2 - Sumarizar o prospecto\033[m")
    print("\033[1m3 - Abrir pagina com prospectos\033[m")
    print("\033[1m4 - Sair\033[m")

def handle_choice(choice):
    if choice == "1":
        question = input("\033[1;32mDigite sua pergunta: \033[m")
        response = chatbot_response(question)
        wrapped_response = textwrap.wrap(response, width=50)
        for line in wrapped_response:
            print(line)
        print()  
    elif choice == "2":
        print("Em desenvolvimento")
    elif choice == "3":
        open_google()
    elif choice == "4":
        print("Até mais!")
        avaliacoes = [] 
        try:
            with open("avaliacoes.json", "r") as file:
                avaliacoes = json.load(file)
        except FileNotFoundError:
            pass
        while True:
            print("\033[1;34mPor favor, avalie o chatbot. Digite uma nota de 1 a 5 (sendo 1 a pior e 5 a melhor):\033[m")
            rating = input("\033[1;32mSua avaliação: \033[m")
            if rating.isdigit() and 1 <= int(rating) <= 5:
                avaliacoes.append(int(rating))
                print("\033[97;42mAvaliação enviada. Obrigado!\033[m")
                with open("avaliacoes.json", "w") as file:
                    json.dump(avaliacoes, file)
                exit()
            else:
                print("\033[1;31mAvaliação inválida. Por favor, digite uma nota de 1 a 5.\033[m")
    elif choice.isdigit() and 1 <= int(choice) <= 4:
        print("Opção em desenvolvimento")
    elif choice.isdigit():
        print("\033[1;31mOpção inválida. Por favor, tente novamente.\033[m")
    else:
        print("\033[1;31mEntrada inválida. Por favor, tente novamente.\033[m")

def open_google():
     webbrowser.open('https://statusinvest.com.br/ipo/acoes')
     show_menu()
     choice = input("\033[1;32mDigite sua escolha: \033[m")
     handle_choice(choice)

while True:
    show_menu()
    choice = input("\033[1;32mDigite sua escolha: \033[m")
    handle_choice(choice)