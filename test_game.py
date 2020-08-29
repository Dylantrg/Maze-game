from game import Game
from player import Player

def test_game():
    game = Game('board_test_game.txt')
    game.player.row = 2
    game.player.col = 2 

    game_edge_case = Game('board_weird.txt')
    game_edge_case.player.row = 0
    game_edge_case.player.col = 1



    #TEST game_move
    """
    Test the return of the step method of each Cell class and the return of move method of Player class. 
    """
    #POSITIVE CASES
    assert game.game_move('w') == ("Thank the Honourable Furious Forest, you've found a bucket of water!"+"\n",0) , "Test case failed"
    assert game.player.row == 1,"Test case failed"   #Test the player move() function. 
    assert game.player.col == 2, "Test case failed"
    assert game.player.num_water_buckets == 1, "Test failed" #Test the step method of Water class


    #NEGATIVE TEST CASES
    assert game.game_move('a1') == ('Please enter a valid move (w, a, s, d, e, q).'+'\n',0), "Test case failed"
    assert game.game_move('') == ('Please enter a valid move (w, a, s, d, e, q).'+'\n',0), "Test case failed"


    #EDGE TEST CASES
    assert game_edge_case.game_move('w') == ("You walked into a wall. Oof!"+"\n",0) , "Test case failed"
    assert game_edge_case.player.row == 0, "Test case failed"  #Test the step function of Wall Cell 
    assert game_edge_case.player.col == 1, "Test case failed"

    



    #TEST print_step function , no negative test case because the bad input is tested above 
    #POSITIVE CASES
    assert game.print_step(['d','a','e','s','w']) == 'd, a, e, s, w', "Test case failed"
    assert game.print_step(['A','S','W','D','S']) == 'a, s, w, d, s', "Test case failed"
    #EDGE CASES
    assert game.print_step(['d','a','e','A','W']) == 'd, a, e, a, w', "Test case failed"
    assert game.print_step(['d']) == 'd', "Test case failed"
    assert game.print_step([]) == '', "Test case failed"

    """
    Not testing the start_position function.
    """



def run_tests():
    test_game()

