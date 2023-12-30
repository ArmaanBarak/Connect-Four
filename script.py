
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
        
class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol


if __name__ == "__main__":
    print("Welcome to Connect-Four Game!")
    player_1_name = input("Please enter your name Player 1: ")
    player_2_name = input("Please enter your name Player 2: ")

    while True:
        player_1_symbol = input("{}, Choose your mark to represent your ball on the grid (Either 'X' or 'O'): ".format(player_1_name))
        if player_1_symbol.capitalize() not in ['X', 'O']:
            print("Invalid Input!")
            continue
        break

    player_1_symbol = player_1_symbol.capitalize()

    if player_1_symbol == "X":
        player_2_symbol = "O"
    else:
        player_2_symbol = "X"

    player1 = Player(player_1_name, player_1_symbol)
    player2 = Player(player_2_name, player_2_symbol)
    my_grid = Grid()

    print("Here's the grid ->")
    my_grid.show_grid()

    print("{} will go first!".format(player1.name))

    match_found = False

    while True:

        while True:
            col_number = int(input("{} enter the column, where you'ld like to insert your ball (1-7): ".format(player1.name)))
            if col_number not in [1, 2, 3, 4, 5, 6, 7]:
                print("Invalid Input!")
                continue
            print("Inserting value!")
            my_grid.modify_grid(col_number, player1.symbol)
            break

        match_found = my_grid.check_for_win(player1.symbol)
        my_grid.show_grid()

        if match_found:
            print("Congratulations! {} you WON!!!".format(player1.name))
            break

        while True:
            col_number = int(input("{} enter the column, where you'ld like to insert your ball (1-7): ".format(player2.name)))
            if col_number not in [1, 2, 3, 4, 5, 6, 7]:
                print("Invalid Input!")
                continue
            print("Inserting value!")
            my_grid.modify_grid(col_number, player2.symbol)
            break

        match_found = my_grid.check_for_win(player1.symbol)
        my_grid.show_grid()

        if match_found:
            print("Congratulations! {} you WON!!!".format(player1.name))
            break
