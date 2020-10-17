x=int(input("Enter a number: "))
for i in range(x+1):
    flag=0
    for j in range(i-1):
        if j>1 and i>1 and i % j==0 :
            flag=1
    if flag == 0 and i>1:
        print(i)