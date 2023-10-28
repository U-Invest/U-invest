import os
import webbrowser
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import PyPDF2
import re
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


# SUMARIZAÇÂO

def selecionar_arquivo_por_id(id_escolhido, caminho_pasta, caminho_pasta_txt, caminho_pasta_saida):
    nomes_arquivos = []
    for nome_arquivo in os.listdir(caminho_pasta):
        if os.path.isfile(os.path.join(caminho_pasta, nome_arquivo)):
            nome_sem_extensao = os.path.splitext(nome_arquivo)[0]
            nomes_arquivos.append(nome_sem_extensao)

    if 1 <= id_escolhido <= len(nomes_arquivos):
        nome_escolhido = nomes_arquivos[id_escolhido - 1]
        print(
            '\033[1;32m'f'Você selecionou a empresa: {nome_escolhido}''\033[0; 0m')

        pdf_path = os.path.join(caminho_pasta, f"{nome_escolhido}.pdf")
        txt_path = os.path.join(
            caminho_pasta_txt, f"{nome_escolhido}_indice.txt")

        extrair_pagina_indice(pdf_path, txt_path)
        numeroDescricaoOferta = buscar_descricao_oferta(txt_path)
        numeroPrecoAcao = buscar_preco_acao(txt_path)
        numeroPulicoAlvo = buscar_publico_alvo(txt_path)

    resultados = {
        "empresa_selecionada": nome_escolhido,
        "descricao_oferta": None,
        "preco_por_acao": None,
        "publico_alvo": None
    }

    if numeroDescricaoOferta is not None:
        descOferta = salvar_pagina_por_numero(
            pdf_path, numeroDescricaoOferta, caminho_pasta_saida)
        palavra_chave = 'Descrição da Oferta'
        nome_arquivo = descOferta
        resultados["descricao_oferta"] = encontrar_descricao_oferta(
            palavra_chave, nome_arquivo)

    if numeroPrecoAcao is not None:
        precoAcao = salvar_pagina_por_numero(
            pdf_path, numeroPrecoAcao, caminho_pasta_saida)
        palavra_chave = 'Preço por Ação'
        nome_arquivo = precoAcao
        resultados["preco_por_acao"] = encontrar_preco_acao(
            palavra_chave, nome_arquivo)

    if numeroPulicoAlvo is not None:
        publicoAlvo = salvar_pagina_por_numero(
            pdf_path, numeroPulicoAlvo, caminho_pasta_saida)
        palavra_chave = 'Público Alvo'
        nome_arquivo = publicoAlvo
        resultados["publico_alvo"] = encontrar_publico_alvo(
            palavra_chave, nome_arquivo)

    return resultados


def extrair_pagina_indice(pdf_path, txt_path):
    with open(pdf_path, 'rb') as arquivo_pdf:
        leitor_pdf = PyPDF2.PdfReader(arquivo_pdf)
        pagina_indice = None
        for num_pagina in range(len(leitor_pdf.pages)):
            pagina = leitor_pdf.pages[num_pagina]
            texto_pagina = pagina.extract_text()
            if 'ÍNDICE' in texto_pagina:
                pagina_indice = pagina
                break
        if pagina_indice is not None:
            texto_indice = pagina_indice.extract_text()
            with open(txt_path, 'w', encoding='utf-8') as arquivo_txt:
                arquivo_txt.write(texto_indice)
        else:
            print(
                f'Erro: Página de índice não encontrada no arquivo "{pdf_path}".')


def buscar_descricao_oferta(txt_path):
    with open(txt_path, 'r', encoding='utf-8') as arquivo_txt:
        linhas = arquivo_txt.readlines()

        for linha in linhas:
            if 'descrição da oferta' in linha.lower():
                numeros = re.findall(r'\d+', linha)
                if numeros:
                    numero_final = int(numeros[-1])
                    return numero_final
                break
        else:
            print('A palavra "descrição da oferta" não foi encontrada na página.')
    return None


def buscar_preco_acao(txt_path):
    with open(txt_path, 'r', encoding='utf-8') as arquivo_txt:
        linhas = arquivo_txt.readlines()
        for linha in linhas:
            if 'preço por ação' in linha.lower():
                numeros = re.findall(r'\d+', linha)
                if numeros:
                    numero_final = int(numeros[-1])
                    return numero_final
                break
        else:
            print('A palavra "Preço por Ação" não foi encontrada na página.')
    return None


def buscar_publico_alvo(txt_path):
    with open(txt_path, 'r', encoding='utf-8') as arquivo_txt:
        linhas = arquivo_txt.readlines()
        for linha in linhas:
            if 'público alvo' in linha.lower():
                numeros = re.findall(r'\d+', linha)
                if numeros:
                    numero_final = int(numeros[-1])
                    return numero_final
                break
        else:
            print('A palavra "Público Alvo" não foi encontrada na página.')
    return None


def buscar_pagina_por_numero(pdf_path, numero):
    with open(pdf_path, 'rb') as arquivo_pdf:
        leitor_pdf = PyPDF2.PdfReader(arquivo_pdf)

        numero_pagina = numero + 4

        if 1 <= numero_pagina <= len(leitor_pdf.pages):
            pagina = leitor_pdf.pages[numero_pagina - 1]
            texto_pagina = pagina.extract_text()
            return texto_pagina
        else:
            print(
                f'Erro: Número da página {numero_pagina} fora do intervalo de páginas do PDF.')
    return None


def salvar_pagina_por_numero(pdf_path, numero, caminho_pasta_saida):
    texto_pagina = buscar_pagina_por_numero(pdf_path, numero)
    if texto_pagina:
        nome_arquivo_saida = f"pagina_{numero + 4}.txt"
        caminho_arquivo_saida = os.path.join(
            caminho_pasta_saida, nome_arquivo_saida)
        with open(caminho_arquivo_saida, 'w', encoding='utf-8') as arquivo_saida:
            arquivo_saida.write(texto_pagina)
        return f"./paginas/{nome_arquivo_saida}"


def encontrar_descricao_oferta(palavra_chave, nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
        descricao_oferta = ""  # Inicializa a string que armazenará a descrição da oferta

        for i in range(len(linhas)):
            linha = linhas[i].lower().strip()
            if palavra_chave.lower() in linha:
                proximo_paragrafo = ""
                for j in range(i + 1, len(linhas)):
                    proxima_linha = linhas[j].strip()
                    if '.' in proxima_linha:  # Se encontrarmos um ponto, assumimos o fim do parágrafo
                        ponto_index = proxima_linha.index('.')
                        proximo_paragrafo += proxima_linha[:ponto_index + 1]
                        break  # Sai do loop quando um ponto é encontrado
                    # Adiciona linhas ao parágrafo enquanto não encontrar um ponto
                    proximo_paragrafo += proxima_linha + " "

                # Atribui o parágrafo encontrado à variável descricao_oferta
                descricao_oferta = proximo_paragrafo.strip()
                break  # Sai do loop principal uma vez que o parágrafo foi encontrado e atribuído

    return descricao_oferta  # Retorna a descrição da oferta encontrada


def encontrar_preco_acao(palavra_chave, nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
        preco_acao = ""  # Inicializa a string que armazenará o preço por ação

        for i in range(len(linhas)):
            linha = linhas[i].lower().strip()
            if palavra_chave.lower() in linha:
                proximo_paragrafo = ""
                for j in range(i + 1, len(linhas)):
                    proxima_linha = linhas[j].strip()
                    if '.' in proxima_linha:
                        ponto_index = proxima_linha.index('.')
                        proximo_paragrafo += proxima_linha[:ponto_index + 1]
                        break
                    proximo_paragrafo += proxima_linha + " "

                # Atribui o parágrafo encontrado à variável preco_acao
                preco_acao = proximo_paragrafo.strip()
                break

    return preco_acao  # Retorna o preço por ação encontrado


def encontrar_publico_alvo(palavra_chave, nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
        publico_alvo = ""  # Inicializa a string que armazenará o público-alvo

        for i in range(len(linhas)):
            linha = linhas[i].lower().strip()
            if palavra_chave.lower() in linha:
                proximo_paragrafo = ""
                for j in range(i + 1, len(linhas)):
                    proxima_linha = linhas[j].strip()
                    if '.' in proxima_linha:
                        ponto_index = proxima_linha.index('.')
                        proximo_paragrafo += proxima_linha[:ponto_index + 1]
                        break
                    proximo_paragrafo += proxima_linha + " "

                # Atribui o parágrafo encontrado à variável publico_alvo
                publico_alvo = proximo_paragrafo.strip()
                break

def open_google():
    url = 'https://statusinvest.com.br/ipo/acoes'
    webbrowser.open(url)
    return 'Site aberto no navegador!'

    return publico_alvo  # Retorna o público-alvo encontrado
