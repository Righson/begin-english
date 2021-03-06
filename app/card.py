from threading import Thread
from bs4 import BeautifulSoup as Soup
import urllib.request


class CardThread(Thread):

    url = 'http://begin-english.ru/word-rand'

    def __init__(self):
        self.data = None
        Thread.__init__(self)

    def run(self):
        data = Soup(urllib.request.urlopen(self.url).read(), 'html.parser').find('div', {'class': 'word'})
        self.data = {'word': str(data.find('div').text).upper(), 'description': CardThread.make_description(data.findAll('div')[2])}

    @staticmethod
    def make_description(in_obj):

        string = ''

        for el in in_obj:
            if el.name == 'h2':
                string += "\n%s\n" % el.string.upper()
            elif el.name is not None:
                string += "%s\n" % el.text

        return string

    @property
    def string(self):

        string = self.data['word']
        string += '\n'+'_'*10 + '\n\n'
        string += self.data['description']

        return string

    @property
    def params(self):
        eng, rus = map(lambda s: s.strip(), self.data['word'].split('—'))

        return {'eng': eng, 'rus': rus, 'decr': self.data['description']}
