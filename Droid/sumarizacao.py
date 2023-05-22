import os
import PyPDF2
import re

def limpaTerminal():
    return os.system('cls' if os.name == 'nt' else 'clear')

def criaBarra():
    return print('-' * 32)

def extrair_pagina_indice(pdf_path, txt_path):
    with open(pdf_path, 'rb') as arquivo_pdf:
        leitor_pdf = PyPDF2.PdfReader(arquivo_pdf)

        # Buscar pela página com o título "Índice"
        pagina_indice = None
        for num_pagina in range(len(leitor_pdf.pages)):
            pagina = leitor_pdf.pages[num_pagina]
            texto_pagina = pagina.extract_text()
            if 'ÍNDICE' in texto_pagina:
                pagina_indice = pagina
                break

        if pagina_indice is not None:
            texto_indice = pagina_indice.extract_text()

            # Salvar a página de índice em um arquivo TXT
            with open(txt_path, 'w', encoding='utf-8') as arquivo_txt:
                arquivo_txt.write(texto_indice)

            # print(f'Página de índice extraída com sucesso! O arquivo "{pdf_path}" foi convertido para "{txt_path}".')
        else:
            print(f'Erro: Página de índice não encontrada no arquivo "{pdf_path}".')

def buscar_descricao_oferta(txt_path):
    with open(txt_path, 'r', encoding='utf-8') as arquivo_txt:
        linhas = arquivo_txt.readlines()

        for linha in linhas:
            if 'descrição da oferta' in linha.lower():
                # print(f'Linha encontrada: {linha.strip()}')
                numeros = re.findall(r'\d+', linha)
                if numeros:
                    numero_final = int(numeros[-1])
                    # print(f'Número encontrado: {numero_final}')
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
                # print(f'Linha encontrada: {linha.strip()}')
                numeros = re.findall(r'\d+', linha)
                if numeros:
                    numero_final = int(numeros[-1])
                    # print(f'Número encontrado: {numero_final}')
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
                # print(f'Linha encontrada: {linha.strip()}')
                numeros = re.findall(r'\d+', linha)
                if numeros:
                    numero_final = int(numeros[-1])
                    # print(f'Número encontrado: {numero_final}')
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
            print(f'Erro: Número da página {numero_pagina} fora do intervalo de páginas do PDF.')
    return None

def salvar_pagina_por_numero(pdf_path, numero, caminho_pasta_saida):
    texto_pagina = buscar_pagina_por_numero(pdf_path, numero)
    if texto_pagina:
        nome_arquivo_saida = f"pagina_{numero + 4}.txt"
        caminho_arquivo_saida = os.path.join(caminho_pasta_saida, nome_arquivo_saida)
        with open(caminho_arquivo_saida, 'w', encoding='utf-8') as arquivo_saida:
            arquivo_saida.write(texto_pagina)
        # print(f'Página do PDF {pdf_path}, referente ao número {numero + 4}, salva em: {caminho_arquivo_saida}.')
        return f"./paginas/{nome_arquivo_saida}"

def encontrar_descricao_oferta(palavra_chave, nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()

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
                print(proximo_paragrafo.strip())
                break

def encontrar_preco_acao(palavra_chave, nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()

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
                print(proximo_paragrafo.strip())
                break
            
def encontrar_publico_alvo(palavra_chave, nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()

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
                print(proximo_paragrafo.strip())
                break

def selecionar_arquivo(caminho_pasta, caminho_pasta_txt, caminho_pasta_saida):
    nomes_arquivos = []
    for nome_arquivo in os.listdir(caminho_pasta):
        if os.path.isfile(os.path.join(caminho_pasta, nome_arquivo)):
            nome_sem_extensao = os.path.splitext(nome_arquivo)[0]
            nomes_arquivos.append(nome_sem_extensao)

    print('\033[1;96m''Selecione sobre qual empresa você deseja abrir o prospecto para ler:''\033[0;0m')
    for i, nome in enumerate(nomes_arquivos, start=1):
        print('\033[1;96m'f'{i}.''\033[0;0m'f'{nome}')

    escolha = input('\033[1;96m''Digite o número correspondente ao prospecto desejado: ''\033[0;0m')
    escolha = int(escolha)

    if 1 <= escolha <= len(nomes_arquivos):
        nome_escolhido = nomes_arquivos[escolha - 1]
        print('\033[1;32m'f'Você selecionou a empresa: {nome_escolhido}''\033[0; 0m')

        pdf_path = os.path.join(caminho_pasta, f"{nome_escolhido}.pdf")
        txt_path = os.path.join(caminho_pasta_txt, f"{nome_escolhido}_indice.txt")

        extrair_pagina_indice(pdf_path, txt_path)
        numeroDescricaoOferta = buscar_descricao_oferta(txt_path)
        numeroPrecoAcao = buscar_preco_acao(txt_path)
        numeroPulicoAlvo = buscar_publico_alvo(txt_path)
        
        if numeroDescricaoOferta is not None:
            descOferta = salvar_pagina_por_numero(pdf_path, numeroDescricaoOferta, caminho_pasta_saida)
            palavra_chave = 'Descrição da Oferta'
            nome_arquivo = descOferta
            print('\033[1;96m''Descrição da Oferta\n''\033[0;0m')
            encontrar_descricao_oferta(palavra_chave, nome_arquivo)
            criaBarra()
            
        if numeroPrecoAcao is not None:
            print('\033[1;96m''Preço por Ação\n''\033[0;0m')
            precoAcao = salvar_pagina_por_numero(pdf_path, numeroPrecoAcao, caminho_pasta_saida)
            palavra_chave = 'Preço por Ação'
            nome_arquivo = precoAcao
            encontrar_preco_acao(palavra_chave, nome_arquivo)
            criaBarra()
            
        if numeroPulicoAlvo is not None:
            print('\033[1;96m''Público Alvo\n''\033[0;0m')
            publicoAlvo = salvar_pagina_por_numero(pdf_path, numeroPulicoAlvo, caminho_pasta_saida)
            palavra_chave = 'Público Alvo'
            nome_arquivo = publicoAlvo
            encontrar_publico_alvo(palavra_chave, nome_arquivo)
            criaBarra()
            
    else:
        print("Escolha inválida.")
