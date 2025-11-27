n=int(input("enter a number: "))
for i in range(1,n+1):
    if i==5:
        continue
    if i==9:
        break
    print(i,end=" ")