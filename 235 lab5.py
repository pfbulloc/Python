# Rock Paper Scissors
# EL E 237 Assignment 5
# Patton Bullock

def intro():
    print("Welcome to the Rock-Paper-Scissors game!")
    print("Instructions:")
    print("Player 1 and Player 2 will each select 'rock', 'paper', or 'scissors'.")
    print("The game will continue until one player wins 3 rounds.")
    print("Rock beats Scissors, Scissors beats Paper, and Paper beats Rock.")
    print()


def choice(player):
    choices = ['rock', 'paper', 'scissors']
    while True:
        choice = input(f"{player}, please enter your choice (rock/paper/scissors): ").lower()
        if choice in choices:
            return choice
        else:
            print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")

def win(choice1,choice2):
    if choice1 == choice2:
        return "draw"
    elif (choice1 == 'rock' and choice2 == 'scissors') or \
         (choice1 == 'scissors' and choice2 == 'paper') or \
         (choice1 == 'paper' and choice2 == 'rock'):
        return "player1"
    else:
        return "player2"

def main():
    intro()

    p1wins = 0
    p2wins = 0
    history = []  # list of move history

    
    while p1wins < 3 and p2wins < 3: # keeps the game going until either p1 or p2 has 3 wins
        p1choice = choice("Player 1")
        p2choice = choice("Player 2")

        
        history.append((p1choice, p2choice)) #stores the choices of the players

        
        winner = win(p1choice, p2choice) #determines the round winner

        if winner == "player1":
            print("Player 1 wins this round!")
            p1wins += 1
        elif winner == "player2":
            print("Player 2 wins this round!")
            p2wins += 1
        else:
            print("It's a draw! No points awarded.")

        print(f"Current score - Player 1: {p1wins}, Player 2: {p2wins}")
        print()


    if p1wins == 3:
        print("Congratulations, Player 1! You won the game!")
    else:
        print("Congratulations, Player 2! You won the game!")

   
    print("\nGame Summary:") #shows the number of moves and what choice was picked for each player
    for round_num, (p1move, p2move) in enumerate(history, start=1):
        print(f"Round {round_num}: Player 1 chose {p1move}, Player 2 chose {p2move}")

if __name__ == "__main__":
    main()


