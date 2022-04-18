def sum_number(num):
    i=0
    sum=0
    while i<len(num):
        sum=sum+num[i]
        i=i+1
    return(sum)
print(sum_number([1,2,3,4,5]))
