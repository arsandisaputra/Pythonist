n = 7
ar = [1,2,1,2,1,3,2]
unpaired = []
while len(ar) > 0:
    flag = ar[0]
    unpaired.append(ar[0])
    ar.remove(ar[0])
    if flag in ar:
        ar.remove(flag)
        unpaired.remove(flag)
print((n - len(unpaired))//2)
    
    
