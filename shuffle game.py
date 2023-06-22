from random import shuffle
## i have written a code to make a shell game#
mylist = [" ","o"," "]

## first i took a list then i implement a shuffle function to shuffle list#
def shuffle_list(my_list):
    shuffle(my_list)
    return my_list


t=shuffle_list(mylist)

## here i took a guess from player##
def player_guess():

    guess = " "
    while guess not in ['0','1','2']:
        guess = input("pick on of the glass 0,1 or 2 :")

    return int(guess)


g= player_guess()
# print(g)

##to check the result##

def answer_it(mylist,guess):
    if mylist[guess] == 'o':
        print("congratulation, you guessed it correct")

    else:
        print("better luck next time")
        print("the ball was in other cup:-",mylist)


answer_it(t,g)