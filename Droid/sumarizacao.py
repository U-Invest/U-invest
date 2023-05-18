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

# Identificar as informações
capital_social = re.findall(r'Capital\s+Social\s*:? *([\d,.]+)\s*', prospecto_text, re.IGNORECASE)
data_liquidacao = re.findall(r'Data\s+de\s+Liquidação\s*:? *([\d/]+)\s*', prospecto_text, re.IGNORECASE)
corretora = re.findall(r'Corretora\s*:? *(.+?)\s*(?=Aviso\s+ao\s+Mercado|\Z)', prospecto_text, re.DOTALL | re.IGNORECASE)
aviso_ao_mercado = re.findall(r'Aviso\s+ao\s+Mercado\s*:? *(.+?)\s*(?=Capital\s+Social|Data\s+de\s+Liquidação|\Z)', prospecto_text, re.DOTALL | re.IGNORECASE)

# Salvar as informações em um arquivo de texto
with open('informacoes.txt', 'w', encoding='utf-8') as txt_file:
    if capital_social:
        txt_file.write('**Capital Social:** R$' + capital_social[0].replace(',', '') + '\n')
        txt_file.write('\n')
    if data_liquidacao:
        txt_file.write('**Data de Liquidação:** ' + data_liquidacao[0] + '\n')
        txt_file.write('\n')
    if corretora:
        txt_file.write('**Corretora:** ' + corretora[0] + '\n')
        txt_file.write('\n')
    if aviso_ao_mercado:
        aviso_resumido = aviso_ao_mercado[0][:100] + '...' if len(aviso_ao_mercado[0]) > 100 else aviso_ao_mercado[0]
        txt_file.write('**Aviso ao Mercado:** ' + aviso_resumido + '\n')
        txt_file.write('\n')

print('As informações foram salvas no arquivo informacoes.txt')

# Sumarizar as informações
summary = ''

if capital_social:
    summary += f"**Capital Social:** R${capital_social[0].replace(',', '')[:50]}...\n\n"

if data_liquidacao:
    summary += f"**Data de Liquidação:** {data_liquidacao[0][:50]}...\n\n"

if corretora:
    summary += f"**Corretora:** {corretora[0][:50]}...\n\n"

if aviso_ao_mercado:
    aviso_resumido = aviso_ao_mercado[0][:100] + '...' if len(aviso_ao_mercado[0]) > 100 else aviso_ao_mercado[0]
    summary += f"**Aviso ao Mercado:** {aviso_resumido[:50]}...\n\n"

print("Resumo das informações:")
print(summary)
