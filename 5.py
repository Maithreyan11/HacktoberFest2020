x=0
y=1
n=int(input("Enter a number: "))
print(x)
print(y)
i=3
while i<=n :
    print(x+y)
    (x,y)=(y,x+y)
    i+=1
