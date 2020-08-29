from game import Game
from grid import grid_to_string
import os
import sys

key =['a', 's', 'd', 'w', 'e', 'q', 'A', 'S', 'D', 'W', 'E', 'Q']

if not len(sys.argv) == 2:
    print('Usage: python3 run.py <filename> [play]')
    exit()

game = Game(sys.argv[1])
print(grid_to_string(game.grid, game.player))  
while True:       
    string = input('Input a move: ')
    a = game.game_move(string)
    if string == 'q' or string =='Q':
        pass
    else:
        print(grid_to_string(game.grid, game.player))

     #Engine to exit the game , the step cell return a list. 1st element is string and other is a number
     # 1 or 0, if 1 exit the game, else the game keep updating   
    if a[0] == '':
        pass
    else:
        print(a[0])
    if ( a[1] == 1):
        exit()
    else:
        pass
    











