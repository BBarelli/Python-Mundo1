import requests
from bs4 import BeautifulSoup

# URL do site
url = "https://www.transfermarkt.com/ceara-sporting-club/startseite/verein/2029"
#Simula que é uma pessoa acessando o navegador
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/114.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": url
}

#Chama o endpoint
response = requests.get(url, headers=headers)
#Transforma o resultado em html.parser
soup = BeautifulSoup(response.text, "html.parser")

responsive_div = soup.find("div", class_="responsive-table")
table = responsive_div.find("table", class_="items")

# Extrair os dados da tabela
rows = table.find_all("tr")
for row in rows[1:]:
    cols = row.find_all(["td", "th"])  # pega tanto cabeçalhos quanto dados
    cols = [col.get_text(strip=True) for col in cols]

     # Só exibe se houver mais de 2 colunas preenchidas
    if len(cols) > 2:
        del cols[2]  # remove o nome+possicao
        del cols[1]  # remove vazio
        # print(cols)

        jogador = {
            "numero":cols[0],
            "nome":cols[1],
            "posição":cols[2],
            "nascimento":cols[3],
            "nascido":cols[4],
            "salario":cols[5].replace('k','.000').replace('m','.000.000').replace('€','')
        }

        print(jogador)