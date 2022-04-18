def max(number):
    i=0
    maxi=number[i]
    while i<len(number):
        if number[i]>maxi:
            maxi=number[i]
        i=i+1
    return maxi
print(max([2,5,8,12,15]))