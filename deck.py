#Consolidation project 
#Deck 

import random 

def create_deck():
    values = ['A'] + [str(i) for i in range(2, 11)] + ['J', 'Q']
    suits = ['hearts', 'diamonds', 'clubs', 'spades']
    deck = [{"value": value, "suit": suit} for suit in suits for value in values]
    random.shuffle(deck)
    return deck
 
def draw_cards(deck, number):
    cards_drawn = deck[:number]
    del deck[:number]
    return cards_drawn
