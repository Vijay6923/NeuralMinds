def average_marks(name,marks):
    d=dict(zip(name,marks))
    for k,v in d.items():
        avg=sum(v)/len(v)
        print(k,avg)




name=["vijay","dinkar"]
marks=[[40,50,60],[70,80,90]]
print(average_marks(name,marks))
