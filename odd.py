# def odd_number(n):
#     i=0
#     a=[]
#     while i<len(n):
#         if n[i]%2!=0:
#             a.append(n[i])
#         i=i+1
#     return a
# print(odd_number([10,11,12,13,14,17,18,19]))


def even_odd(limit):
    i=1
    while i<=user:
        if i%2==0:
            print(i,"even numbr")
        else:
            print(i,"odd number")
        i=i+1
user=int(input("enter the limit"))
even_odd(user)





