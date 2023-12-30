
class Grid:
    # Grid class which is used to create a 6 rows x 7 columns Grid to play Connect Four

    def __init__(self):
        # define an instance variable .grid which holds a 2 dimensional list representing out 6x7 grid
        self.grid = [["_", "_", "_", "_", "_", "_", "_"],
                     ["_", "_", "_", "_", "_", "_", "_"],
                     ["_", "_", "_", "_", "_", "_", "_"],
                     ["_", "_", "_", "_", "_", "_", "_"],
                     ["_", "_", "_", "_", "_", "_", "_"],
                     ["_", "_", "_", "_", "_", "_", "_"]]

    def show_grid(self):
        # this class method is used to printout current grid

        # Opening message
        print("Here's the grid ->")

        # Looping through each list of the 2-d list
        for row in self.grid:

            # Looping through each element of current list
            for cell in row:

                # Printing out current element with formatted print statement to make the grid look more presentable
                print(cell + "|", end="")

            # empty print statement to move the cursor to a newline every an internal list is completely looped through
            print("")

    def modify_grid(self, col_num, symbol):
        # this class method is used to modify a cell of grid with the symbol that is passed in.
        # this method takes a column number, iterates from the bottom of the grid and finds the 
        # first empty cell and replaces "_" with the symbol passed as an argument
         
         # looping through each internal list in reverse order
        for row in self.grid[::-1]:

            # conditinal to check if the element in the column passed is empty, if yes then replace it with the symbol
            # and break out of the loop
            if row[col_num - 1] == "_":
                row[col_num - 1] = symbol
                break

    def check_for_win(self, symbol):
        # this class method is used to iterate over the whole grid, check if the passed symbol inside it forms a match
        # if yes then this method returns True, else None

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
    # this class represents a player. Takes in a name and has methods to get player symbol and to insert a symbol in the required column
    
    def __init__(self, name):
        # defines instance variables with unique name and an empty .symbol
        self.name = name
        self.symbol = ""
    
    def get_symbol(self, other_player):
        # loops untill, user gives an appropriate symbol and assigns other players symbol according to it too

        while True:
            player_input = input("{}, choose your mark to represent your ball on the grid (Either 'X' or 'O'): ".format(self.name)).capitalize()
            if player_input not in ['X', 'O']:
                print("Invalid Input!")
                continue
            break
        self.symbol = player_input

        # Assigning other_player's symbol
        if self.symbol == "X":
            other_player.symbol = "O"
        else:
            other_player.symbol = "X"

        # printing out a confirmation statement
        print("{} gets {}".format(other_player.name, other_player.symbol))
    
    def insert_symbol(self, grid:Grid):
        # this method is used to insert player's symbol into the passed grid

        # loops until it gets a valid column number, then inserts player symbol inside grid at that specific place
        while True:
            col_number = int(input("{} enter the column, where you'ld like to insert your ball (1-7): ".format(self.name)))

            if col_number not in [1, 2, 3, 4, 5, 6, 7]:
                print("Invalid Input!")
                continue

            print("Inserting value!")
            grid.modify_grid(col_number, self.symbol)
            break

def play_connect_four():
    # This function is used to play the game
    # Consists of all the tasks required to play the game in sequence
    
    # Welcome message, and getting name input of players
    print("Welcome to Connect-Four Game!")
    player_1_name = input("Please enter your name Player 1: ")
    player_2_name = input("Please enter your name Player 2: ")

    # Initializing player and grid objects
    player1 = Player(player_1_name)
    player2 = Player(player_2_name)
    my_grid = Grid()

    # Getting and assigning respective player symbols
    player1.get_symbol(player2)

    # printing the grid at the begininning to provide an idea how it looks to the player
    my_grid.show_grid()

    # Informing who plays first
    print("{} will go first!".format(player1.name))

    # Variable used to break the loop when there is a match found
    match_found = False

    while True:

        # inserting player1's symbol on grid
        player1.insert_symbol(my_grid)

        # checking if there is a match
        match_found = my_grid.check_for_win(player1.symbol)

        # displaying the grid
        my_grid.show_grid()

        # If match is found, print closing message and exit out of the program
        if match_found:
            print("Congratulations! {} you WON!!!".format(player1.name))
            break
        
        # inserting player2's symbol on grid
        player2.insert_symbol(my_grid)

        # checking if there is a match
        match_found = my_grid.check_for_win(player2.symbol)

        # displaying the grid
        my_grid.show_grid()

        # If match is found, print closing message and exit out of the program
        if match_found:
            print("Congratulations! {} you WON!!!".format(player1.name))
            break

# Calling main function to start the game
play_connect_four()
