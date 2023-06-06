#

print("\n** WELCOME TO SUPER SMOOTHIE! **")

bill = float(0)

while True:

    strawberry_banana = 3
    mango = 2
    peanut_butter_choc_chip = 3
    
    print("\n1. Strawberry & Banana Smoothie\t\t$", strawberry_banana)
    print("2. Mango Smoothie\t\t\t$", mango)
    print("3. Peanut Butter Chocolate Chip\t\t$", peanut_butter_choc_chip)
    print("4. Checkout")

    order = input("\nWhat would you like to order? ")

    if order == "1":
        bill += 3
        f = open("smoothies_receipt.txt", 'a')
        f.write("STRAWBERRY & BANANA SMOOTHIE       $ 3\n")
        f.close()
    elif order == "2":
        bill += 2
        f = open("smoothies_receipt.txt", 'a')
        f.write("MANGO SMOOTHIE                     $ 2\n")
        f.close()
    elif order == "3":
        bill += 3
        f = open("smoothies_receipt.txt", 'a')
        f.write("PEANUT BUTTER CHOCOLATE CHIP       $ 3\n")
        f.close()
    elif order == "4":
        break

print ("\n\nYOUR BILL:\n")
f = open("smoothies_receipt.txt", 'r')
text = f.read()
print (text)

f = open("smoothies_receipt.txt", 'w')
f.close()

tax = round(bill * .06, 2)
total_balance = round(bill + tax, 2)

print ("\nSubtotal:\t\t$", bill)
print ("\n6% Taxes:\t\t$", tax)

leave_tip = input("\nWould you like to leave a tip? (y/n): ")

if leave_tip == "y":
    print("\nPlease pick tip amount: ")
    print("\n1 - 10%")
    print("2 - 15%")
    print("3 - 20%")
    
    amount = input("\nEnter the tip item number: ")
    
    if amount == "1":
        tip = round(bill * 0.1, 2)
        print("\n10% Tip:\t\t$", tip)
    elif amount == "2":
        tip = round(bill * 0.15, 2)
        print("\n15% Tip:\t\t$", tip)
    elif amount == "3":
        tip = round(bill * 0.2, 2)
        print("\n20% Tip:\t\t$", tip)
    
    print("\nTotal Balance:\t\t$", round(total_balance + tip, 2), "\n")

elif leave_tip == "n":
    print("\nTotal Balance:\t\t$", round(total_balance, 2), "\n")

#