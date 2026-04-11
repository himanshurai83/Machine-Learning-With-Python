# Check whether a number is Armstrong or not.
n = int(input("Enter a number: "))
tmp = n
arm = 0
digit = 0
while n != 0:
    rem = n % 10
    digit += 1
    n = n//10
n = tmp
while n != 0:
    rem = n % 10
    arm += rem**digit
    n = n//10
if tmp == arm:
    print("The number is armstrong!")
else:
    print("Number is not armstrong!")
