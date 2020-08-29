class Player:
    def __init__(self, row, col):
        self.display = 'A'
        self.num_water_buckets = 0
        self.row = row
        self.col = col

    def move(self, move):
        if move == 'w' or move =='W':
            self.row -= 1
        elif move == 'a' or move == 'A':
            self.col -= 1
        elif move == 's' or move =='S':
            self.row += 1
        elif move == 'd' or move == 'D':
            self.col += 1

    def num_water_buckets(self):
        return self.num_water_buckets

    def get_row(self):
        return self.row

    def get_col(self):
        return self.col

    def display(self):
        return self.display
        
    
