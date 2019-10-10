import requests
from bs4 import BeautifulSoup as bs

headers = {'accept':'*/*',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
base_url = 'https://www.gipernn.ru/dom/gorod-nizhniY-novgorod?per-page=100&page=1'

def hh_parse(base_url, headers):
    real_estate = []
    session = requests.session()
    requset = session.get(base_url, headers=headers, verify=False)
    if requset.status_code == 200:
        soup = bs(requset.content, 'html.parser')
        divs = soup.find_all('tr')
        for div in divs:
# district - район
            if div.span == None:
                pass
            else:
                district = div.span.text
                print(district)
# addres - адрес
            if div.td == None:
                pass
            else:
                if div.td.next.next.next.text == "":
                    pass
                else:
                    addres = div.td.next.next.next.a.text
                    print(addres)
# material - материал стен
            if div.td == None:
                pass
            else:
                if div.td.next.next.next.text == "":
                    pass
                else:
                    material = div.td.next.next.next.next.next.next.next.next.next.text
                    print(material)
# flors_number - этажность
            if div.td == None:
                pass
            else:
                if div.td.next.next.next.text == "":
                    pass
                else:
                    flors_number = div.td.next.next.next.next.next.next.next.next.next.next.next.text
                    #print(flors_number)
# year_buid - год постройки
            if div.td == None:
                pass
            else:
                if div.td.next.next.next.text == "":
                    pass
                else:
                    year_buid = div.span.next.next.next.next.next.next.text
                    #print(year_buid)
# appartment_number - количество квартир
            if div.td == None:
                pass
            else:
                if div.td.next.next.next.text == "":
                    pass
                else:
                    appartment_number = div.span.next.next.next.next.next.next.next.next.text
                    #print(appartment_number)
# mean_price_sqr_m - средняя цена за кв. метр
            if div.td == None:
                pass
            else:
                if div.td.next.next.next.text == "":
                    pass
                else:
                    mean_price_sqr_m = div.span.next.next.next.next.next.next.next.next.next.next.next.next.text
                    mean_price_sqr_m = "".join(mean_price_sqr_m.split())
                    #print(mean_price_sqr_m)

        print(len(real_estate))
    else:
        print('ERRRRoR')

hh_parse(base_url, headers)
