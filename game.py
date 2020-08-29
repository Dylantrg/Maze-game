from game_parser import read_lines
from grid import grid_to_string
from player import Player
from cells import Start, End, Air, Fire, Water, Teleport, Wall
class Game:
    def __init__(self, filename):
        self.grid = read_lines(filename)
        self.position = self.start_position(self.grid)
        self.player = Player(self.position[0], self.position[1])
        self.move_made =[]
        self.prev_row = 0 
        self.prev_col = 0

    def game_move(self, move):
        key =['a', 's', 'd', 'w', 'e', 'q', 'A', 'S', 'D', 'W', 'E', 'Q']
        if move in key:
            if move == 'q' or move =='Q':
                return "\n"+"Bye!", 1
            elif move == 'e' or move == 'E':
                self.move_made.append(move)
                return self.grid[self.player.row][self.player.col].step(self)
            else:
                self.prev_row = self.player.row
                self.prev_col = self.player.col
                self.player.move(move)
                self.move_made.append(move)

                # WHEN THE PLAYER STEP OUT OF THE MAZE BOUND
                if self.player.row == -1 or self.player.row == len(self.grid) or self.player.col == -1 or self.player.col == len(self.grid[0]):
                    self.move_made.pop()
                    self.player.row = self.prev_row
                    self.player.col = self.prev_col
                    return 'You walked into a wall. Oof!'+"\n",0

                else:
                    return self.grid[self.player.row][self.player.col].step(self)
        else:
            return 'Please enter a valid move (w, a, s, d, e, q).'+'\n',0
                                                                              


    def start_position(self, grid):  #INITIAL POSITION OF PLAYER
        pos =[]
        i = 0
        while i < len(self.grid):
            j = 0
            while j < len(self.grid[i]):
                if type(self.grid[i][j]) == Start:
                    pos.append(i)
                    pos.append(j)
                j += 1
            i += 1
        return pos

    def print_step(self, ls):  #PRINT THE MOVE LIST IN LOWERCASE
        line =''
        i=0
        while i < len(ls):
            if i == len(ls)-1:
                line += ls[i].lower()
            else:
                line += '{}, '.format(ls[i].lower())
            i+=1
        return line
    
    
    





