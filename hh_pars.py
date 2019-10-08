import requests
from bs4 import BeautifulSoup as bs

headers = {'accept':'*/*',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
base_url = 'https://www.gipernn.ru/dom/gorod-nizhniY-novgorod?page=1'

def hh_parse(base_url, headers):
    session = requests.session()
    requset = session.get(base_url, headers=headers)
    if requset.status_code == 200:
        soup = bs(requset.content, 'html.parser')
        divs = soup.find_all('tr')
        for div in divs:
            addres = div.text
            print(addres)
    else:
        print('ERRRRoR')

hh_parse(base_url, headers)