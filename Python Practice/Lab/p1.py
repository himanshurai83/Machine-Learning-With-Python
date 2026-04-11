n = int(input("Enter a number: "))
i = 0
while n != 0:
    n = n//10
    i += 1
print(f"Number of digit is : {i}")


n = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{n} X {i} = {n*i}")
