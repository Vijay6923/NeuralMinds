def mean(values):
    mean=sum(values)/len(values)
    var=sum((i-mean)**2 for i in values)/len(values)
    return var** 0.5
    


values=[10,20,30,40,50]
print(mean(values))






