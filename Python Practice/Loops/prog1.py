# Print Fibonacci series up to n terms.
n = int(input("Enter nth term: "))
f = 0
s = 1
i = 0
while i < n:
    print(f)
    th = f+s
    f = s
    s = th
    i += 1
