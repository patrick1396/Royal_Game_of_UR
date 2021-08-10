#!/bin/python
import numpy as np
import os
import random
import math

#Define the piece object
#Contains the position and the display text of the piece, this is initially set just to 4 empty spaces
class piece:

    position = 0
    text = "____"

#Define the square object that a piece can be on
#Contains the display text, initialised as the most common text "oo" showing an empty space
         #and the index of the counter currently on the square, initialised as -1
class square:

    text = "oo"
    counter = -1


#Subroutine to initialise the board and off_board arrays
#Sets the special squares on the board and the empty squares on the board
#Off board array stores the pieces that are yet to be played, preceeded by an S; and the pieces that have finished, preceeded by an F. In this subroutine the arrays are populated with the S and F and underscores where the pieces go
def Init_Board(board, off_board):

    #Set the text of the special squares on the board
    board[0,0].text = "++"
    board[0,2].text = "++"
    board[3,1].text = "++"
    board[6,0].text = "++"
    board[6,2].text = "++"

    #Set the text of the eqpty squares on the board
    board[4,0].text = "  "
    board[5,0].text = "  "
    board[4,2].text = "  "
    board[5,2].text = "  "


    #Goes through all squares of the off_board array and initialises the text of all of them 
    for i in range(2):
        for j in range(16):
            #All initially set to two underscores
            off_board[j,i].text = "__"

        #First and ninth square' text set to S: anf F: respectively
        off_board[0,i].text = "S:"
        off_board[8,i].text = "F:"

        
#Subroutine to initialise the pieces of the two players and stores them in the counters array
def Init_Counters(counters):

    #First 7 pieces are white pieces
    colour = "w"
    #Upper case used to indicate pieces that can move
    upp_colour = "W"

    #Loop over i = 0 and 1
    for i in range(2):
        #Multiply i by 7 to give the first index of the set
        k = i*7

        #Loop over i = 0 to 6
        for j in range(7):
            #l is the index of the current piece
            l = j+k

            #m is a character that is the number of the piece
            m = str(j+1)

            #set the text of the counter to be the lower case colour, the number, the upper case colour and then the number
            counters[l].text = colour+m+upp_colour+m
            
        #set colour and upper case colour to b for the second loop when i = 1
        colour = "b"
        upp_colour = "B"


#Subroutine to print the current state of the game
#Takes as input the board, the off_board array, the counters array, the current dice roll, the current player and the mask of allowed moves of the current player
def Print_Board(board, off_board, counters, roll, player, move_mask):

    #Print a blank line
    print("")

    #Go over the 16 positions in the black off_board array
    for i in range(16):
        #Find the counter index of the current off_board square
        index = off_board[i,1].counter

        #If the index is -1 then current square does not have a piece, print the suares default text value
        if (index==-1):
            print(off_board[i,1].text+" ", end='')

        #Otherwise, if the current player is the black piece player then 
        elif (player==1):
            #Find the value of the move mask of the current piece
            mask = move_mask[index-7]
            #Print the text of the current piece, if the current value of mask is 1 then this will print the upper case text, otherwise it will print the lower case text
            print(counters[index].text[0+2*mask:2+2*mask]+" ", end='')
        else:
            #Print the lower cast text of the current piece
            print(counters[index].text[0:2]+" ", end='')
    #Print some blank lines
    print("")
    print("")

    #Loop over the positions on the board
    for i in range(3):
        for j in range(8):
            #Find the counter index of the current board square
            index = board[j,i].counter

            #If the index is -1 then current square does not have a piece, print the suares default text value
            if (index==-1):
                print(board[j,i].text+" ", end='')

            #If the index corresponds to the current player and can be moved according to the move mask then print the upper case text of the piece otherwise print the lower case text
            elif (math.floor(index/7.0)==player):
                mask = move_mask[index-7*player]
                print(counters[index].text[0+2*mask:2+2*mask]+" ", end='')

            #If the index doesn't correspond to the current player then print the lower case text of the pieces
            else:
                print(counters[index].text[0:2]+" ", end='')

        
        print("")
    
    print("")
          
    #Go over the 16 positions in the white off_board array 
    for i in range(16):
        #Find the counter index of the current off_board square
        index = off_board[i,0].counter

        #If the index is -1 then current square does not have a piece, print the suares default text value
        if (index==-1):
            print(off_board[i,0].text+" ", end='')

        #Otherwise, if the current player is the white piece player then 
        elif (player==0):
            #Find the value of the move mask of the current piece
            mask = move_mask[index]
            #Print the text of the current piece, if the current value of mask is 1 then this will print the upper case text, otherwise it will print the lower case text
            print(counters[index].text[0+2*mask:2+2*mask]+" ", end='')

        #Print the lower cast text of the current piece
        else:
            print(counters[index].text[0:2]+" ", end='')

    print("")
    print("")

    #Print the dice roll of the current player
    if (player==0):
        print("White rolled: "+str(roll))
    else:
        print("Black rolled: "+str(roll))


#Subroutine that defines the position map array, the counters just count their position as integers, these integers correspond to an x and y coordinate on the board.
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



#The dice roll is either a 0 or a 1, like a coin flip
def Dice_Roll():
    return random.randint(0,1)


#Function to decide who goes first, this is decided by each player rolling four dice until one gets a higher number than the other. This player goes first
#Returns a number the indicates the first player, 0 is the white pieces, 1 is the black pieces
def Who_Goes_First():

    #Initialise found as false
    found = False

    #Loop while found is false
    while (found==False):
        #Roll for white piece player and print
        w_roll = Dice_Roll()+Dice_Roll()+Dice_Roll()+Dice_Roll()
        print("White rolled: "+str(w_roll))
        print("")

        #Roll for black piece player and print
        b_roll = Dice_Roll()+Dice_Roll()+Dice_Roll()+Dice_Roll()
        print("Black rolled: "+str(b_roll))
        print("")

        #Compare and decide who goes first
        if (w_roll>b_roll):
            print("White Goes First")
            player = 0
            found = True
            
        elif(b_roll>w_roll):
            print("Black Goes First")
            player = 1
            found = True

        #If its a draw then go again
        else:
            print("Draw, reroll")
            found = False

    #Return the number of the player who's going first
    return player

#Subroutine to initialise the counter positions in the off_board arrays
def Init_Counter_Positions(board, off_board, counters, pos_map):
    #Loop over the counters
    for i in range(14):
        #initialise the start row of the off_board array with the counters
        off_board[(i%7)+1, math.floor(i/7.0)].counter = i
        
            
            
def Find_Valid_Moves(counters, board, pos_map, player, roll):

    move_mask = np.zeros((7), dtype=int)
    if (roll==0):
        return move_mask
    
    for i in range(0+7*player, 7+7*player):
        check_pos = counters[i].position + roll
        if (check_pos>15):
            move_mask[i-7*player] = 0
            continue

        ind_1 = pos_map[0, check_pos, player]
        ind_2 = pos_map[1, check_pos, player]

        target_counter = board[ind_1, ind_2].counter

        if (target_counter==-1):
            move_mask[i-7*player] = 1
        elif ((ind_1==3)and(ind_2==1)and(target_counter!=-1)):
            move_mask[i-7*player] = 0

        elif (math.floor(target_counter/7.0)==player):
            move_mask[i-7*player] = 0
        else:
            move_mask[i-7*player] = 1

    return move_mask



def Move(counters, roll, player, move_mask, pos_map, turn, score):

    if (np.all(move_mask[:] == 0)):
        print("No valid moves", end='')
        input()
        return turn+1, score
    
    valid_move = False

    while (valid_move==False):
        if (player == 0):
            print("White moves piece ", end='')
        else:
            print("Black moves piece ", end='')
                
        index = int(input())-1
        count_ind = index+7*player
        print("")

        if (move_mask[index]==0):
            print("Invalid Move! Try again")
            valid_move = False
        else:
            valid_move = True

    if (counters[count_ind].position==0):
        off_board[index+1, player].counter = -1
    else:
        ind_1 = pos_map[0, counters[count_ind].position, player]
        ind_2 = pos_map[1, counters[count_ind].position, player]

        board[ind_1, ind_2].counter = -1
        

    counters[count_ind].position += roll

    if (counters[index+7*player].position==15):
        off_board[index+9, player].counter = count_ind
        score[player] +=1
    else:
        ind_1 = pos_map[0, counters[count_ind].position, player]
        ind_2 = pos_map[1, counters[count_ind].position, player]

        if (board[ind_1, ind_2].counter!=-1):
            capture(counters, board[ind_1, ind_2].counter, off_board)
        
        board[ind_1, ind_2].counter = count_ind

        if (board[ind_1, ind_2].text == "++"):
            return turn, score
        
    return turn+1, score


def capture(counters, counter_ind, off_board):
    counters[counter_ind].position = 0
    off_board[(counter_ind%7)+1, math.floor(counter_ind/7.0)].counter = counter_ind

            
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

Init_Counter_Positions(board, off_board, counters, pos_map)


random.seed()

turn = -1
    
score = np.zeros((2), dtype = int)

    
while ((score[0]<7) and (score[1]<7)):
    os.system('cls||clear')
    if (turn<1):
        turn = Who_Goes_First()
        
    player = turn%2
    
    roll = Dice_Roll()+Dice_Roll()+Dice_Roll()+Dice_Roll()
    move_mask = np.zeros((7), dtype = int)
    move_mask = Find_Valid_Moves(counters, board, pos_map, player, roll)
    
    
    Print_Board(board, off_board, counters, roll, player, move_mask)

    turn, score = Move(counters, roll, player, move_mask, pos_map, turn, score)

if (score[0]==7):
    print("White wins")
elif (score[1]==7):
    print("White wins")
