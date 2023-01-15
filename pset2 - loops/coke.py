# In a file called coke.py, implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due.
# Once the user has inputted at least 50 cents, output how many cents in change the user is owed. Assume that the user will only input
# integers, and ignore any integer that isn’t an accepted denomination.


price = 50
coins = [25, 10, 5]

while price > 0:
    print("Amount Due:", price)
    pmt = int(input("Insert Coin: "))
    if pmt in coins:
        price = price - pmt
    else:
        continue

print("Change Owed:", (price * (-1)))
