#importações utilizadas /bibilhoteca
from bs4 import BeautifulSoup
import requests
from csv import writer
#site usado para realizaar busca 
url= "https://www.zapimoveis.com.br/aluguel/apartamentos/mg+belo-horizonte/?transacao=Aluguel&tipoUnidade=Residencial,Apartamento&tipo=Imóvel%20usado&pagina=1&onde=,Minas%20Gerais,Belo%20Horizonte,,,,,city,BR>Minas%20Gerais>NULL>Belo%20Horizonte,-19.919052,-43.938669,"
headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0'}
page = requests.get(url,headers=headers)
#class contendo informações que serão recolhidas
soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all('div', class_="simple-card__box")
#responsevel por criar e escrever no aquivo csv
with open('aps.csv', 'a', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['QUARTOS','LOCALIZAÇÃO','PREÇO','BANHEIROS']
    thewriter.writerow(header)

    for list in lists:
        QUARTOS = list.find('span', itemprop="numberOfRooms").text.replace('\n', '')
        LOCALIZAÇÃO = list.find('h2', class_="simple-card__address color-dark text-regular").text.replace('\n', '')
        PREÇO = list.find('div', class_="simple-card__prices simple-card__listing-prices").text.replace('\n', '')
        AREA = list.find('span', itemprop="floorSize").text.replace('\n', '')
        BANHEIROS = list.find('span', itemprop="numberOfBathroomsTotal").text.replace('\n', '')
        
        
        
        info = [QUARTOS,LOCALIZAÇÃO,PREÇO,BANHEIROS]
        thewriter.writerow(info)

