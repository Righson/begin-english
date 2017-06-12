import unittest
from app.cardmanager import CardManager


class CommandTest(unittest.TestCase):
    def test_createCardManagerAndGetFirstLine(self):
        c = CardManager()
        self.assertIsInstance(c.get_one(), tuple)
        self.assertEqual(len(c.cards), 3)

if __name__ == '__main__':
    unittest.main()
