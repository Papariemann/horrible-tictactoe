# tictactoe
# player 1 has X
# player 2 has O
# there is a grid

# grid:

# stupid but I think it will work
grid_row1: str = " | | "
grid_row2: str = "-+-+-"
grid_row3: str = " | | "
grid_row4: str = "-+-+-"
grid_row5: str = " | | "

# storing them in an array for ease of use, I guess
grid: list = [list(grid_row1), list(grid_row2), list(grid_row3), list(grid_row4), list(grid_row5)]

# function to display the grid
def display_grid(row1, row2, row3, row4, row5):
    grid: list = [row1, row2, row3, row4, row5]  
    for row in grid:
        print(row) 

def get_move(grid):
    while True:
        try:
            move: str = input("Enter your move (row, col), where row and col are 1, 2, or 3: ") 1 -> 0, 2 -> 2, 3 -> 4
       
            # for parsing the coordinate inputs 
            row, col = map(int, move.split(","))
            if row in [1, 2, 3] and col in [1, 2, 3]:
                row = int(row) - 1
                col = int(col) - 1

                tempr = 2 * row
                tempc = 2 * col
                # convert to zero based index
                if grid[tempr][tempc] == " ":  
                    return row, col
                else: 
                    print("Cell already taken! Try again.")
            else:
                print("Invalid input. Please enter numbers between 1 and 3 included. ")

        except ValueError:
            print("Invalid input format. Please enter as 'row, col'.")

def check_win(grid):
    # checking rows:
    for i in [0, 1, 2]:
        temp = 2 * i
        if grid[temp][0] == grid[temp][2] == grid[temp][4] and grid[temp][0] != " ":
            return True

    # checking columns
    for i in [0, 1, 2]:
        temp = 2 * i
        if grid[0][temp] == grid[2][temp] == grid[4][temp] and grid[0][temp] != " ":
            return True

    # checking for diagonals
    if (grid[4][0] == grid[2][2] == grid[0][4] or grid[0][0] == grid[2][2] == grid[4][4]) and grid[2][2] != " ":
        return True


def check_draw(grid):
    if check_win(grid):
        return False
    else:
        for i in [0, 2, 4]:
            for j in [0, 2, 4]:
                if grid[i][j] == " ":
                    return False
        return True 

def main(row1, row2, row3, row4, row5):

    grid: list = [list(row1), list(row2), list(row3), list(row4), list(row5)]
    display_grid(row1, row2, row3, row4, row5)

    PLAYERS = ["X", "O"]
    turn = 0

    while True:

        current_player = PLAYERS[ turn % 2 ]
        print(f"Player { current_player }'s turn: ")

        coord_row, coord_col = get_move(grid)
        # now, we have to map row = 0 to grid_row1, row = 1 to grid_row 3, and row 2 to grid_row5
        # and map col = 1 to row[0], col = 2 to row[2] and col = 3 to row[4]
        # notice that if we grid_row(n) for some n is just grid_row(2 * row + 1)
        row_grid: int = 2 * (coord_row)
        column_grid: int = 2 * (coord_col)
        player_move = current_player

        grid[row_grid][column_grid] = player_move

        # converting the rows back to strings for displaying (since display_grid takes arguments of type str)
        display_rows = ["".join(row) for row in grid]
        # * is the python unpacking operator (display_rows is an array so it just does that for me, maybe don't forget to use it every now and then)
        display_grid(*display_rows)

        win_bool = check_win(grid)
        if win_bool:
            print(f"Player {current_player} has won!")
            print("Game over!")
            break

        draw_bool = check_draw(grid)
        if draw_bool:
            print("Draw! Game finished. ")
            break

        turn +=1 


main(grid_row1, grid_row2, grid_row3, grid_row4, grid_row5)



