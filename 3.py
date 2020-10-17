print("Enter three numbers: ")
x=int(input())
y=int(input())
z=int(input())
if x>y:
    if x>z:
        print("x is the greatest")
    else:
        print("z is the greatest")
else:
    if y>z:
        print("y is the greatest")
    else:
        print("z is the greatest")
