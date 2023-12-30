
class Grid:

    def __init__(self):
        self.grid = [["_", "_", "_", "_", "_", "_", "_"],
                     ["_", "_", "_", "_", "_", "_", "_"],
                     ["_", "_", "_", "_", "_", "_", "_"],
                     ["_", "_", "_", "_", "_", "_", "_"],
                     ["_", "_", "_", "_", "_", "_", "_"],
                     ["_", "_", "_", "_", "_", "_", "_"]]

    def show_grid(self):
        for row in self.grid:

            for cell in row:
                print(cell + "|", end="")

            print("")

    def modify_grid(self, col_num, symbol):
        for row in self.grid[::-1]:
            if row[col_num - 1] == "_":
                row[col_num - 1] = symbol
                break

    def check_for_win(self, symbol):
        # horizontal 4-match check
        for row in self.grid[::-1]:
            if ((row[0] == symbol) and (row[1] == symbol) and (row[2] == symbol) and (row[3] == symbol)):
                return True
            elif ((row[1] == symbol) and (row[2] == symbol) and (row[3] == symbol) and (row[4] == symbol)):
                return True
            elif ((row[2] == symbol) and (row[3] == symbol) and (row[4] == symbol) and (row[5] == symbol)):
                return True
            elif ((row[3] == symbol) and (row[4] == symbol) and (row[5] == symbol) and (row[6] == symbol)):
                return True
        
        # vertical 4-match check
        for col_index in range(7):
            if ((self.grid[0][col_index] == symbol) and (self.grid[1][col_index] == symbol) and (self.grid[2][col_index] == symbol) and (self.grid[3][col_index] == symbol)):
                return True
            elif ((self.grid[1][col_index] == symbol) and (self.grid[2][col_index] == symbol) and (self.grid[3][col_index] == symbol) and (self.grid[4][col_index] == symbol)):
                return True
            elif ((self.grid[2][col_index] == symbol) and (self.grid[3][col_index] == symbol) and (self.grid[4][col_index] == symbol) and (self.grid[5][col_index] == symbol)):
                return True
        
        # diagnol check left to right
        for row_index in range(3):
            if ((self.grid[row_index][0] == symbol) and (self.grid[row_index + 1][1] == symbol) and (self.grid[row_index + 2][2] == symbol) and (self.grid[row_index + 3][3] == symbol)):
                return True
            elif ((self.grid[row_index][1] == symbol) and (self.grid[row_index + 1][2] == symbol) and (self.grid[row_index + 2][3] == symbol) and (self.grid[row_index + 3][4] == symbol)):
                return True
            elif ((self.grid[row_index][2] == symbol) and (self.grid[row_index + 1][3] == symbol) and (self.grid[row_index + 2][4] == symbol) and (self.grid[row_index + 3][5] == symbol)):
                return True
            elif ((self.grid[row_index][3] == symbol) and (self.grid[row_index + 1][4] == symbol) and (self.grid[row_index + 2][5] == symbol) and (self.grid[row_index + 3][6] == symbol)):
                return True
        
        # Diagnol 4-match check right to left
        for row_index in range(3):
            if ((self.grid[row_index][-1] == symbol) and (self.grid[row_index + 1][-2] == symbol) and (self.grid[row_index + 2][-3] == symbol) and (self.grid[row_index + 3][-4] == symbol)):
                return True
            elif ((self.grid[row_index][-2] == symbol) and (self.grid[row_index + 1][-3] == symbol) and (self.grid[row_index + 2][-4] == symbol) and (self.grid[row_index + 3][-5] == symbol)):
                return True
            elif ((self.grid[row_index][-3] == symbol) and (self.grid[row_index + 1][-4] == symbol) and (self.grid[row_index + 2][-5] == symbol) and (self.grid[row_index + 3][-6] == symbol)):
                return True
            elif ((self.grid[row_index][-4] == symbol) and (self.grid[row_index + 1][-5] == symbol) and (self.grid[row_index + 2][-6] == symbol) and (self.grid[row_index + 3][-7] == symbol)):
                return True
        

my_grid = Grid()

# testing for check_for_win() method
my_grid.modify_grid(6, "X")
my_grid.modify_grid(6, "O")
my_grid.modify_grid(6, "O")
my_grid.modify_grid(6, "X")
my_grid.modify_grid(5, "O")
my_grid.modify_grid(5, "O")
my_grid.modify_grid(5, "X")
my_grid.modify_grid(4, "O")
my_grid.modify_grid(4, "X")
my_grid.modify_grid(3, "X")
my_grid.show_grid()

# should print True
print(my_grid.check_for_win("X"))