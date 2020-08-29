from grid import grid_to_string
from player import Player 
from game_parser import parse , read_lines

def test_grid():
    player_1 = Player(2,2)
    player_2 = Player(0,1)
    player_2.num_water_buckets = 3
    player_3 = Player(0,2)
    player_4 = Player(10,10)

    #POSITIVE CASE
    assert grid_to_string(read_lines('board_positive_case_1.txt'), player_1 ) == '*X**'+'\n'+\
                                                                                 '*1W*'+'\n'+\
                                                                                 '*1A*'+'\n'+\
                                                                                 '*YF*'+'\n'+'\n'+\
                                                                                 'You have 0 water buckets.'+'\n', 'Test case failed'


    assert grid_to_string(read_lines('board_positive_case_1.txt'), player_2 ) == '*A**'+'\n'+\
                                                                                 '*1W*'+'\n'+\
                                                                                 '*1 *'+'\n'+\
                                                                                 '*YF*'+'\n'+'\n'+\
                                                                                 'You have 3 water buckets.'+'\n', 'Test case failed'

                                                        
    #NEGATIVE CASES
    try:
        grid_to_string(read_lines('board_one_line.txt'), player_2)
    except ValueError as e:
        assert str(e) == 'This is not a maze!', 'Test case failed'

    try:
        grid_to_string(read_lines('board_positive_case_1.txt'), player_4)
    except ValueError as e:
        assert str(e) == 'Player must stay inside the maze!', 'Test case failed'
    

    #EDGE CASES
    try:
        #Player is at the corner of the board, where a Wall cell is missing. Consider as outside the maze
        grid_to_string(read_lines('board_positive_case.txt'), player_3 )
    except ValueError as e:
        assert str(e) == 'Player must stay inside the maze!', 'Test case failed'
    
    assert grid_to_string(read_lines('board_packed.txt'), player_1 ) == '***X**'+'\n'+\
                                                                        '*F1WF*'+'\n'+\
                                                                        '*1AW2*'+'\n'+\
                                                                        '**Y***'+'\n'+'\n'+\
                                                                        'You have 0 water buckets.'+'\n', 'Test case failed'
        

        

def run_tests():
    test_grid()

