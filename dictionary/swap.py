d={"a":1,"b":1,"c":2}
ans={}
for k, v in d.items():
    ans.setdefault(v,[]).append(k)
print(ans)
