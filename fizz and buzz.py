def fun(n):
    if n%5==0 and n%3==0:
        print("fizz buzz")
    if n%3==0:
        print("fizz")
    elif n%5==0:
        print("buzz")
n=int(input("enter the number"))
fun(n)