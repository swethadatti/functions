def positive_sum(num):
    s=0
    i=0
    while i<len(num):
        if num[i]>0:
            s=s+num[i]
        i=i+1
    return(s)
print(positive_sum([1,8,3,2,-2]))