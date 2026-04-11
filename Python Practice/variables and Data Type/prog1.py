# Swap two numbers without using third variable.
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
print(f"Before swapping n1 = {n1} and n2 = {n2}")
n1 = n1+n2
n2 = n1-n2
n1 = n1-n2
print(f"After swapping n1 = {n1} and n2 = {n2}")
