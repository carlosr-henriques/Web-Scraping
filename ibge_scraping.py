import requests
from bs4 import BeautifulSoup
import pandas as pd

def scraping_website(uf: str):
    url = f"https://www.ibge.gov.br/cidades-e-estados/{uf}.html"
    browsers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"}
    page = requests.get(url, browsers)
    soup = BeautifulSoup(page.content, 'html.parser')
    uf_dict = {
        dado.select(".ind-label")[0].text: dado.select(".ind-value")[0].text
        for dado in soup.select(".indicador")
    }

    return uf_dict

for estado in ["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"]:
    uf = scraping_website(estado.lower())
    for indicador in uf:
        if "]" in uf[indicador]:
            uf[indicador] = uf[indicador].split("]")[0][:-8]
        else:
            pass
    print(uf)
