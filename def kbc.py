def option(index):
    j=0
    while j<len(option[index]):
        print(j+1,[index][j])
        j=j+1
    user_ans=int(input("enter your option"))
    if user_ans ==ans_list[index]:
        return True
    if user_ans ==5050:
        return(life line(index))
    else:
        return False
def que():
    index=0
    while index<len(que_list):
        print("q",index+1,que_list[index],"?")
        result=option(index)
        if result =="no":
            index+=1
        elif result == true:
            print("congrtulations your enter the next question")
        else:
            print("oops! you choose wrong option you left the game")
            break
        index+=1
def kbc():
    que()
kbc()
