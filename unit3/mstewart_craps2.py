import random
player1_bank = 100
player2_bank = 100
print("Player 1 has ${}".format(player1_bank))
print("Player 2 has ${}".format(player2_bank))
player_pick = random.choice([1,2])
while player1_bank > 0 and player2_bank > 0:
    if player_pick == 1:
        print("Player 1 is the shooter")
        print("")
    elif player_pick == 2:
        print("Player 2 is the shooter")
        print("")
    if player_pick == 1:
        bet = int(input("Player 2 place your bet: "))
        if bet > player2_bank:
            print("You don't have that much money!")
            print("")
        elif bet < 0:
            print("You can't bet a negative number!")
            print("")
        elif bet == 0:
            print("You didn't bet anything.")
            print("")
        elif bet > 0 and bet <= player2_bank:
            print("")
            dice1 = random.choice([1,2,3,4,5,6])
            dice2 = random.choice([1,2,3,4,5,6])
            dice_total = dice1 + dice2
            print("The dice is thrown: {} and {}, {} total".format(dice1, dice2, dice_total))
            if dice_total == 2 or dice_total == 3 or dice_total == 12:
                player1_bank = player1_bank + bet
                player2_bank = player2_bank - bet
                print("You rolled a {}. You lost the round!".format(dice_total))
                print("Player 1 has ${}".format(player1_bank))
                print("Player 2 has ${}".format(player2_bank))
                print("")
            elif dice_total == 7 or dice_total == 11:
                player1_bank = player1_bank - bet
                player2_bank = player2_bank - bet
                bet = bet * 2
                player2_bank = player2_bank + bet
                print("You rolled a {}. You win the round!".format(dice_total))
                print("Player 1 has ${}".format(player1_bank))
                print("Player 2 has ${}".format(player2_bank))
                print("")
            elif dice_total == 4 or dice_total == 5 or dice_total == 6 or dice_total == 8 or dice_total == 9 or dice_total == 10:
                point_number = dice_total
                print("Your point number is {}".format(point_number))
                print("")
                enter = input("Player 1 press enter to roll")
                print("")
                if enter == "":
                    dice1 = random.choice([1,2,3,4,5,6])
                    dice2 = random.choice([1,2,3,4,5,6])
                    dice_total = dice1 + dice2
                    print("The dice is thrown: {} and {}, {} total".format(dice1, dice2, dice_total))
                    if dice_total == 7:
                        dice_total == 7
                        player1_bank = player1_bank + bet
                        player2_bank = player2_bank - bet
                        print("You rolled a 7. You lost the round!")
                        print("Player 1 has ${}".format(player1_bank))
                        print("Player 2 has ${}".format(player2_bank))
                        print("")
                    elif dice_total == point_number:
                        dice_total == point_number
                        player1_bank = player1_bank - bet
                        player2_bank = player2_bank - bet
                        bet = bet * 2
                        player2_bank = player2_bank + bet
                        print("You rolled your point number! You win the round!")
                        print("Player 1 has ${}".format(player1_bank))
                        print("Player 2 has ${}".format(player2_bank))
                        print("")
                    else:
                        while dice_total != 7 or dice_total != point_number:
                            print("No 7 or {}. Reroll!".format(point_number))
                            print("")
                            enter = input("Player 1 press enter to reroll")
                            print("")
                            if enter == "":
                                dice1 = random.choice([1,2,3,4,5,6])
                                dice2 = random.choice([1,2,3,4,5,6])
                                dice_total = dice1 + dice2
                                print("The dice is thrown: {} and {}, {} total".format(dice1, dice2, dice_total))
                                if dice_total == 7:
                                    player1_bank = player1_bank + bet
                                    player2_bank = player2_bank - bet
                                    print("You rolled a 7. You lost the round!")
                                    print("Player 1 has ${}".format(player1_bank))
                                    print("Player 2 has ${}".format(player2_bank))
                                    print("")
                                    break
                                elif dice_total == point_number:
                                    player1_bank = player1_bank - bet
                                    player2_bank = player2_bank - bet
                                    bet = bet * 2
                                    player2_bank = player2_bank + bet
                                    print("You rolled your point number! You win the round!")
                                    print("Player 1 has ${}".format(player1_bank))
                                    print("Player 2 has ${}".format(player2_bank))
                                    print("")
                                    break
        if player1_bank == 0:
            print("Player 2 Wins!")
            break
    elif player_pick == 2:
        bet = int(input("Player 1 place your bet: "))
        if bet > player1_bank:
            print("You don't have that much money!")
            print("")
        elif bet < 0:
            print("You can't bet a negative number!")
            print("")
        elif bet == 0:
            print("You didn't bet anything.")
            print("")
        elif bet > 0 and bet <= player1_bank:
            print("")
            dice1 = random.choice([1,2,3,4,5,6])
            dice2 = random.choice([1,2,3,4,5,6])
            dice_total = dice1 + dice2
            print("The dice is thrown: {} and {}, {} total".format(dice1, dice2, dice_total))
            if dice_total == 2 or dice_total == 3 or dice_total == 12:
                player2_bank = player2_bank + bet
                player1_bank = player1_bank - bet
                print("You rolled a {}. You lost the round!".format(dice_total))
                print("Player 1 has ${}".format(player1_bank))
                print("Player 2 has ${}".format(player2_bank))
                print("")
            elif dice_total == 7 or dice_total == 11:
                player2_bank = player2_bank - bet
                player1_bank = player1_bank - bet
                bet = bet * 2
                player1_bank = player1_bank + bet
                print("You rolled a {}. You win the round!".format(dice_total))
                print("Player 1 has ${}".format(player1_bank))
                print("Player 2 has ${}".format(player2_bank))
                print("")
            elif dice_total == 4 or dice_total == 5 or dice_total == 6 or dice_total == 8 or dice_total == 9 or dice_total == 10:
                point_number = dice_total
                print("Your point number is {}".format(point_number))
                print("")
                enter = input("Player 2 press enter to roll")
                print("")
                if enter == "":
                    dice1 = random.choice([1,2,3,4,5,6])
                    dice2 = random.choice([1,2,3,4,5,6])
                    dice_total = dice1 + dice2
                    print("The dice is thrown: {} and {}, {} total".format(dice1, dice2, dice_total))
                    if dice_total == 7:
                        dice_total == 7
                        player2_bank = player2_bank + bet
                        player1_bank = player1_bank - bet
                        print("You rolled a 7. You lost the round!")
                        print("Player 1 has ${}".format(player1_bank))
                        print("Player 2 has ${}".format(player2_bank))
                        print("")
                    elif dice_total == point_number:
                        dice_total == point_number
                        player2_bank = player2_bank - bet
                        player1_bank = player1_bank - bet
                        bet = bet * 2
                        player1_bank = player1_bank + bet
                        print("You rolled your point number! You win the round!")
                        print("Player 1 has ${}".format(player1_bank))
                        print("Player 2 has ${}".format(player2_bank))
                        print("")
                    else:
                        while dice_total != 7 or dice_total != point_number:
                            print("No 7 or {}. Reroll!".format(point_number))
                            print("")
                            enter = input("Player 2 press enter to reroll")
                            print("")
                            if enter == "":
                                dice1 = random.choice([1,2,3,4,5,6])
                                dice2 = random.choice([1,2,3,4,5,6])
                                dice_total = dice1 + dice2
                                print("The dice is thrown: {} and {}, {} total".format(dice1, dice2, dice_total))
                                if dice_total == 7:
                                    player2_bank = player2_bank + bet
                                    player1_bank = player1_bank - bet
                                    print("You rolled a 7. You lost the round!")
                                    print("Player 1 has ${}".format(player1_bank))
                                    print("Player 2 has ${}".format(player2_bank))
                                    print("")
                                    break
                                elif dice_total == point_number:
                                    player2_bank = player2_bank - bet
                                    player1_bank = player1_bank - bet
                                    bet = bet * 2
                                    player1_bank = player1_bank + bet
                                    print("You rolled your point number! You win the round!")
                                    print("Player 1 has ${}".format(player1_bank))
                                    print("Player 2 has ${}".format(player2_bank))
                                    print("")
                                    break
        if player2_bank == 0:
            print("Player 1 Wins!")
            break