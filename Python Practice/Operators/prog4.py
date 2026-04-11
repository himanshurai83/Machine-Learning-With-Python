# Find profit or loss percentage.

cp = int(input("Enter cost price: "))
sp = int(input("Enter selling price: "))
if cp > sp:
    loss = cp - sp
    print(f"Loss percentage: {(loss/cp) * 100}%")
else:
    profit = sp-cp
    print(f"Profit percentage: {(profit/cp) * 100}%")
