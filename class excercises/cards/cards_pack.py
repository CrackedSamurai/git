import random

ranks = [str(i) for i in range(2, 11)] + ['Jack', 'Queen', 'King', 'Ace']
colors = ['heart','dimond','clubs', 'spades']

class card:
    def __init__(self, rank, color):
        self.__set_color(color)
        self.__set_rank(rank)
    def __set_color(self, color):
        colors = ['heart','dimond','clubs', 'spades']
        self.color = color
        self.__is_color(colors)
    def __set_rank(self, rank):
        ranks = [str(i) for i in range(2, 11)] + ['Jack', 'Queen', 'King', 'Ace']
        self.rank = rank
        self.__is_rank(ranks)
    def __is_color(self, colors):
        if self.color in colors: pass
        else: raise ValueError(f"not a valid color: {self.color}")
    def __is_rank(self, ranks):
        if self.rank in ranks: pass 
        else: raise ValueError(f"not a valid rank: {self.rank}")
    def show(self):
        print(f"{self.rank} of {self.color} ")
    
class deck:
    def __init__(self):
        self.cards = []
    def sort(self):
        self.cards.sort(key=lambda c: (colors.index(c.color), ranks.index(c.rank)))
    def add_card(self, card):
        self.cards.append(card)
    def remove_card(self, rank=None, color=None, index=None):
        if index != None or index<len(self.cards): self.cards.pop(index)
        else:
            for c in self.cards:
                if c.rank==rank and c.color==color: self.cards.remove(c)
                else: pass
    def show(self):
        print("------")
        print("cards:")
        for card in self.cards:
            card.show()
        print("------")
    def shuffle(self):
        random.shuffle(self.cards)
    def push(self, card, pile):
        pile.add_card(self.cards[card])
        self.remove_card(index=card)
    def deal(self, num, hands):
        for _ in range(num):
            for hand in hands:
                self.push(0, hand)
    def create_deck(self, num):
        for _ in range(num):
            for rank in ranks:
                for color in colors:
                    self.add_card(card(rank=rank, color=color))

