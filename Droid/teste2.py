from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from spacy.cli import download
from bs4 import BeautifulSoup
import time
time.clock = time.perf_counter


chatbot = ChatBot('Meu Bot')


trainer = ListTrainer(chatbot)
trainer.train("chatterbot.corpus.portuguese")


url = "https://www.investopedia.com/terms/p/prospectus.asp"


def get_prospectus_definition():
    
    response = chatbot.get(url)

    # Criar um objeto BeautifulSoup com o conteúdo HTML da página
    soup = BeautifulSoup(response.content, 'html.parser')

    definition = soup.find('div', {'class': 'comp article-body'}).find_all('p')[1].get_text()

    return definition

# Função para responder às perguntas do usuário
def get_bot_response(user_input):
    if 'prospectus' in user_input:
        # Se a pergunta do usuário contiver a palavra "prospectus", extrair a definição da página da Investopedia
        definition = get_prospectus_definition()
        return definition
    else:
        # Caso contrário, deixe o chatbot fornecer uma resposta padrão
        response = chatbot.get_response(user_input)
        return response.text

# Testar o chatbot
while True:
    user_input = input("Usuário: ")
    response = get_bot_response(user_input)
    print("Bot:", response)
