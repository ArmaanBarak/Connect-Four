
class Grid:

    def __init__(self):
        self.grid = [["_", "_", "_", "_", "_", "_", "_"],
                     ["_", "_", "_", "_", "_", "_", "_"],
                     ["_", "_", "_", "_", "_", "_", "_"],
                     ["_", "_", "_", "_", "_", "_", "_"],
                     ["_", "_", "_", "_", "_", "_", "_"],
                     ["_", "_", "_", "_", "_", "_", "_"]]

    def show_grid(self):
        print("Here's the grid ->")
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
        
class Player:
    def __init__(self, name):
        self.name = name
        self.symbol = ""
    
    def get_symbol(self, other_player):
        while True:
            player_input = input("{}, choose your mark to represent your ball on the grid (Either 'X' or 'O'): ".format(self.name)).capitalize()
            if player_input not in ['X', 'O']:
                print("Invalid Input!")
                continue
            break
        self.symbol = player_input

        if self.symbol == "X":
            other_player.symbol = "O"
        else:
            other_player.symbol = "X"

        print("{} gets {}".format(other_player.name, other_player.symbol))
    
    def insert_symbol(self, grid:Grid):
        while True:
            col_number = int(input("{} enter the column, where you'ld like to insert your ball (1-7): ".format(self.name)))
            if col_number not in [1, 2, 3, 4, 5, 6, 7]:
                print("Invalid Input!")
                continue
            print("Inserting value!")
            grid.modify_grid(col_number, self.symbol)
            break


def play_connect_four():
    print("Welcome to Connect-Four Game!")
    player_1_name = input("Please enter your name Player 1: ")
    player_2_name = input("Please enter your name Player 2: ")

    player1 = Player(player_1_name)
    player2 = Player(player_2_name)
    my_grid = Grid()

    player1.get_symbol(player2)

    my_grid.show_grid()

    print("{} will go first!".format(player1.name))

    match_found = False

    while True:

        player1.insert_symbol(my_grid)

        match_found = my_grid.check_for_win(player1.symbol)
        my_grid.show_grid()

        if match_found:
            print("Congratulations! {} you WON!!!".format(player1.name))
            break

        player2.insert_symbol(my_grid)

        match_found = my_grid.check_for_win(player2.symbol)
        my_grid.show_grid()

        if match_found:
            print("Congratulations! {} you WON!!!".format(player1.name))
            break

play_connect_four()
