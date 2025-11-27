def min_max(values):
    mn,mx=min(values),max(values)
    return [(i-mn)/(mx-mn) for i in values]
    
    


values=[10,20,30,40,50]
print(min_max(values))






