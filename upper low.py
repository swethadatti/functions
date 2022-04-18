# def up_law(stri):
#     a=ord(stri)
#     upp=0
#     low=0
#     i=0
#     while i<len(stri):
#         if 94<99:
#             low+=1
#         elif 65<69:
#             upp+=1
#         i=i+1
#     print(upp)
#     print(low)
# stri=input("The Quick Brow Fox")
# up_law(stri)
def upper():
    string="The Quick Brow box"
    i=0
    count=0
    count1=0
    while i<len(string):
        if string[i].isupper():
            count=count+1
        elif string[i].islower():
            count1=count1+1
        i=i+1
    print(count)
    print(count1)
upper()