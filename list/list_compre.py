n=int(input("enter a number "))
ans=[i*i for i in range(1,n+1) if i%2==0]
print(ans)