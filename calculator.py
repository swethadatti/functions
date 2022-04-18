def add(a,b):
    c=a+b
    return c
def sub(a,b):
    d=a-b
    return d
def multi(a,b):
    e=a*b
    return e
def div(a,b):
    f=a/b 
    return f
def main():
    if smb == "+":
        print(add(a,b))
    elif smb == "-":
        print(sub(a,b))
    elif smb == "*":
        print(multi(a,b))
    elif smb == "/":
        print(div(a,b))
a=int(input("enter the number"))
b=int(input("enter the number"))
smb=input("enter the symbol")
main()