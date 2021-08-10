#!/bin/python
import numpy as np
import os
import random
import math

class piece:

    position = 0
    text = "____"

        
class square:

    text = "oo"
    counter = -1


def Init_Board(board, off_board):

    board[0,0].text = "++"
    board[0,2].text = "++"
    board[3,1].text = "++"
    board[6,0].text = "++"
    board[6,2].text = "++"

    board[4,0].text = "  "
    board[5,0].text = "  "
    board[4,2].text = "  "
    board[5,2].text = "  "

    
    for i in range(2):
        for j in range(16):
            off_board[j,i].text = "__"

        off_board[0,i].text = "S:"
        off_board[8,i].text = "F:"


def Init_Counters(counters):
    colour = "w"
    upp_colour = "W"

    for i in range(2):
        k = i*7
        for j in range(7):
            l = j+k
            m = str(j+1)

            counters[l].text = colour+m+upp_colour+m
            

        colour = "b"
        upp_colour = "B"


def Print_Board(board, off_board, counters, roll, turn):

    print("")
    if (turn==0):
        print("White rolled: "+str(roll))
    else:
        print("Black rolled: "+str(roll))
        
    for i in range(16):
        index = off_board[i,1].counter
        if (index==-1):
            print(off_board[i,1].text+" ", end='')
        elif (turn==1):
            mask = move_mask[index-7]
            print(counters[index].text[0+2*mask:2+2*mask]+" ", end='')
        else:
            print(counters[index].text[0:2]+" ", end='')
        
    print("")
    print("")
    for i in range(3):
        for j in range(8):
            print(board[j,i].text+" ", end='')
        print("")
    
    print("")
          
          
    for i in range(16):
        index = off_board[i,0].counter
        if (index==-1):
            print(off_board[i,0].text+" ", end='')
        elif (turn==0):
            mask = move_mask[index]
            print(counters[index].text[0+2*mask:2+2*mask]+" ", end='')
        else:
            print(counters[index].text[0:2]+" ", end='')

    print("")



def Init_Pos_Map(pos_map):
    pos_map[:,:,:] = 0
    
    #Mapping of white positions
    pos_map[0,1,0] = 3
    pos_map[1,1,0] = 2

    pos_map[0,2,0] = 2
    pos_map[1,2,0] = 2

    pos_map[0,3,0] = 1
    pos_map[1,3,0] = 2

    pos_map[0,4,0] = 0
    pos_map[1,4,0] = 2

    pos_map[0,5,0] = 0
    pos_map[1,5,0] = 1

    pos_map[0,6,0] = 1
    pos_map[1,6,0] = 1

    pos_map[0,7,0] = 2
    pos_map[1,7,0] = 1

    pos_map[0,8,0] = 3
    pos_map[1,8,0] = 1

    pos_map[0,9,0] = 4
    pos_map[1,9,0] = 1

    pos_map[0,10,0] = 5
    pos_map[1,10,0] = 1

    pos_map[0,11,0] = 6
    pos_map[1,11,0] = 1

    pos_map[0,12,0] = 7
    pos_map[1,12,0] = 1

    pos_map[0,13,0] = 7
    pos_map[1,13,0] = 2

    pos_map[0,14,0] = 6
    pos_map[1,14,0] = 2


    #Mapping of black positions
    pos_map[0,1,1] = 3
    pos_map[1,1,1] = 0

    pos_map[0,2,1] = 2
    pos_map[1,2,1] = 0

    pos_map[0,3,1] = 1
    pos_map[1,3,1] = 0

    pos_map[0,4,1] = 0
    pos_map[1,4,1] = 0

    pos_map[0,5,1] = 0
    pos_map[1,5,1] = 1

    pos_map[0,6,1] = 1
    pos_map[1,6,1] = 1

    pos_map[0,7,1] = 2
    pos_map[1,7,1] = 1

    pos_map[0,8,1] = 3
    pos_map[1,8,1] = 1

    pos_map[0,9,1] = 4
    pos_map[1,9,1] = 1

    pos_map[0,10,1] = 5
    pos_map[1,10,1] = 1

    pos_map[0,11,1] = 6
    pos_map[1,11,1] = 1

    pos_map[0,12,1] = 7
    pos_map[1,12,1] = 1

    pos_map[0,13,1] = 7
    pos_map[1,13,1] = 0

    pos_map[0,14,1] = 6
    pos_map[1,14,1] = 0


def Dice_Roll():
    return random.randint(0,1)


def Who_Goes_First():
    found = False

    while (found==False):
        w_roll = Dice_Roll()+Dice_Roll()+Dice_Roll()+Dice_Roll()
        print("White rolled: "+str(w_roll))
        print("")
        b_roll = Dice_Roll()+Dice_Roll()+Dice_Roll()+Dice_Roll()
        print("Black rolled: "+str(b_roll))
        print("")

        if (w_roll>b_roll):
            print("White Goes First")
            player = 0
            found = True
            
        elif(b_roll>w_roll):
            print("Black Goes First")
            player = 1
            found = True

        else:
            print("Draw, reroll")
            found = False
                          
    return player

def Counter_Positions(board, off_board, counters, pos_map):
    for i in range(14):
        if (counters[i].position==0):
            off_board[(i%7)+1, math.floor(i/7.0)].counter = i
        elif (counters[i].position==15):
            off_board[(i%7)+9, math.floor(i/7.0)].counter = i

            
def Find_Valid_Moves(counters, board, pos_map, turn, roll):

    move_mask = np.zeros((7), dtype=int)
    for i in range(0+7*turn, 7+7*turn):
        check_pos = counters[i].position + roll
        if (check_pos>15):
            move_mask[i-7*turn] = 0
            continue

        ind_1 = pos_map[0, check_pos, turn]
        ind_2 = pos_map[1, check_pos, turn]

        target_counter = board[ind_1, ind_2].counter

        if (target_counter==-1):
            move_mask[i-7*turn] = 1
        elif ((ind_1==3)and(ind_2==1)and(target_counter!=-1)):
            move_mask[i-7*turn] = 0

        elif (target_counter%7==turn):
            move_mask[i-7*turn] = 0
        else:
            move_mask[i-7*turn] = 1

    return move_mask


# def Test():
#     rolls = np.zeros(5)
#     n = 1000000
#     for i in range(n):
#         roll = Dice_Roll()+Dice_Roll()+Dice_Roll()+Dice_Roll()
#         rolls[roll] += 1


#     for i in range(5):
#         print(rolls[i]/n)


    
board = np.empty((8,3), dtype = object)
for i in range(3):
    for j in range(8):
        board[j,i] = square()

off_board = np.empty((16,2), dtype = object)
for i in range(2):
    for j in range(16):
        off_board[j,i] = square()        
Init_Board(board, off_board)
        

pos_map = np.empty((2,16,3), dtype = int)
Init_Pos_Map(pos_map)


counters = np.empty((14), dtype = object)
for i in range(14):
    counters[i] = piece()
Init_Counters(counters)


random.seed()

round = -1
os.system('cls||clear')


if (round<1):
    round = Who_Goes_First()

turn = round%2

Counter_Positions(board, off_board, counters, pos_map)

roll = Dice_Roll()+Dice_Roll()+Dice_Roll()+Dice_Roll()
move_mask = np.zeros((7), dtype = int)
move_mask = Find_Valid_Moves(counters, board, pos_map, turn, roll)


Print_Board(board, off_board, counters, roll, turn)


