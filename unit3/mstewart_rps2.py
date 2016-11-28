r = "Rock"
p = "Paper"
s = "Scissors"
import random
player_wins = 0
comp_wins = 0
ties = 0
round_num = 0
p1_move = "1"
rounds = "1"
comp_move = random.choice([r,p,s])

def get_rounds(rounds):
    rounds = int(input("How many rounds do you want to play from 1 to 9: "))
# def get_p1_move(p1_move):
#     # round_num = round_num + 1
#     # print("Round {}".format(round_num))
#     p1_move = input("Enter your move from [r|p|s]: ")
#     if p1_move == "r":
#         print("You picked: Rock")
#     elif p1_move == "p":
#         print("You picked: Paper")
#     elif p1_move == "s":
#         print("You picked: Scissors")
# def get_comp_move(comp_move):
#     print("Computer picked: {}".format(comp_move))
def get_round_winner(p1_move,comp_move,player_wins,comp_wins,ties):
    p1_move = input("Enter your move from [r|p|s]: ")
    comp_move = random.choice([r,p,s])
    if p1_move == "r" and comp_move == p:
        print("You picked: Rock")
        print("Computer picked : Paper")
        print("Computer Won!")
        comp_wins = comp_wins + 1
    elif p1_move == "p" and comp_move == p:
        print("You picked: Paper")
        print("Computer picked : Paper")
        print("Tie!")
        ties = ties + 1
    elif p1_move == "s" and comp_move == p:
        print("You picked: Scissors")
        print("Computer picked: Paper")
        print("Player Won!")
        player_wins = player_wins + 1
    elif p1_move == "r" and comp_move == r:
        print("You picked: Rock")
        print("Computer picked: Rock")
        print("Tie!")
        ties = ties + 1
    elif p1_move == "p" and comp_move == r:
        print("You picked: Paper")
        print("Computer picked: Rock")
        print("Player Won!")
        player_wins = player_wins + 1
    elif comp_move == "s" and comp_move == r:
        print("You picked: Scissors")
        print("Computer picked: Rock")
        print("Computer Won!")
        comp_wins = comp_wins + 1
    elif p1_move == "r" and comp_move == s:
        print("You picked: Rock")
        print("Computer picked: Scissors")
        print("Player Won!")
        player_wins = player_wins + 1
    elif p1_move == "p" and comp_move == s:
        print("You picked: Paper")
        print("Computer picked: Scissors")
        print("Computer Wins!")
        comp_wins = comp_wins + 1
    elif p1_move == "s" and comp_move == s:
        print("You picked: Scissors")
        print("Computer picked: Scissors")
        print("Tie!")
        ties = ties + 1
    # if p1_move == "r" and comp_move == r:
    #     print("You picked: Rock")
    #     ties = ties + 1
    #     print("Tie")
    # elif p1_move == "p" and comp_move == r:
    #     print("You picked: Paper")
    #     player_wins = player_wins + 1
    #     print("Player Won")
    # elif p1_move == "s" and comp_move == r:
    #     print("You picked: Scissors")
    #     comp_wins = comp_wins + 1
    #     print("Computer Won")
    # elif p1_move == "r" and comp_move == p:
    #     print("You picked: Rock")
    #     comp_wins = comp_wins + 1
    #     print("Computer Won")
    # elif p1_move == "p" and comp_move == p:
    #     print("You picked: Paper")
    #     ties = ties + 1
    #     print("Tie")
    # elif p1_move == "s" and comp_move == p:
    #     print("You picked: Scissors")
    #     player_wins = player_wins + 1
    #     print("Player Won")
    # elif p1_move == "r" and comp_move == s:
    #     print("You picked: Rock")
    #     player_wins = player_wins + 1
    #     print("Player Won")
    # elif p1_move == "p" and comp_move == s:
    #     print("You picked: Paper")
    #     comp_wins = comp_wins + 1
    #     print("Computer Won")
    # elif p1_move == "s" and comp_move == s:
    #     print("You picked: Scissors")
    #     ties = ties + 1
    #     print("Tie")
def print_score(player_wins,comp_wins,ties):
    print("Player Wins: {}".format(player_wins))
    print("Computer Wins: {}".format(comp_wins))
    print("Ties: {}".format(ties))
def rps(p1_move,comp_move,player_wins,comp_wins,ties,rounds):
    rounds = get_rounds(rounds)
    for rounds in range(rounds):
        # get_p1_move(p1_move)
        # get_comp_move(comp_move)
        get_round_winner(p1_move,comp_move,player_wins,comp_wins,ties)
        print_score(player_wins,comp_wins,ties)

rps(p1_move,comp_move,player_wins,comp_wins,ties,rounds)