import random
# rules of the game............
print("Welcome to a game of rock, paper, scissors. \n" +
      "How to win: \n" + "Rock vs Paper: Paper wins. \n" + "Rock vs Scissors: Rock wins. \n" + "Paper vs Scissors: Scissors wins. \n")
while True:
    options = ["rock", "paper", "scissors"]

    computer = random.choice(options)
    player = None

    while player not in options:
        player = input("rock, paper, or scissors? ").lower()
    # conditions for the game........
    if player == computer:
        print("computer", "(" + computer + ")",
              ":", "player", "(" + player + ")")
        print("draw, same guess")
    elif player == "rock":
        if computer == "paper":
            print("computer", "(" + computer + ")",
                  ":", "player", "(" + player + ")")
            print("you win! paper covers rock... ")
    elif player == "paper":
        if computer == "scissors":
            print("computer", "(" + computer + ")",
                  ":", "player", "(" + player + ")")
            print("you lose! scissors cuts paper... ")
    elif player == "scissors":
        if computer == "paper":
            print("computer", "(" + computer + ")",
                  ":", "player", "(" + player + ")")
            print("you win! scissors cuts paper... ")
    # condition to play again..........
    play_again = input("Would you like to play again? (yes/no): ").lower()
    if play_again != "yes":
        break
print("See you soon, bye...")
