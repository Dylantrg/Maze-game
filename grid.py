from cells import (
    Start,
    End,
    Air,
    Wall,
    Fire,
    Water,
    Teleport
)
from game_parser import parse, read_lines
from player import Player
def grid_to_string(grid, player):
    string=''
    if player.row < 0 or player.row > len(grid) or player.col < -1 or player.col == len(grid[0]): 
        raise ValueError ("Player must stay inside the maze!")
    for i, line in enumerate(grid):
        for j, char in enumerate(line):
            if i == player.row and j == player.col:
                string += player.display
            else:
                string += char.display
        string += '\n'
    if (player.num_water_buckets == 1 ):
        return string +'\n'+ 'You have {} water bucket.'.format(player.num_water_buckets)+'\n' 
    else:
        return string +'\n'+ 'You have {} water buckets.'.format(player.num_water_buckets)+'\n'

    

    """Turns a grid and player into a string

    Arguments:
        grid -- list of list of Cells
        player -- a Player with water buckets

    Returns:
        string: A string representation of the grid and player.
    """






