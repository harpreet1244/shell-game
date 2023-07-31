import random

def display(board):
    print(b_list[1]+ "|", b_list[2] + "|",b_list[3] + "|" )
    print("----------")
    print(b_list[4]+ "|", b_list[5] + "|",b_list[6] + "|" )
    print("----------")
    print(b_list[7]+ "|", b_list[8] + "|",b_list[9] + "|" )
    print("----------")

   
b_list = ["#"," "," "," "," "," "," "," "," "," "]
# display(b_list)

def player():
    marker = "wrong"
    while not (marker =="x" or marker == "o"):
        marker = input("player : choose x or o: ")
        if marker not in ["x","o"]:
            print("please select x or o to start")
    if marker == "x":
        return("x","o")
    else:
         return("o","x")
    
    
player1_choice , player2_choice = player()
##print("player2 has selected: ",player2_choice)

def position():
    choice = 0
    while choice not in [1,2,3,4,5,6,7,8,9]:
        choice = int(input("select the position where you want to mark: "))
        if choice not in [1,2,3,4,5,6,7,8,9]:
            print("enter the relivent position")
    return choice



def place(board,marker,position):
     board[position] = marker


place(b_list,"x",8)
# display(b_list)

def win_check(board,mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark)or
    (board[4] == mark and board[5] == mark and board[6] == mark)or
    (board[1] == mark and board[2] == mark and board[3] == mark)or
    (board[7] == mark and board[4] == mark and board[1] == mark)or
    (board[8] == mark and board[5] == mark and board[2] == mark)or
    (board[9] == mark and board[6] == mark and board[3] == mark)or
    (board[7] == mark and board[5] == mark and board[3] == mark)or
    (board[9] == mark and board[5] == mark and board[1] == mark))




win_check(b_list,"x")


def choose_first():
    flip = random.randint(0,1)


    if flip == 0:
        return 'player 1'
    else:
        return "player 2"
    


def space_check(board,position):
    return b_list[position] == " "
     

def full_board_check(b_list,position):
    for i in range(0,10):
        if space_check(b_list,i):
            return False
        
    return True

def player_choice(board):
    position = 0
    while position  not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input("choose a position (1-9): "))

    return position

def replay():
    choice = input("play again? enter yes or no")
    return choice == "yes"


print("welcome to tic tac toe")

while True:

    the_board = [" "]*10
    player1_choice,player2_choice = player()

    turn = choose_first()
    print(turn +  "will go first")

    play_game = input("READY TO PLAY y or n: ")

    if play_game == "y":
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn =="player 1":
            display(b_list)

            position = player_choice(b_list)
            place(b_list,player1_choice,position)

            if win_check(b_list,player1_choice):
                display(b_list)
                print("player1 has won")
                game_on = False
            else:
                if full_board_check(b_list,position):
                    display(b_list)
                    print("tie game")
                    game_on = False
                else:
                    turn = "player 2"
                
        else:
            position = player_choice(b_list)
            place(b_list,player2_choice,position)

            if win_check(b_list,player2_choice):
                display(b_list)
                print("player2 has won")
                game_on = False
            else:
                if full_board_check(b_list,position):
                    display(b_list)
                    print("tie game")
                    game_on = False
                else:
                    turn = "player 1"
        

    if not replay():
        break

        
    
