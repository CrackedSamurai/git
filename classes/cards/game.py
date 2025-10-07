import cards_pack

game_deck = cards_pack.deck()
hand_1 = cards_pack.deck()
hand_2 = cards_pack.deck()

game_deck.shuffle()
game_deck.deal(7, [hand_1, hand_2])
game_deck.show()
hand_1.show()
hand_2.show()