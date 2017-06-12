from app.cardmanager import CardManager
from app.data import Data


class CommandLineListener:

    viewed = 0

    def __init__(self):
        self.card_manger = CardManager()
        self.database = Data()

    def question(self, in_question, in_answer, in_callback):
        response = input(in_question)
        if response.upper() == in_answer:
            in_callback()
        else:
            return False

    def listen(self):
        self.viewed += 1
        string, data = self.card_manger.get_one()
        # вывести на экран
        print("Просмотрено %s карточек" % self.viewed)
        print(string)
        # добавить в базу данных новую карточку
        self.database.new({'eng': data['eng'], 'rus': data['rus']}, data['decr'])
        self.question('Next Card (y/n): ', 'Y', self.listen)
