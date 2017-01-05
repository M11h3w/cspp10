import random
player_bank = 100
casino_bank = 1000
print("OVER UNDER 7")
print("")
print("")
print("You have ${}".format(player_bank))
while player_bank > 0 and casino_bank > 0:
    money_bet = int(input("Enter a whole number for your bet: "))
    range_bet = input("Enter your guess for the dice roll, either below, above, or 7: ")
    if money_bet > player_bank:
        print("You don't have that much money!")
        print("")
    elif money_bet < 0:
        print("You can't bet a negative number!")
        print("")
    elif money_bet == 0:
        print("You didn't bet anything.")
        print("")
    elif money_bet > 0 and money_bet <= player_bank:
        print("")
        dice1 = random.choice([1,2,3,4,5,6])
        dice2 = random.choice([1,2,3,4,5,6])
        dice_total = dice1 + dice2
        print("The dice is thrown: {} total".format(dice_total))
        print("")
        if dice_total > 7:
            if range_bet == "above":
                player_bank = player_bank - money_bet
                money_bet = money_bet * 2
                player_bank = player_bank + money_bet
                print("Your guess was correct. You won the round!")
                print("You have ${}.".format(player_bank))
                print("")
            elif range_bet == "7" or range_bet == "below":
                casino_bank = casino_bank + money_bet
                player_bank = player_bank - money_bet
                print("Your guess was incorrect. You lose the round!")
                print("You have ${}.".format(player_bank))
                print("")
        elif dice_total == 7:
            if range_bet == "7":
                player_bank = player_bank - money_bet
                money_bet = money_bet * 4
                player_bank = player_bank + money_bet
                print("Your guess was correct. You won the round!")
                print("You have ${}.".format(player_bank))
                print("")
            elif range_bet == "above"  or range_bet == "below":
                casino_bank = casino_bank + money_bet
                player_bank = player_bank - money_bet
                print("Your guess was incorrect. You lose the round!")
                print("You have ${}.".format(player_bank))
                print("")
        elif dice_total < 7:
            if range_bet == "below":
                player_bank = player_bank - money_bet
                money_bet = money_bet * 2
                player_bank = player_bank + money_bet
                print("Your guess was correct. You won the round!")
                print("You have ${}.".format(player_bank))
                print("")
            elif range_bet == "above" or range_bet == "7":
                casino_bank = casino_bank + money_bet
                player_bank = player_bank - money_bet
                print("Your guess was incorrect. You lose the round!")
                print("You have ${}.".format(player_bank))
                print("")
    elif casino_bank == 0:
        print("")
        print("You beat the casino. You have ${}".format(player_bank))
        break
    elif player_bank == 0:
        print("")
        print("You have $0. You Lose!")
        break