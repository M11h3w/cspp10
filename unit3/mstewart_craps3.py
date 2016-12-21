import random
casino_bank = 1000
player_bank = 100
bet = 1
dice_total = 1
point_number = 1
def get_bet(bet):
    bet = int(input("Enter a whole number for your bet: "))
    if bet > player_bank:
        print("You don't have that much money!")
        print("")
    elif bet < 0:
        print("You can't bet a negative number!")
        print("")
    elif bet == 0:
        print("You didn't bet anything.")
        print("")
    return bet
def roll_dice(dice_total):
    print("")
    dice1 = random.choice([1,2,3,4,5,6])
    dice2 = random.choice([1,2,3,4,5,6])
    dice_total = dice1 + dice2
    print("The dice is thrown: {} and {}, {} total".format(dice1, dice2, dice_total))
    return dice_total
def determine_roll(bet, dice_total, point_number):
    if dice_total == 2 or dice_total == 3 or dice_total == 12:
        casino_bank = casino_bank + bet
        player_bank = player_bank - bet
        print("You rolled a {}. You lost the round!".format(dice_total))
        print("You have ${}.".format(player_bank))
        print("")
        return player_bank
    elif dice_total == 7 or dice_total == 11:
        player_bank = player_bank - bet
        bet = bet * 2
        player_bank = player_bank + bet
        print("You rolled a {}. You win the round!".format(dice_total))
        print("You have ${}.".format(player_bank))
        print("")
        return player_bank
    elif dice_total == 4 or dice_total == 5 or dice_total == 6 or dice_total == 8 or dice_total == 9 or dice_total == 10:
        point_number = dice_total
        print("Your point number is {}".format(point_number))
        return point_number
def roll_again(bet, dice_total, point_number):
    enter = input("Press enter to continue")
    print("")
    if enter == "":
        dice1 = random.choice([1,2,3,4,5,6])
        dice2 = random.choice([1,2,3,4,5,6])
        dice_total = dice1 + dice2
        print("The dice is thrown: {} and {}, {} total".format(dice1, dice2, dice_total))
        if dice_total == 7:
            dice_total == 7
            casino_bank = casino_bank + bet
            player_bank = player_bank - bet
            print("You rolled a 7. You lost the round!") 
            print("You have ${}.".format(player_bank))
            print("")
            return player_bank
        elif dice_total == point_number:
            dice_total == point_number
            player_bank = player_bank - bet
            bet = bet * 2
            player_bank = player_bank + bet
            print("You rolled your point number! You win the round!")
            print("You have ${}.".format(player_bank))
            print("")
            return player_bank
        else:
            while dice_total != 7 or dice_total != point_number:
                print("No 7 or {}. Reroll!".format(point_number))
                enter = input("Press enter to continue")
                print("")
                if enter == "":
                    dice1 = random.choice([1,2,3,4,5,6])
                    dice2 = random.choice([1,2,3,4,5,6])
                    dice_total = dice1 + dice2
                    print("The dice is thrown: {} and {}, {} total".format(dice1, dice2, dice_total))
                    if dice_total == 7:
                        casino_bank = casino_bank + bet
                        player_bank = player_bank - bet
                        print("You rolled a 7. You lost the round!")
                        print("You have ${}.".format(player_bank))
                        print("")
                        return player_bank
                    elif dice_total == point_number:
                        player_bank = player_bank - bet
                        bet = bet * 2
                        player_bank = player_bank + bet
                        print("You rolled your point number! You win the round!")
                        print("You have ${}.".format(player_bank))
                        print("")
                        return player_bank
def craps(bet, dice_total, point_number):
    get_bet(bet)
    roll_dice(dice_total)
    determine_roll(bet, dice_total, point_number)
    roll_again(bet, dice_total, point_number)

    
craps(bet, dice_total, point_number)