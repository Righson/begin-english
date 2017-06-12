from app.card import CardThread


class CardManager:
    def __init__(self):
        self.cards = []

        for ii in range(3):
            self.cards.append(CardThread())
            self.cards[ii].start()
            self.cards[ii].join()

    def get_one(self):
        self.cards[2].join()
        res = (self.cards[0].string, self.cards[0].params)
        self.cards = self.cards[1:]
        self.cards.append(CardThread())
        self.cards[2].start()
        return res
