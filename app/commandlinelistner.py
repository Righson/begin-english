from app.cardmanager import CardManager


class CommandLineListener:

    viewed = 0

    def __init__(self):
        self.card_manger = CardManager()

    def listen(self):
        self.viewed += 1
        print("Просмотрено %s карточек" % self.viewed)
        print(self.card_manger.get_one())
        response = input('Next Card (y/n): ')
        if response == 'y' or response == 'Y':
            self.listen()
        else:
            return False
