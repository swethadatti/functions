def perfect(num):
    i=1
    s=0
    while i<num:
        if num%i==0:
            s=s+i
        i=i+1
    return s
num=int(input("enter number"))
c=perfect(num)
if c==num:
        print(num,"is  a perfect number")
else:
    print(num,"is not a perfect number")

            