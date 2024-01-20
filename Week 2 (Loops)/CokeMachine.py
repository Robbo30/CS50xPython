amountDue = 50

while amountDue > 0:
    print("Amount Due:",amountDue)

    coin = int(input("Insert Coin: "))

    if coin in [25,10,5]:
        amountDue = amountDue - coin

    if amountDue < 0:
        break

print("Change Owed:",amountDue)


