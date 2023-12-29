
class Grid:

    def __init__(self):
        row = ["_" for i in range(7)]
        self.grid = [row for i in range(6)]


    def show_grid(self):
        for row in self.grid:

            for cell in row:
                print(cell + "|", end="")

            print("")


my_grid = Grid()

# testing show_grid() method
my_grid.show_grid()