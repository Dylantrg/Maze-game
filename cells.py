class Start:
    def __init__(self):
        self.display = 'X'

    def display(self):
        return self.display

    def step(self, game):
        return '',0
    


class End:
    def __init__(self):
        self.display = 'Y'

    def display(self):
        return self.display

    def step(self, game):
        lin =''
        if len(game.move_made) ==1:
            lin=''
        else:
            lin='s'
        return "\n"+"You conquer the treacherous maze set up by the Fire Nation "\
            "and reclaim the Honourable Furious Forest Throne, " \
            "restoring your hometown back to its former glory of rainbow and sunshine!"\
            " Peace reigns over the lands."+"\n" +"\n"+\
            "You made {} move{}.".format(len(game.move_made),lin)+"\n" + \
            "Your move{}: {}".format(lin, game.print_step(game.move_made))+"\n"+"\n"+\
            "====================="+"\n" +\
            "====== YOU WIN! ====="+"\n" +\
            "=====================".replace('\n', ""), 1



class Air:
    def __init__(self):
        self.display = ' '
    
    def display(self):
        return self.display

    def step(self, game):
        return '', 0
    


class Wall:  
    def __init__(self):
        self.display = '*' 
    
    def display(self):
        return self.display

    def step(self, game):
        game.move_made.pop()
        game.player.row = game.prev_row
        game.player.col = game.prev_col
        return "You walked into a wall. Oof!"+"\n",0


class Fire:  
    def __init__(self):
        self.display = 'F'

    def display(self):
        return self.display

    def step(self, game):
        game.grid[game.player.row][game.player.col] = Air()
        if game.player.num_water_buckets > 0:
            game.player.num_water_buckets -=1
            return "With your strong acorn arms, you throw a water bucket at the fire. "\
                   "You acorn roll your way through the extinguished flames!"+"\n",0
        if game.player.num_water_buckets == 0:
            lin =''
            if len(game.move_made) ==1:
                lin=''
            else:
                lin='s'

            return "\n"+"You step into the fires and watch your dreams disappear :(."+"\n"+"\n"\
                   "The Fire Nation triumphs! The Honourable Furious Forest is reduced to a pile of ash "\
                   "and is scattered to the winds by the next storm... You have been roasted."+"\n" +"\n"\
                   "You made {} move{}.".format(len(game.move_made),lin)+"\n"+\
                   "Your move{}: {}".format(lin, game.print_step(game.move_made))+"\n"+"\n"\
                   "====================="+"\n" +\
                   '===== GAME OVER ====='+"\n" + \
                   '====================='.rstrip("\n"), 1
                   
        
class Water:
    def __init__(self):
        self.display = 'W'

    def display(self):
        return self.display

    def step(self, game):
        game.grid[game.player.row][game.player.col] = Air()
        game.player.num_water_buckets +=1
        return "Thank the Honourable Furious Forest, you've found a bucket of water!"+"\n",0
    
        

class Teleport: #CHECK THE TELEPORT PAD 
    def __init__(self, display):
        self.display = display
        self.partner_pos =[]     #[x1, y1, x2, y2]

    def step(self, game):
        row = 0
        col = 0
        while row < len(game.grid): # find the location of other pad
            col = 0
            while col<len(game.grid[row]):
                if game.grid[row][col].display == self.display:
                    self.partner_pos.append(row)
                    self.partner_pos.append(col)
                col += 1
            row += 1
        if game.player.row == self.partner_pos[2] and game.player.col == self.partner_pos[3]:
            game.player.row = self.partner_pos[0]
            game.player.col = self.partner_pos[1]

        elif game.player.row == self.partner_pos[0] and game.player.col == self.partner_pos[1]:
            game.player.row = self.partner_pos[2]
            game.player.col = self.partner_pos[3]
        game.grid[game.position[0]][game.position[1]] = Start()
        return 'Whoosh! The magical gates break Physics as we know it '\
               'and opens a wormhole through space and time.'+"\n",0
    
    def display(self):
        return self.display
    

