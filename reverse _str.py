def reverse_str(name):
    i=-1
    a=""
    while i<=len(name):
        a+=name[-i]
        i+=1
    return(a)
a=input("enter the string")
print(reverse_str(a))






