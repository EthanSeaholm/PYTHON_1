#

import random

while True:      # until a proper float or int is inputted into 'money_in', the following code will continue to loop

    try:

        money_in = (float(input("\nHow much money would you like to insert into the machine? ")))
        
        while money_in <= 0:
            money_in = (float(input("\nYOU CANNOT BET WITH NO MONEY OR LOWER, TRY AGAIN: ")))     # cannot enter a float or int 

        format_money_in = "{:.2f}".format(money_in)
        print (f"\nYou have inputted ${format_money_in} into the machine")
        break

    except ValueError as e:     # triggers when a string is inputted into 'money_in'
        
        print ("\nERROR, ENTER AN INTEGER OR FLOAT:", e)

while True:       # the same as the loop above

    try:

        bet = (float(input("\nHow much money would you like to bet? ")))
        
        while bet <= 0:
            bet = (float(input("\nINVALID BET, TRY AGAIN: ")))
        
        while bet > money_in:
            bet = (float(input("\nERROR, BET CANNOT BE HIGHER THAN YOUR BALANCE. TRY AGAIN: ")))

        format_bet = "{:.2f}".format(bet)
        print (f"\nYou are betting ${format_bet}")
        break

    except ValueError as e:

        print ("\nERROR, ENTER AN INTEGER OR FLOAT:", e)

profits = money_in      # 'profits' stores the inputted 'money_in' float or int and is now used as a counter for wins and losses

# slot code

while True and profits != 0:

    print ("\nROLLING!")
    profits -= bet      # 'profits' being used as a counter

    roll_1 = ["ORANGE...", "APPLE...", "CHERRY...", "BANANA...", "PEACH...", "WATERMELON..."]
    random_choice_1 = random.choice(roll_1)

    roll_2 = ["ORANGE...", "APPLE...", "CHERRY...", "BANANA...", "PEACH...", "WATERMELON..."]
    random_choice_2 = random.choice(roll_2)

    roll_3 = ["ORANGE...", "APPLE...", "CHERRY...", "BANANA...", "PEACH...", "WATERMELON..."]
    random_choice_3 = random.choice(roll_3)

    print (random_choice_1)
    print (random_choice_2)
    print (random_choice_3)

    if random_choice_1 == random_choice_2 == random_choice_3:
        print ("\nJACKPOT!")
        profits = (profits + (bet * 3))
        format_profits = "{:.2f}".format(profits)
        print (f"\nYOU HAVE ${format_profits} REMAINING")

    elif random_choice_1 == random_choice_2 or random_choice_2 == random_choice_3 or random_choice_3 == random_choice_1:
        print ("\nDOUBLE!")
        profits = (profits + (bet * 2))
        format_profits = "{:.2f}".format(profits)
        print (f"\nYOU HAVE ${format_profits} REMAINING")

    elif random_choice_1 != random_choice_2 and random_choice_2 != random_choice_3 and random_choice_3 != random_choice_1:
        print ("\nBETTER LUCK NEXT TIME!")
        format_profits = "{:.2f}".format(profits)
        print (f"\nYOU HAVE ${format_profits} REMAINING")
        
    if profits == 0:        # losing all of your money will break you out of the loop. the code will end
        print ("\nOUT OF MONEY")
        break

    play_again = (input("\nPLAY AGAIN (y/n) or CHANGE BET AMOUNT (r): ")).lower()       # the user can choose to play again, stop playing, or change their bet amount

    while play_again != "y" and play_again != "n" and play_again != "r":
        play_again = (input("\nINVALID INPUT, TRY AGAIN: ")).lower()      # ints or floats cannot be inputted

    # changing the bet amount
        
    if play_again == "r":
        
        while True:

            try:
                    
                bet = (float(input("\nWhat would you like to change your bet to? ")))
                
                while bet <= 0 or bet > profits:
                    bet = (float(input("\nINVALID BET, TRY AGAIN: ")))

                format_bet = "{:.2f}".format(bet)
                print (f"\nYou are betting ${format_bet}")
                break

            except ValueError as e:

                print ("\nERROR, ENTER AN INTEGER OR FLOAT:", e)

    if play_again == "n":     # upon entering 'n' into play_again, the loop is ended
        break

# calculating profits 

if profits > money_in:
    final_profits = profits - money_in

    format_final_profits = "{:.2f}".format(final_profits)
    format_profits = "{:.2f}".format(profits)

    print (f"\nYOU ARE WALKING AWAY WITH A ${format_final_profits} PROFIT FOR A TOTAL OF ${format_profits}")      # winning money
    
elif profits < money_in and profits != 0:
    loss = money_in - profits

    format_loss = "{:.2f}".format(loss)
    format_profits = "{:.2f}".format(profits)
    format_money_in = "{:.2f}".format(money_in)
    
    print (f"\nYOU LOST -${format_loss} FROM YOUR INPUT OF ${format_money_in} AND YOU ARE WALKING AWAY WITH A TOTAL OF ${format_profits}")        # losing money

elif profits == money_in:
    print ("\nYOU BROKE EVEN")        # breaking even

print("\nTHANKS FOR PLAYING\n")

#