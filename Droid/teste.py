import requests
from bs4 import BeautifulSoup

# Defina a URL da página que você deseja analisar
url = 'https://statusinvest.com.br/ipo/acoes'

# Faz a requisição HTTP para a página
response = requests.get(url)

# Verifica se a requisição foi bem sucedida
if response.status_code == 200:
    # Cria o objeto BeautifulSoup com o conteúdo da página
    soup = BeautifulSoup(response.content, 'html.parser')

    # Agora você pode usar os métodos do BeautifulSoup para extrair dados da página
    # Por exemplo, para extrair todos os links da página, você pode fazer o seguinte:
    links = soup.find_all('h3')
    
    # Para extrair o texto de cada link, você pode iterar sobre a lista de links:
    for link in links:
        print(link.text)
else:
    print('Falha ao carregar a página:', response.status_code)
