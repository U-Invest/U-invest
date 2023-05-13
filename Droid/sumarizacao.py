import fitz
from nltk.tokenize import sent_tokenize
from heapq import nlargest
import nltk
from nltk.corpus import stopwords
stop_words = set(stopwords.words('portuguese'))

def summarize_pdf(input_file, output_file, summary_ratio=0.1):
    # Abrir o arquivo PDF
    with fitz.open(input_file) as pdf:
        num_pages = pdf.page_count
        text = ""

        # Extrair texto de todas as páginas
        for i in range(num_pages):
            page = pdf.load_page(i)
            text += page.get_text()

        # Tokenização das sentenças
        sentences = sent_tokenize(text)

        # Criar dicionário de frequência de palavras
        word_freq = {}
        for sentence in sentences:
            words = nltk.word_tokenize(sentence.lower())
            for word in words:
                if word not in stop_words:
                    if word not in word_freq.keys():
                        word_freq[word] = 1
                    else:
                        word_freq[word] += 1

        # Normalizar a frequência de palavras
        max_freq = max(word_freq.values())
        for word in word_freq.keys():
            word_freq[word] = word_freq[word]/max_freq

        # Calcular pontuação de cada sentença
        sentence_scores = {}
        for sentence in sentences:
            for word in nltk.word_tokenize(sentence.lower()):
                if word in word_freq.keys():
                    if len(sentence.split(' ')) < 30:
                        if sentence not in sentence_scores.keys():
                            sentence_scores[sentence] = word_freq[word]
                        else:
                            sentence_scores[sentence] += word_freq[word]

        # Selecionar as N sentenças mais importantes
        num_sentences = int(len(sentences)*summary_ratio)
        summary_sentences = nlargest(num_sentences, sentence_scores, key=sentence_scores.get)
        summary = ' '.join(summary_sentences)

        # Salvar o resultado em um arquivo PDF
        with open(output_file, 'wb') as f:
            pdf_writer = fitz.open()
            pdf_writer.insert_pdf(pdf)
            page = pdf_writer[-1]
            page.insert_text((0, 0), summary)
            pdf_writer.save(f)

        # Fechar o arquivo
        pdf_writer.close()
