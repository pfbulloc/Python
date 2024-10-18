# Rock Paper Scissors Game
#EL E 237
#Assignment 4
#Patton Bullock

def display_instructions():
    print("Welcome to Rock Paper Scissors")
    print("Instructions:")
    print("Player 1 and Player 2 will each select 'rock', 'paper', or 'scissors'.")
    print("The game will continue until one player wins 3 rounds.")
    print("Rock beats Scissors, Scissors beats Paper, and Paper beats Rock.")
    print()

def get_choice(player):
    choices = ['rock', 'paper', 'scissors']
    while True:
        choice = input(f"{player}, please enter your choice (rock/paper/scissors): ").lower()
        if choice in choices:
            return choice
        else:
            print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")

def determine_winner(choice1, choice2):
    if choice1 == choice2:
        return "draw"
    elif (choice1 == 'rock' and choice2 == 'scissors') or \
         (choice1 == 'scissors' and choice2 == 'paper') or \
         (choice1 == 'paper' and choice2 == 'rock'):
        return "player1"
    else:
        return "player2"

def main():
    display_instructions()

    player1_wins = 0
    player2_wins = 0
    moves_history = []  # List to store moves history

    # Game continues until one player wins 3 rounds
    while player1_wins < 3 and player2_wins < 3:
        # Get choices from both players
        player1_choice = get_choice("Player 1")
        player2_choice = get_choice("Player 2")

        # Records the choices
        moves_history.append((player1_choice, player2_choice))

        # Determines the winner of the round
        winner = determine_winner(player1_choice, player2_choice)

        if winner == "player1":
            print("Player 1 wins this round!")
            player1_wins += 1
        elif winner == "player2":
            print("Player 2 wins this round!")
            player2_wins += 1
        else:
            print("It's a draw, no points awarded.")

        print(f"Current score - Player 1: {player1_wins}, Player 2: {player2_wins}")
        print()

    # Congratulates the winner
    if player1_wins == 3:
        print("Player 1 Has won the game")
    else:
        print("Player 2 Has won the game")

    # Displays the summary of moves
    print("\nGame Summary:")
    for round_num, (p1_move, p2_move) in enumerate(moves_history, start=1):
        print(f"Round {round_num}: Player 1 chose {p1_move}, Player 2 chose {p2_move}")

if __name__ == "__main__":
    main()
