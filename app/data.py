import pymongo
import random
# формат колекции базы данных
# word
#   eng - слово на английском
#   rus - слово на русском
# description - описание


class Data(object):

    def __init__(self):
        self._collection = pymongo.MongoClient('localhost', 27017)['cards']['words']

    def new(self, in_word, in_description):
        # найти слово в колекции
        if self._collection.find({"word.eng": in_word['eng'].upper()}).count() == 0:
            # добавить новую запись в колекцию
            if isinstance(in_description, str) \
                    and isinstance(in_word, dict) \
                    and all(keys in in_word for keys in ('eng', 'rus')):
                return self._collection.insert_one(
                    {
                        'word': in_word,
                        'description': in_description
                    }
                )
            else:
                return None
        else:
            # если такое слово есть вернуть False
            return False

    def get_random_card(self):
        return self._collection.find()[random.randint(0, self._collection.count())]
