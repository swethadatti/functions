# def add(a,b):
#     c=a+b
#     print(c)
# x=add(a=4,b=5)

# def add(*b):
#     result=0
#     for i in b:
#         result=result+i
#     return result
# print(add(1,3,4,5))

def person(name,**data):
    print(name)
    for i,j in data.items:
        print(i,j)