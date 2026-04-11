# Menu-driven ATM system.
print("Welcome to ATM")
print("1: for check balance")
print("2: for check withdraw")
print("3: for check deposit")
choice = input("Enter what do you want:")
balance = 100
if choice == '1':
    print(f"Balance is: {balance}")
elif choice == '2':
    amount = int(input("Enter amount: "))
    if amount > balance:
        print("Amount is less!")
    else:
        balance -= amount
        print(f"withdraw successfully, New balance is: {balance}")

elif choice == '3':
    amount = int(input("Enter amount: "))
    balance += amount
    print(f"Deposit successfully, New balance is: {balance}")
else:
    print("Invalid choice!")
