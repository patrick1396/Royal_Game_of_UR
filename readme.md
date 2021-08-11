The Royal Game of Ur

The Royal Game of Ur was a game played throughout Mesopotamia during the early third millennium BCE, named for the fact that boards were discovered in a royal cemetary in the Summarian city of Ur.

The board is made of 20 squares given in the following arrangement, where oo is a normal square and ++ is a rosette

++ oo oo oo&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;++ oo\
oo oo oo ++ oo oo oo oo\
++ oo oo oo&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;++ oo


Each player has 7 pieces that start off the board. The game is a race and players take it in turns to roll a set of dice and move their pieces onto and then off of the board. The first player to get all their pieces off the board is the winner.

The dice are four sided and can give either a 1 or a 0 with equal probability, the result of the four dice are then summed to give the total number of squares a piece can be moved.

Pieces are moved along in the direction of the arrows where S and F show the start and finish

| <--------------- S&nbsp;&nbsp;&nbsp;F <------\
v ++ oo oo oo&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;++ oo ^\
------------------------> |\
&nbsp;&nbsp;oo oo oo ++ oo oo oo oo \
------------------------> |  
^ ++ oo oo oo&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;++ oo v\
| <--------------- S&nbsp;&nbsp;&nbsp;F <------\

For both sides, the first 4 and final 2 squares are seperate, these are safe squares where your piece can't be taken.
The central 8 squares are shared, pieces of the opposing player can be captured here and sent back to the start by landing on them.
The rosettes are special squares that allow the current player to roll again, also the rosette on the central row protects a piece from being captured.

To play this download the Royal_Game_of_Ur.py file and run using python 3. It requries the numpy, os, random and math libraries to run.

At the start, players roll dice to decide who goes first, this is done automatically in this game.
During play the board will look something like this


S: b1 b2 b3 b4 b5 b6 b7 F: __ __ __ __ __ __ __ \

++ oo oo oo&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;++ oo \
oo oo oo ++ oo oo oo oo \
++ oo oo oo&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;++ oo 

S: W1 W2 W3 W4 W5 W6 W7 F: __ __ __ __ __ __ __ 

White rolled: 3\
White moves piece\

It is white's turn, the upper case letters indicate which of their pieces are available for movement. A piece is moved by typing its number and pressing enter. Entering 1 here would then give

S: B1 B2 B3 B4 B5 B6 B7 F: __ __ __ __ __ __ __ \

++ oo oo oo&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;++ oo \
oo oo oo ++ oo oo oo oo \
++ w1 oo oo&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;++ oo 

S: __ w2 w3 w4 w5 w6 w7 F: __ __ __ __ __ __ __ \

Black rolled: 3\
Black moves piece\


Enjoy the game and let me know if you encounter any bugs


