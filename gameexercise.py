"""
My implementation of the Conway's game of life in python

Ref: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

Rules
Any live cell with fewer than two live neighbours dies, as if by underpopulation.
Any live cell with two or three live neighbours lives on to the next generation.
Any live cell with more than three live neighbours dies, as if by overpopulation.
Any dead cell with three live neighbours becomes a live cell, as if by reproduction.

The game plan for this code is as follows:
Create a copy of the inputted board
loop through all the cells on the board
    determine whether they are alive or dead
    count the number of neighbours that are alive
    with the count apply the rules to know whether the current state stays the same or changes
    reflect any changes in the new board
return the new board
"""

# representation of the board
# list of 4 lists - sets could be used as well

# random initial state
# ths state will represent a generation

# variable to allow for situations when the board is larger than 4X4
cells_in_squares = 4  # it could be any number

# the state of the cell is represented by 0s and 1s

DEAD = 0
ALIVE = 1

# find cells that are alive cells that have 1 are alive
# cycle through each cell turning it on or off depending on the rules


def return_next_generation(bdlist):
    """ this function returns another list which represents the next generation after
    processing the original board"""

    """ Unit tests need to be carried out to ensure code doesnt fall over unexpectedly
    1. that the input passed in is a list
    2. that the input is of the required dimensions
    3. that the input values consist of only 0s and 1s - no alphabets, complex numbers etc
    
    The first test is done below but ideally this would have been done in a separate unit test
    file
    """
    # checking to see that the tight structure is passed in
    if type(bdlist) != list:
        raise TypeError("Input must be a list")

    #

    # copy the original board
    nextboard = bdlist.copy()

    # alivemsg = "{},{} is alive"
    # deadmsg = "{},{} is dead"
    # loop to find out the state of the cells
    for x in range(4):
        for y in range(4):
            ct = neighbours_alive(bdlist, x, y)
            nextboard[x][y] = applygamerules(bdlist[x][y], ct)
    return nextboard


def neighbours_alive(bd, x, y):
    """ return a count of neighbours alive
    we have a maximum of 8 cell surrounding each cell
    leftcell, rightcell, upcell, downcell, diagleftupcell, diagleftdowncell diagrightupcell diagrightdowncell
    """
    count = 0
    # print(x,y)
    # we need to allow for corner cells
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            # we are using this function because this function checks for existence of the cell
            ret = return_cell_state(bd, i, j)
            if ret == ALIVE:
                # we are only counting the cell that are alive
                count += 1
    # had to make this adjustment
    if return_cell_state(bd, x, y) == ALIVE:
        count -= 1
    return count


def return_cell_state(bd, x, y):
    """this function returns the state of the cell
    if it does not exist it returns -1
    we have to check to see that the cell exists. For example
    we cant have a cell with x or y value -1
    """
    if x < 0 or x > cells_in_squares-1 or y < 0 or y > cells_in_squares - 1:
        return -1
    else:
        # cell exists
        return bd[x][y]


def applygamerules(state, numberalive):
    """this function applies the game rules to the cell. It takes the current state of the cell and number
    of current cells that are ALIVE"""
    if state == ALIVE:
        if numberalive < 2:
            return DEAD
        elif numberalive == 2 or numberalive == 3:
            return ALIVE
        elif numberalive > 3:
            return DEAD
    else:
        # means the cell is dead
        if numberalive == 3:
            return ALIVE
        else:
            return DEAD


def list_board_status(bdlist):
    """This function is not used but was used for debugging purposes. It loops through all the
    cells on the board and show their status"""

    alivemsg = "{},{} is alive"
    deadmsg = "{},{} is dead"
    # loop to find out the state of the cells
    for x in range(4):
        for y in range(4):
            if bdlist[x][y] == ALIVE:
                print(alivemsg.format(x, y))
            else:
                print(deadmsg.format(x, y))


# carry out a run using the sample board
if __name__ == "__main__":
    # This function will print out the original board and the next generation after processing
    board = [[1, 0, 0, 0],
             [1, 0, 0, 1],
             [0, 1, 1, 0],
             [0, 0, 0, 1]]
    print("Original board is :", board)
    # define a counter for a loop
    x = 0
    # build a loop with the new generated board as input
    # original board is printed once but all all the new generations are printed
    for x in range(51):
        # x-1 iterations
        board = return_next_generation(board)
        print(board)
    print("End of simulation")
    """
    At this stage instead of just printing the newly generated board output it can 
    be connected to a plotting engine to show the changes. The board could be designed 
    like a chess board sized 4 x 4. One color for the dead cells and another for the cells are alive
    So in summary the outstanding work is as follows
    1. find a logical test on the board to end the simulations for example if the new board is the same as the 
        one that went in stop the loop and end the program
    2. Plot the board to produce a visual representation
    3. code a random starting board position 
    4. unit tests for the program logic
       
    """
