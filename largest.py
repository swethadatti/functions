def fun(a,b,c):
    if a>b:
        if a>c:
            print(a, "is largest")
        else:
            print(c,"is largest")
    else:
        if b>c:
            print(b,"is largest")
        else:
            print(c,"is largest")
a=int(input("enter the number"))
b=int(input("enter the number"))
c=int(input("enter the number"))
fun(a,b,c)



