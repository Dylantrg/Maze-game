from game_parser import parse


def test_parse():
    #POSITIVE CASES
    positive_case = parse(['*X*','* *','*Y*'])
    positive_case_1 = parse(['*X**','*1W*','*1 *','*YF*'])
    assert check(positive_case) == True, "Test case failed" 
    assert check(positive_case_1) == True, "Test case failed" 

    #NEGATIVE CASES
    try:
        #The maze is expected to have a rectangular shape
        negative_case_1 =['XY*']       
        test = check(negative_case_1)
    except ValueError as e:
        assert str(e) == "This is not a maze !", "Test case failed" 
        
    try:
        #Two starting positiona and three ending positions
        negative_case_2 = parse(['*X*','* *','*X*','YYY'])
        test = check(negative_case_2)
    except ValueError as e:
        assert str(e) == "Expected 1 starting and 1 ending position, got 2 starting positions and 3 ending positions.", "Test case failed" 

    try:
        # Teleport pad 0 is not a valid pad
        negative_case_2 = parse(['*X*','*0*','*0*','**Y'])
        test = check(negative_case_2)
    except ValueError as e:
        assert str(e) == "0 is not a valid teleport pad.", "Test case failed" 

    try:
        negative_case_3 = parse(['*X**','*  *','1134','*Y**'])
        test = check(negative_case_3)
    except ValueError as e:
        assert str(e) == "Teleport pad 3 does not have an exclusively matching pad.", "Test case failed" 
    

    #EDGE CASES
    edge_case = ['*X*************','*    W W     2*','*3*** **3**** *','* * WW*   1   *','*W**WFF2FFFFFF*','* 1********FFF*','*************Y*']
    edge_case_1 = parse(['*X**','*Y**'])
    assert check(edge_case) == True, "Test case failed"
    assert check(edge_case_1) == True, "Test case failed"


def check(ls):
    cell_type = []
    check = True 
    for line in ls:
        for char in line:
            if type(char) != str:
                check = True
    return check

def run_tests():
    test_parse()


