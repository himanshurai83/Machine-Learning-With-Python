# Create a simple calculator using operators (+, -, *, /, %).
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

choice = input("Enter your choice(+,-,*,/,%): ")
if choice == '+':
    print(f"Sum: {n1+n2}")
elif choice == '-':
    print(f"Sub: {n1-n2}")
elif choice == '*':
    print(f"Mul: {n1*n2}")
elif choice == '/':
    print(f"Div: {n1/n2}")
elif choice == '%':
    print(f"Rem: {n1 % n2}")
else:
    print("Invalid choice!")
