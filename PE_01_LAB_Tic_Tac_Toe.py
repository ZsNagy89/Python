from random import randrange

def display_board():
    print(board1.values(), sep="\n")
    return

def user_moves():
    step=int(input("Choose a number."))
    if step in range(1,10):
        if board1[step]=="   ":
            board1[step]=" O "
        else:
            print("Please choose another number, it's not free.")
            user_moves()
    else:
        print("Out of the 1-9 range.")
        user_moves()

def computer_moves():
    step_cp=randrange(10)
    if board1[step_cp]=="   ":
        board1[step_cp]=" X "
    else:
        computer_moves()

def somebody_win():
    if board1[1]== " O " and board1[2]== " O " and board1[3]== " O ":
        return False
    elif board1[4]== " O " and board1[5]== " O " and board1[6]== " O ":
        return False
    elif board1[7]== " O " and board1[8]== " O " and board1[9]== " O ":
        return False
    elif board1[1]== " O " and board1[4]== " O " and board1[7]== " O ":
        return False
    elif board1[2]== " O " and board1[5]== " O " and board1[8]== " O ":
        return False
    elif board1[3]== " O " and board1[6]== " O " and board1[9]== " O ":
        return False
    elif board1[1]== " O " and board1[5]== " O " and board1[9]== " O ":
        return False
    elif board1[3]== " O " and board1[5]== " O " and board1[7]== " O ":
        return False
    elif board1[1]== " X " and board1[2]== " X " and board1[3]== " X ":
        return True
    elif board1[4]== " X " and board1[5]== " X " and board1[6]== " X ":
        return True
    elif board1[7]== " X " and board1[8]== " X " and board1[9]== " X ":
        return True
    elif board1[1]== " X " and board1[4]== " X " and board1[7]== " X ":
        return True
    elif board1[2]== " X " and board1[5]== " X " and board1[8]== " X ":
        return True
    elif board1[3]== " X " and board1[6]== " X " and board1[9]== " X ":
        return True
    elif board1[1]== " X " and board1[5]== " X " and board1[9]== " X ":
        return True
    elif board1[3]== " X " and board1[5]== " X " and board1[7]== " X ":
        return True

board1={1:"   ",2:"   ",3:"   ",4:"   ",5:"   ",6:"   ",7:"   ",8:"   ",9:"   "}

display_board()
rounds=1
print("Computer starts! This is Round:",rounds)
board1[5]=" X "
display_board()
rounds=2

while rounds<=9:
        print("User's round! It's the", rounds,"round!")
        user_moves()
        rounds+=1
        if somebody_win()==False:
           print("User won!")
           break
        if rounds==9:
            break
        display_board()
        print("Computer's round! It's the", rounds,"round!")
        computer_moves()
        rounds+=1
        if somebody_win()==True:
           print("Computer won!")
           break        
        display_board()
