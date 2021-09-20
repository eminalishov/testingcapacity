import requests
from bs4 import BeautifulSoup


class ClinicList:
    def __init__(self):
        self.url = 'https://testovani.uzis.cz/'
        self.content = requests.get(self.url).text

    def data(self):
        soup = BeautifulSoup(self.content, features="html.parser")
        list__result = soup.find_all('div', attrs={'class': 'list__result'})
        l = []
        for res in list__result:
            url = self.url+res.find('a', attrs={'class': 'list__link'}).get('href').strip()
            name = res.find('span', attrs={'class': 'list__col'}).text.strip()
            l.append({
                'name': name,
                'url': url,
            })
        return l
