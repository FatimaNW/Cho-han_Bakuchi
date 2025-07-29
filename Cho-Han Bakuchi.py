from random import *

cash_total = 100 

name = input("\nPlease enter a Username: ")
print("\nHello " + name.title() +"!")
print("Let's play a game of Cho-Han! ")
print("Available Cash: $", cash_total)

def cho_han(): 
    global cash_total 
    odd_or_even = str(input("\nPlease enter Odd or Even: "))
    if odd_or_even.lower() == "even" or odd_or_even.lower() =="odd": 

        try: 
            place_wager = int(input("Please enter your Wager: ")) 

            if place_wager <= 0:
                print("Wager must be greater than $0. Please try again.")
                return cho_han()
            elif place_wager <= cash_total:
                print("\nYou placed $", place_wager, "on", odd_or_even.title())
                dice_1 = randint(1, 6)
                dice_2 = randint(1, 6)
                input("\nPress Enter to roll both dice ")
                print("\nDice 1 = ", dice_1)
                print("Dice 2 = ", dice_2)
                sum_of_two_dice = dice_1 + dice_2
                remainder = sum_of_two_dice % 2
            else:
                print("You don't have enough money. Your total cash: $", cash_total,)
                return cho_han()

            if remainder == 0 and odd_or_even.lower() == "even":
                cash_total = place_wager + cash_total
                print("\nThe sum of the two dice is an Even Number!")
                print("You Won!!!")
                print("Total cash is $", cash_total)
            elif remainder == 1 and odd_or_even.lower() == "odd":
                cash_total = place_wager + cash_total
                print("\nThe sum of the two dice is an Odd Number!")
                print("You Won!!!")
                print("Total cash is $", cash_total)
            else:
                cash_total = cash_total - place_wager
                print("\nThe sum of the two dice is not", odd_or_even.title(), ":(")
                print("Sorry, you Lost!!!")
                print("Total cash is $", cash_total)

            play = (input("\nDo you want to play again? Y/N \n"))
            if play.upper() == "Y":
                if cash_total > 0:
                    return cho_han()
                else:
                    print("\nYou've run out of money, sorry!")
            elif play.upper() == "N":
                print("\nThank you for playing!")

        except ValueError:
            print("The inputted value is not an integer, please try again.")
            return cho_han()

    else:
        print("Invalid answer, please try again.")
        return cho_han()

cho_han()