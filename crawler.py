import requests
from bs4 import BeautifulSoup

anchieta = 'https://anchieta.br' 

r = requests.get(anchieta)
html_anchieta = r.text

soup = BeautifulSoup(html:_anchieta)
for elem in soup. find_all('div', calss_='elementor-widget-container'):
    print(elem.text)
