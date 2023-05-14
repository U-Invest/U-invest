import PyPDF2
import re
import datetime
import tkinter as tk
from tkinter import messagebox

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
preco_oferta = re.findall(r'Preço\s+por\s+ação\s*:? *R?\$? *([\d,.]+)\s*', prospecto_text)
quantidade_oferta = re.findall(r'Quantidade\s+de\s+ações\s+ofertadas\s*:? *([\d,.]+)\s*', prospecto_text)
valor_total_oferta = re.findall(r'Valor\s+total\s+da\s+oferta\s*:? *R?\$? *([\d,.]+)\s*', prospecto_text)
data_inicio_oferta = re.findall(r'Data\s+de\s+início\s+da\s+oferta\s*:? *([\d/]+)\s*', prospecto_text)
data_fim_oferta = re.findall(r'Data\s+de\s+término\s+da\s+oferta\s*:? *([\d/]+)\s*', prospecto_text)
objetivo_oferta = re.findall(r'Objetivo\s+da\s+oferta\s*:? *(.+?)\s*(?=Caracter|Riscos|Informa|\Z)', prospecto_text,
                             re.DOTALL)
garantias_oferta = re.findall(
    r'Garantias\s+oferecidas\s+aos\s+investidores\s*:? *(.+?)\s*(?=Objetivo|Caracter|Riscos|Informa|\Z)',
    prospecto_text, re.DOTALL)
riscos_oferta = re.findall(
    r'Riscos\s+envolvidos\s+na\s+oferta\s*:? *(.+?)\s*(?=Objetivo|Caracter|Garantias|Informa|\Z)', prospecto_text,
    re.DOTALL)
informacoes_oferta = re.findall(
    r'Informações\s+sobre\s+a\s+empresa\s+e\s+a\s+oferta\s*:? *(.+?)\s*(?=Objetivo|Caracter|Garantias|Riscos|\Z)',
    prospecto_text, re.DOTALL)

# Criar arquivo de texto e salvar informações
try:
    with open('informacoes_prospecto.txt', 'w') as txt_file:
        if preco_oferta:
            txt_file.write('Preço por ação: R$ {}\n\n'.format(preco_oferta[0]))
        if quantidade_oferta:
            txt_file.write('Quantidade de ações ofertadas: {}\n\n'.format(quantidade_oferta[0]))
        if valor_total_oferta:
            txt_file.write('Valor total da oferta: R$ {}\n\n'.format(valor_total_oferta[0]))
        if data_inicio_oferta:
            txt_file.write('Data de início da oferta: {}\n\n'.format(data_inicio_oferta[0]))
        if data_fim_oferta:
            txt_file.write('Data de término da oferta: {}\n\n'.format(data_fim_oferta[0]))
        if objetivo_oferta:
            txt_file.write('Objetivo da oferta: {}\n\n'.format(objetivo_oferta[0].strip()))
        if garantias_oferta:
            txt_file.write('Garantias oferecidas aos investidores: {}\n\n'.format(garantias_oferta[0].strip()))
        if riscos_oferta:
            txt_file.write('Riscos envolvidos na oferta: {}\n\n'.format(riscos_oferta[0].strip()))
        if informacoes_oferta:
            txt_file.write('Informações sobre a empresa e a oferta: {}\n\n'.format(informacoes_oferta[0].strip()))
    messagebox.showinfo(title='Sucesso', message='As informações foram salvas no arquivo "informacoes_prospecto.txt"')
except:
    messagebox.showerror(title='Erro', message='Ocorreu um erro ao criar o arquivo de texto')


