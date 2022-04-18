def fun(a):
    i=0
    c=0
    b=0
    while i<len(a):
        if a[i]<0:
            c=c+1
        elif a[i]>0:
            b=b+1
        i=i+1
    print(c)
    print(b)
a=[2,-7,5,-64,-14]
fun(a)
