import requests
from bs4 import BeautifulSoup


class CalendarByDate:

    def __init__(self, url):
        self.url = url
        self.content = requests.get(self.url).text

    def get_info(self):
        soup = BeautifulSoup(self.content,features="html.parser")
        table = soup.find('div', attrs={'class': 'info'})
        table_body = table.find('table')
        rows = table_body.find_all('tr')
        data = []
        for row in rows:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            data.append(cols)
        dict = {}
        for datum in data:
            dict[datum[0]] = datum[1]
        return dict
    def get_calendar(self):
        soup = BeautifulSoup(self.content, features="html.parser")
        table = soup.find('div', attrs={'class': 'slots__list'})
        tops = table.find_all('div',attrs={'class': 'slots__top'})
        toplist = []
        for top in tops:
            p0 = top.find_all('p')[0].text
            p1 = top.find_all('p')[1].text
            toplist.append('{} {}'.format(p0,p1))
        bottoms = table.find_all('div', attrs={'class': 'slots__bottom'})
        bottomlist = []
        for bottom in bottoms:
            p = bottom.find('p').text
            bottomlist.append(p)
            dict = {}
        for x in list(zip(toplist,bottomlist)):
            dict[x[0]] = x[1]
        return dict
