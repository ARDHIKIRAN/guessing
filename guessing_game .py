from random import shuffle
mylist=["0"," "," "]
def shuffle_list(mylist):
    shuffle(mylist)
    return mylist
mixed_list=shuffle_list(mylist)
def guess_number():
    user_guess=input("enter the guess position: ")
    while user_guess not in  ["0","1","2"]:
        user_guess=input("enter the guess position: ")
       
    return int(user_guess)    
def guess_game(mylist,guess):
    if mylist[guess] == "0":
        print("correct guess")
    else:
        print("incorrect guess")
        print(mylist)
 
guess=guess_number()#fuction calling

guess_game(mixed_list,guess)#another function calling