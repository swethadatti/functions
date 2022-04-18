# i=0
# while i<10:
#     i=i+1
#     if i>2 and i<9:
#         continue
#     print(i)
    

def fun(weight,hight):
    bmi=a/b
    if bmi<=18.5:
        print("under weigt")
    elif bmi<=25.0:
        print("normal")
    elif bmi<=30.0:
        print("over weight")
    else:
        print("obese weight")
b=int(input("enter hight"))
a=int(input("enter the weight"))
fun(a,b)
