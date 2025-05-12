# Terminal Card Game — Python Edition

This is a simple terminal-based card game built with Python. 
The game allows one human player to compete against the computer in a series of rounds, 
drawing cards from a shuffled deck and scoring points based on who draws the higher card.

## Game Summary

- Two players: You vs. the Computer
- A standard 52-card deck is used
- Each round, both players draw one card
- The player with the higher card wins the round and earns a point
- The game ends when all cards have been drawn
- Final scores are shown and a winner is declared (or a draw if tied)

## How to Run the Game

1. make sure u have Python 3.x installed on your computer

2. #Steps to Run#:
   - Download all files: `main.py`, `deck.py`, and `4_17_25.py`
   - Open your terminal and navigate to the folder containing the files
   - Run the game by typing:

     ```bash
     python main.py
     ```

     or, if you're on macOS/Linux and `python3` is required:

     ```bash
     python3 main.py
     ```

# File Descriptions

- `main.py`: The main game script — handles user input, gameplay loop, and scoring.
- `deck.py`: Contains the `Deck` and `Card` classes, managing the creation and shuffling of the card deck.
- `4_17_25.py`: Handles auxiliary functions, such as sorting or comparing cards, or may contain player logic (based on your setup).

# No External Libraries Needed

This game is built using only standard Python libraries. You don't need to install anything extra.



