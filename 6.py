x=(input("Enter a number: "))
n=len(x)
x=int(x)
sum=0
r=x
while(r>0):
    sum+=(r%10)**n
    r//=10
if x==sum:
    print("It's a Armstrong Number")
else:
    print("Not an Armstrong Number")