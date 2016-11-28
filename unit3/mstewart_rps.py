r = "Rock"
p = "Paper"
s = "Scissors"
import random
player_wins = 0
comp_wins = 0
ties = 0
round_num = 0
rounds = int(input("How many rounds do you want to play from 1 to 9: "))
for rounds in range(rounds):
    round_num = round_num + 1
    print("Round {}".format(round_num))
    p1_move = input("Enter your move from [r|p|s]: ")
    comp_move = random.choice([r,p,s])
    if p1_move == "r" and comp_move == p:
        print("You picked: Rock")
        print("Computer picked : Paper")
        print("Computer Won!")
        print("")
        comp_wins = comp_wins + 1
    elif p1_move == "p" and comp_move == p:
        print("You picked: Paper")
        print("Computer picked : Paper")
        print("Tie!")
        print("")
        ties = ties + 1
    elif p1_move == "s" and comp_move == p:
        print("You picked: Scissors")
        print("Computer picked: Paper")
        print("Player Won!")
        print("")
        player_wins = player_wins + 1
    elif p1_move == "r" and comp_move == r:
        print("You picked: Rock")
        print("Computer picked: Rock")
        print("Tie!")
        print("")
        ties = ties + 1
    elif p1_move == "p" and comp_move == r:
        print("You picked: Paper")
        print("Computer picked: Rock")
        print("Player Won!")
        print("")
        player_wins = player_wins + 1
    elif p1_move == "s" and comp_move == r:
        print("You picked: Scissors")
        print("Computer picked: Rock")
        print("Computer Won!")
        print("")
        comp_wins = comp_wins + 1
    elif p1_move == "r" and comp_move == s:
        print("You picked: Rock")
        print("Computer picked: Scissors")
        print("Player Won!")
        print("")
        player_wins = player_wins + 1
    elif p1_move == "p" and comp_move == s:
        print("You picked: Paper")
        print("Computer picked: Scissors")
        print("Computer Wins!")
        print("")
        comp_wins = comp_wins + 1
    elif p1_move == "s" and comp_move == s:
        print("You picked: Scissors")
        print("Computer picked: Scissors")
        print("Tie!")
        print("")
        ties = ties + 1
    elif p1_move != "r" or p1_move != "p" or p1_move != "s":
        print("Something went wrong, please start over.")
print("")
print("")
print("Player Wins: {}".format(player_wins))
print("Computer Wins: {}".format(comp_wins))
print("Ties: {}".format(ties))