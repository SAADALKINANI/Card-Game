# Tricksy Battle - main.py
import deck
import random

# Step 1: Create deck and shuffle
game_deck = deck.create_deck()

# Step 2: Deal 8 cards to each player
player1_hand = deck.draw_cards(game_deck, 8)
player2_hand = deck.draw_cards(game_deck, 8)

# Step 3: Print hands
print("Player 1's Hand:")
for card in player1_hand:
    print(f"{card['value']} of {card['suit']}")

print("\nPlayer 2's Hand:")
for card in player2_hand:
    print(f"{card['value']} of {card['suit']}")

print(f"\nCards left in deck: {len(game_deck)}")

# Step 4: Initialize scores and choose who leads first
player1_score = 0
player2_score = 0
leader = random.choice(["Player 1", "Player 2"])
print(f"\n{leader} will lead the first round.")

# Function to get numeric value of the card
def get_card_value(card):
    if card["value"] == "A":
        return 1
    elif card["value"] == "J":
        return 11
    elif card["value"] == "Q":
        return 12
    else:
        return int(card["value"])

# Function to play a card from hand
def play_card(hand, lead_suit=None):
    valid_cards = [c for c in hand if c["suit"] == lead_suit] if lead_suit else hand
    if not valid_cards:
        valid_cards = hand
    chosen_card = valid_cards[0]
    hand.remove(chosen_card)
    return chosen_card
