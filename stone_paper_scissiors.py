import  random
options = ("rock" , "paper" ,"scissors")

playing = True
while playing:
    player = None
    computer = random.choice(options)
    while player not in options:
        player  = input("Enter a choice (rock,paper,scissors): ")

    print(f"player: {player}")
    print(f"computer : {computer}")

    if player == computer:
        print("It's a Tie 🤝")
    elif player == "rock" and computer == "scissors":
        print("You win! 🏆")
    elif player == "paper" and computer =="rock":
        print("🎆You win 🏆")
    elif player =="scissors" and computer=="paper":
        print("You win 🏆")

    else:
        print("You Lose!👎")

    if  input("Play again? (y/n): ").lower() !="y":
        playing =False
print("Thanks for playing !")
