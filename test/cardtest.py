import unittest
from app.card import CardThread


class TestStringMethods(unittest.TestCase):
    def test_openSite(self):
        c = CardThread()
        self.assertIsNone(c.data)

    def test_getRandomDataFromSite(self):
        threads = []
        for ii in range(3):
            threads.append(CardThread())
            threads[ii].start()
            threads[ii].join()

        self.assertNotEqual(threads[0].data['word'], threads[1].data['word'])
        self.assertNotEqual(threads[1].data['word'], threads[2].data['word'])
        self.assertNotEqual(threads[2].data['word'], threads[0].data['word'])

        self.assertIsNotNone(threads[0].data['word'])
        self.assertIsNotNone(threads[1].data['word'])
        self.assertIsNotNone(threads[2].data['word'])

if __name__ == '__main__':
    unittest.main()
