
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

my_grid = Grid()

# testing modify_grid() method
# adding "X" in first empty space of column 3 from bottom
my_grid.modify_grid(3, "X")
my_grid.show_grid()