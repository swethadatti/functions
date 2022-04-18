def sum(a):
    i=0
    s=0
    while i<=len(a):
        j=0
        while j<len(a):
            sum=s+a[i][j]
        i=i+1
    print(s)
sum([1,2,3,4,[5,6,7,8,9],10])
