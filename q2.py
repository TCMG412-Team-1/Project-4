import random

def roll_die():
    return random.randint(1, 11)

def player():
    print('************ YOUR TURN ************')
    rounds = 1
    while (rounds != 3):
        if (rounds == 1):
            first = roll_die()
            rounds += 1
        elif (rounds == 2):
            second = roll_die()
            rounds += 1
            total = second
            second = first + second
            print ("Roll: ", first, second)
            
            
            if (total == 21):
                print("Blackjack!") 
            else:
                print("Total: ",total)
                
            #if not automatic blackjack and have to roll
            user = input("(s)tay or (r)oll?")
            print(" ")
            
            while (user == "r") and (total <21):
                rolldice = roll_die()
                total = total +rolldice
                print (" ")
                print ("Roll: ", rolldice)
                print ("Total: ",total)
                
                if (total < 21):
                    user = input("(s)tay or (r)oll?")
                elif (total > 21):
                    user == "s"
                    print ('Bust!')
                    return total
                elif (user == "s"):
                    return total
                elif (user == "r"):
                    return total
            return total

def dealer():
    dice1 = roll_die()
    dice2 = roll_die()
    dice3 = roll_die()
    total = player()
    print("********** DEALER'S TURN **********")
    dicetotal = dice1 + dice2
    print("Total: ", dicetotal)
    
    while (total >= dicetotal < 21):
        enter = input("Press <enter> to continue...")
        print("Roll: ", dice3)
        dicetotal = dicetotal + dice3
        print("Total: ", dicetotal)

def main():
    total = player()
    if (total == "blackjack"):
        print("********** GAME OVER ********** You win!")
    elif (total > 21):
        dicetotal = dealer()
        print("********** GAME OVER ********** Dealer wins!")
    elif (total >21):
        print("********** GAME OVER ********** Dealer wins!")
    else:
        dicetotal = dealer()
        if (dicetotal > total):
            print("********** GAME OVER ********** Dealer wins!")
        elif (dicetotal < total):
            print("********** GAME OVER ********** Player wins!")
        elif (dicetotal >21):
            print("********** GAME OVER ********** You win!")
            
main()