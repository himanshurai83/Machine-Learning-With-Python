# Grade calculator (A, B, C based on marks).
mark = int(input('Enter marks: '))
if mark < 100:
    if mark > 90:
        print("Grade A+")
    elif mark <= 90 and mark > 80:
        print("Grade A")
    elif mark <= 80 and mark > 70:
        print("Grade B")
    elif mark <= 70 and mark > 55:
        print("Grade C")
    else:
        print("Fails!")
else:
    print("Invalid marks!")
