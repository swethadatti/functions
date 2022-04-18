def max(number):
    i=1
    m=[0]
    while i<len(number):
        if number[i]>m:
            m=number[i]
        i=i+1
    return m
d=max([[0],[1,3],[5,7],[9,11],[13,15,17]])
print((len(d),(d)))