import random


class Cards:
    def __init__(self, suit, val):
        self.suit = suit
        self.val = val
    
    def show(self):
        print('{} {}'.format(self.val, self.suit))
    
    
class Deck(Cards):
    def __init__(self):
        self.cards = []
        self.create()
    
    def create(self):
        for suit in ['Червы', 'Бубны', 'Трефы', 'Пики']:
            for value in [str(n) for n in range(2, 11)] + list('JQKA'):
                self.cards.append(Cards(suit, value))
    


    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]
    print('Перетасока')

    def deal(self):
        return self.cards.pop()
    
    def _count(self):
        length = len(self.cards)
        print(f'Осталось {length} карт')        

deck = Deck()
deck.shuffle()
card = deck.deal()
card.show()
deck._count()
