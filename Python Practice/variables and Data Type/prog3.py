# Find the largest of three numbers.

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))

if n1 > n2:
    if n1 > n3:
        print(f"{n1} is large!")
    else:
        print(f"{n3} is large!")
elif n2 > n3:
    print(f"{n2} is large!")
else:
    print(f"{n3} is large!")
