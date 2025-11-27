name=["vijay","dinkar","yashraj","dinkar","vijay"]
ans={}
for i in name:
    ans[i]=ans.get(i,0)+1

print(ans)