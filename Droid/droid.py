from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from spacy.cli import download

download("pt_core_news_sm")

class PTSM:
    ISO_639_1 = 'pt_core_news_sm'

chatbot = ChatBot("Droid", tagger_language=PTSM)

IPO = [
"Você sabe o que é um IPO?",
"Sim, IPO é o processo pelo qual uma empresa se torna pública pela primeira vez, vendendo ações para investidores em um mercado de ações.",
"Quais são as vantagens de fazer um IPO?",
"Fazer um IPO pode fornecer à empresa acesso a mais capital, aumentar a visibilidade e a credibilidade da empresa, e permitir que os acionistas existentes vendam suas ações.",
"Quais são as desvantagens de fazer um IPO?",
"Fazer um IPO pode ser caro e demorado, requerer maior divulgação e transparência financeira, e pode resultar em uma perda de controle da empresa pelos fundadores.",
"Como é determinado o preço das ações em um IPO?",
"O preço das ações é geralmente determinado por meio de um processo de bookbuilding, no qual os bancos de investimento que administram o IPO coletam as ofertas dos investidores e determinam o preço que maximiza a arrecadação de fundos para a empresa."
]

trainer = ListTrainer(chatbot)
trainer.train(IPO)

pergunta = "O que é (IPO)?"
resposta = chatbot.get_response(pergunta)
print(resposta)
