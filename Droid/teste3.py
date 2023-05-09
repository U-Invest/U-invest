import requests
from bs4 import BeautifulSoup

# Define a URL da página que vamos fazer o scraping
url = 'https://www.investopedia.com/terms/p/prospectus.asp'

# Faz uma requisição HTTP GET para a URL
response = requests.get(url)

# Analisa o HTML da página usando a biblioteca BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Encontra o elemento HTML que contém as informações sobre prospectos
prospectus_definition = soup.find('div', {'class': 'comp article-body'})

# Extrai o texto resumido sobre prospectos
prospectus_summary = prospectus_definition.find_all('p')[1].text.strip()

# Imprime o resultado
print(prospectus_summary)
