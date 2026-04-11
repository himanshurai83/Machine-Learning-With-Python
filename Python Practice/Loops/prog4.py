# Check palindrome number.
n = int(input("Enter a number: "))
rev = 0
tmp = n
while n != 0:
    rem = n % 10
    rev = rev * 10 + rem
    n = n//10
if tmp == rev:
    print("Number is palindrome!")
else:
    print("Number is not palindrome!")
