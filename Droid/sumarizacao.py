import PyPDF2
import re

# Ler o prospecto
try:
    with open('prospecto.pdf', 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        prospecto_text = ''
        for page in pdf_reader.pages:
            prospecto_text += page.extract_text()
except FileNotFoundError:
    print('O arquivo do prospecto não foi encontrado')
    exit()

# Nomes possíveis
nomes_possiveis = ['PRIVALIA BRASIL', 'CFL', 'AÇU PETRÓLEO', 'PRIVALIA BRASIL',
                   "ENTALPIA PARTICIPAÇÕES", "YUNY", "EZ INC", "LIVETECH DA BAHIA INDÚSTRIA E COMÉRCIO",
                   "NORTIS", "LABORATÓRIO TEUTO BRASILEIRO", "GRANBIO", "GRUPO MPR"]

# CNPJs possíveis
cnpjs_possiveis = ['12345678000123', '98765432000198', '87654321000145']

# Identificar o nome da empresa
nome_empresa_encontrado = None
for nome in nomes_possiveis:
    if re.search(r'\b' + re.escape(nome) + r'\b', prospecto_text, re.IGNORECASE):
        nome_empresa_encontrado = nome
        break

# Identificar possíveis CNPJs
cnpjs_encontrados = []
for cnpj in cnpjs_possiveis:
    if re.search(cnpj, prospecto_text):
        cnpjs_encontrados.append(cnpj)

# Salvar o nome da empresa e os CNPJs encontrados em um arquivo de texto
with open('nome_cnpj.txt', 'w', encoding='utf-8') as txt_file:
    if nome_empresa_encontrado:
        txt_file.write(f'Nome da empresa: {nome_empresa_encontrado}\n\n')
    if cnpjs_encontrados:
        txt_file.write('CNPJs encontrados:\n')
        for cnpj in cnpjs_encontrados:
            txt_file.write(cnpj + '\n')

if nome_empresa_encontrado:
    print(f'Nome da empresa: "{nome_empresa_encontrado}"')
else:
    print('Nenhum dos nomes possíveis foi encontrado no prospecto.')

if cnpjs_encontrados:
    print('CNPJs encontrados:')
    for cnpj in cnpjs_encontrados:
        print(cnpj)
else:
    print('Nenhum dos CNPJs possíveis foi encontrado no prospecto.')
