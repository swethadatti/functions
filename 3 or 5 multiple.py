def fun(a):
    i=0
    s=0
    while i<=a:
        if i%3==0 or i%5==0:
            s=s+i
        i=i+1
    return s
b=fun(10)
print(b)