import unittest
import pymongo
from app.data import Data
from app.card import CardThread


class TestStringMethods(unittest.TestCase):

    d = Data()
    c = CardThread()

    def test_create_database_connection(self):
        self.assertIsInstance(self.d._collection, pymongo.collection.Collection)

    def test_find_test_string(self):
        self.assertEqual(self.d._collection.find_one({'eng': 'test'})['eng'], 'test')

    def test_new_word(self):

        self.c.start()
        self.c.join()

        d = self.c.params

        self.assertIsNotNone(self.d.new({'eng': d[0], 'rus': d[1]}, d[2]))
        self.assertFalse(self.d.new({'eng': 'MINER', 'rus': 'ШАХТЕР'}, ''))

    def test_ger_random_card(self):
        self.assertIsInstance(self.d.get_random_card(), dict)

if __name__ == '__main__':
    unittest.main()
