from cells import (
    Start,
    End,
    Air,
    Wall,
    Fire,
    Water,
    Teleport
)

CELLS ={
    'X': Start, 
    'Y': End,
    '*': Wall,
    'W': Water,
    'F': Fire,  
    ' ': Air  
}   

def read_lines(filename):
    """Read in a file, process them using parse(),
    and return the contents as a list of list of cells."""
    try:
        grid =[]
        f = open(filename, 'r')
        while True:
            lin = f.readline()
            if lin =='':
                break
            grid.append(lin)
        grid = parse(grid)
        return grid
    except FileNotFoundError:
        print('{} does not exist!'.format(filename))
        exit()



def parse(lines):  
    countX =0
    countY =0 
    grid =[]
    teleport_pad ={}

    if len(lines) <= 1:
        raise ValueError ("This is not a maze!") 
    else:  
        for line in lines:
            line = line.strip()
            cell_line =[]
            for char in line:
                if char == 'X':
                    countX += 1
                if char == 'Y':
                    countY += 1
                try:
                    int(char)

                    if char == 0:  #0 is not a valid pad 
                        raise ValueError('0 is not a valid teleport pad.')


                    #If no error raise the char is a number, mean it is a teleport pad

                    cell = Teleport(char)
                    if char not in teleport_pad:
                        teleport_pad[char] = 1
                    else:
                        teleport_pad[char] += 1
                except:
                    if char not in CELLS:
                        raise ValueError('Bad letter in configuration file: {}.'.format(char))
                    cell = CELLS[char]()
                cell_line.append(cell)
            grid.append(cell_line)
        if countX != 1 and countY != 1:   #In case there are
            raise ValueError ('Expected 1 starting and 1 ending position, got {} starting positions and {} ending positions.'.format(countX, countY)) 
        elif  countX != 1:
            raise ValueError('Expected 1 starting position, got {}.'.format(countX))
        elif countY != 1:
            raise ValueError('Expected 1 ending position, got {}.'.format(countY))
        for (num, count) in teleport_pad.items():
            if count != 2:
                raise ValueError('Teleport pad {} does not have an exclusively matching pad.'.format(num))
        return grid
    






        
