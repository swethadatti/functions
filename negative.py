def reverse_order(reverse):
    k=[]
    i=(len(reverse))-1
    while i>=0:
        k.append(reverse[i])
        i=i-1
    return(k)
print(reverse_order(["s","a","i","r","a","m"]))