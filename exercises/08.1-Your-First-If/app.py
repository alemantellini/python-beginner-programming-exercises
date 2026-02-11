# EJERCICIO 8.1 - your first if
total = int(input('How much money do you have in your pocket\n'))
# ↓ YOUR CODE HERE ↓
if total > 100:
    print("Give me your money!")
else:
    if total > 50:
        print("Buy me some coffee, you cheap!")
    else:
        if total <= 50:
            print("You are a poor guy, go away!")
