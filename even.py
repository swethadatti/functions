# def even_number(n):
#     i=0
#     a=[]
#     while i<len(n):
#         if n[i]%2==0:
#             a.append(n[i])
#         i=i+1
#     return a
# print(even_number([10,11,12,13,14,17,18,19])

n=[10,11,12,13,14,15,16,17,18]
i=0
a=[]
b=[]
while i<len(n):
    if n[i]%2==0:
       b.append(n[i])
    else:
        a.append(n[i])
    i=i+1
print(a)
print(b)