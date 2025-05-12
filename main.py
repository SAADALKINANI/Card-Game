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

# === Game Loop ===
round_number = 1
max_rounds = 16

while round_number <= max_rounds:
    print(f"\n====== Round {round_number} ======")
    print(f"{leader} will lead this round.")

    # Player moves
    if leader == "Player 1":
        p1_card = play_card(player1_hand)
        print(f"Player 1 plays: {p1_card['value']} of {p1_card['suit']}")
        p2_card = play_card(player2_hand, lead_suit=p1_card["suit"])
        print(f"Player 2 plays: {p2_card['value']} of {p2_card['suit']}")
        lead_suit = p1_card["suit"]
    else:
        p2_card = play_card(player2_hand)
        print(f"Player 2 plays: {p2_card['value']} of {p2_card['suit']}")
        p1_card = play_card(player1_hand, lead_suit=p2_card["suit"])
        print(f"Player 1 plays: {p1_card['value']} of {p1_card['suit']}")
        lead_suit = p2_card["suit"]

    # Decide winner
    if p1_card["suit"] == lead_suit and p2_card["suit"] != lead_suit:
        player1_score += 1
        leader = "Player 1"
        winner = "Player 1"
    elif p2_card["suit"] == lead_suit and p1_card["suit"] != lead_suit:
        player2_score += 1
        leader = "Player 2"
        winner = "Player 2"
    else:
        if get_card_value(p1_card) > get_card_value(p2_card):
            player1_score += 1
            leader = "Player 1"
            winner = "Player 1"
        else:
            player2_score += 1
            leader = "Player 2"
            winner = "Player 2"

    print(f"{winner} wins this round!")
    print(f"Score: Player 1 = {player1_score} | Player 2 = {player2_score}")

    # Reveal a card from deck
    if len(game_deck) > 0:
        revealed = deck.draw_cards(game_deck, 1)[0]
        print(f"Revealed card from deck: {revealed['value']} of {revealed['suit']}")

    # Check for mid-game re-deal
    if len(player1_hand) == 4 and len(player2_hand) == 4 and len(game_deck) >= 8:
        print("\nRe-dealing 4 cards to each player...")
        player1_hand += deck.draw_cards(game_deck, 4)
        player2_hand += deck.draw_cards(game_deck, 4)

    # Early game end check
    if (player1_score >= 9 and player2_score > 0) or (player2_score >= 9 and player1_score > 0):
        print("\nGame ends early — someone reached 9 and the other can't catch up.")
        break

    round_number += 1

# === End of Game Summary ===
print("\n====== Game Over ======")
if player1_score == 0:
    print("Player 1 shot the moon! Final score: Player 1 = 17 | Player 2 = 0")
elif player2_score == 0:
    print("Player 2 shot the moon! Final score: Player 1 = 0 | Player 2 = 17")
elif player1_score > player2_score:
    print(f"Player 1 wins! Final score: {player1_score} to {player2_score}")
elif player2_score > player1_score:
    print(f"Player 2 wins! Final score: {player2_score} to {player1_score}")
else:
    print("It’s a tie!")
