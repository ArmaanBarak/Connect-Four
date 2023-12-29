
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

my_grid = Grid()

# testing for check_for_win() method
my_grid.modify_grid(3, "X")
my_grid.modify_grid(4, "X")
my_grid.modify_grid(2, "X")
my_grid.modify_grid(5, "X")
my_grid.show_grid()
# should print True
print(my_grid.check_for_win("X"))