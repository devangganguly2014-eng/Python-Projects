# snake_water_gun.py
# Simple Snake-Water-Gun game (like Rock-Paper-Scissors)
# Rules:
#   Snake (s) drinks Water (w) -> Snake wins
#   Water (w) douses Gun (g) -> Water wins
#   Gun (g) kills Snake (s) -> Gun wins

import random
import sys
import time

CHOICES = {'s': 'Snake', 'w': 'Water', 'g': 'Gun'}

def decide_winner(player, computer):
    # returns "player", "computer", or "draw"
    if player == computer:
        return "draw"
    # win combos for player
    if (player == 's' and computer == 'w') or \
       (player == 'w' and computer == 'g') or \
       (player == 'g' and computer == 's'):
        return "player"
    return "computer"

def get_player_choice():
    while True:
        choice = input("Choose [s]nake, [w]ater, [g]un (or q to quit): ").strip().lower()
        if choice == 'q':
            return 'q'
        if choice in CHOICES:
            return choice
        print("Invalid input — please type s, w, g or q.")

def main():
    print("Welcome to Snake-Water-Gun! (Best of N rounds or custom rounds)")
    # ask for number of rounds
    while True:
        rounds_input = input("Kitne rounds khelenge? (default 5) — press Enter for 5: ").strip()
        if rounds_input == "":
            total_rounds = 5
            break
        if rounds_input.isdigit() and int(rounds_input) > 0:
            total_rounds = int(rounds_input)
            break
        print("Please enter a positive integer or press Enter for default.")
    
    player_score = 0
    comp_score = 0
    draws = 0

    for round_no in range(1, total_rounds + 1):
        print(f"\nRound {round_no} / {total_rounds}")
        player = get_player_choice()
        if player == 'q':
            print("Quitting game early. Bye!")
            break
        comp = random.choice(list(CHOICES.keys()))
        print(f"You chose: {CHOICES[player]}")
        # slight delay for nicer feel
        time.sleep(0.3)
        print(f"Computer chose: {CHOICES[comp]}")
        
        result = decide_winner(player, comp)
        if result == "draw":
            draws += 1
            print("Result: It's a draw!")
        elif result == "player":
            player_score += 1
            print("Result: You WIN this round! 🎉")
        else:
            comp_score += 1
            print("Result: Computer wins this round.")
        
        print(f"Score -> You: {player_score} | Computer: {comp_score} | Draws: {draws}")

    # final summary
    print("\n=== Final Summary ===")
    print(f"Rounds played: { (round_no if player != 'q' else round_no-1) if 'round_no' in locals() else 0 }")
    print(f"You: {player_score}  Computer: {comp_score}  Draws: {draws}")
    if player_score > comp_score:
        print("Overall: Congratulations! You won the game! 🏆")
    elif player_score < comp_score:
        print("Overall: Computer won the game. Better luck next time!")
    else:
        print("Overall: It's a tie overall.")
    print("Thanks for playing!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nGame interrupted. Bye!")
        sys.exit(0)
