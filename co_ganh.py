from copy import deepcopy
import random
from datetime import datetime

""" Check top position """
def Top(num):
    return num == 4

""" Check botton postion """
def Bottom(num):
    return num == 0

""" Check left position """
def Left(num):
    return num == 0

""" Check right position """
def Right(num):
    return num == 4

""" Print state"""
def print_state(state):
    for i in [4, 3, 2, 1, 0]:
        print(i, ":", end=" ")
        for j in range(5):
            print(state[i][j], end=" ")
        print()
    print("   ", 0, 1, 2, 3, 4)
    print("")


# ======================== Class Player =======================================
class Player:
    # student do not allow to change two first functions
    def __init__(self, str_name):
        self.str = str_name
    
    def __str__(self):
        return self.str

    # get enermy metood
    def enermy(self):
        if self.str == "r":
            return "b"
        else:
            return "r"
    
    # Evaluate value
    Value = 0
    
    # Latest map
    Last_state = 0

    # Player move
    player_move = 0

    """ Evaluated function of state"""
    def evaluated_function(self, state):
        count = 0
        for row in [4,3,2,1,0]:
            for col in range(5):
                if self.str == state[row][col]:
                    count+=1
        return count

    """ Move chess to clear position """
    def move(self, state, current, new):
        cur_x = current[0]
        cur_y = current[1]
        new_x = new[0]
        new_y = new[1]
        state[cur_x][cur_y] = "."
        state[new_x][new_y] = self.str
        self.change_color(state, new)
        self.EvaluateAndSelect(current, new, state)


    """One for two"""
    def OneForTwo (self, state, position):
        # Check and change the chessman color 
        # ? self.str ?
        first_chess_row = position[0][0]
        first_chess_col = position[0][1]
        second_chess_row = position[1][0] 
        second_chess_col = position[1][1]
        if state[first_chess_row][first_chess_col] == self.enermy() and state[second_chess_row][second_chess_col] == self.enermy():
            state[first_chess_row][first_chess_col] = self.str
            state[second_chess_row][second_chess_col] = self.str
            return True
        else:
            return False

    """Two for one"""
    def TwoForOne (self, state, position):
        # Check and change the chessman color
        # self.str self.enermy() ?
            return True 
    
    """Find in stack for all near chessman"""
    def FindInStack (self,state, stack):
        # if new chessman near current chessman 
        # we should check if chessman already in stack
        if state in stack:
            return True
        else:
            return False

    """ Evaluate and select """
    def EvaluateAndSelect(self, current, new, state):
        newValue = self.evaluated_function(state)
        if newValue > self.Value:
            self.Value = newValue
            self.Last_state = state 
            self.player_move = [current, new]
        elif newValue == self.Value:
            random.seed(datetime.now())
            if random.randint(0,100) < 50:
                self.Value = newValue
                self.Last_state = state
                self.player_move = [current, new]

    """ Change color """
    def change_color(self, state, position):
        row = position[0]
        col = position[1]
        if (row + col) % 2 == 0:
            # Chessman in Top row
            if Top(row):
                # Position in top row
                # Middle
                if col == 2:
                    if state[row][col - 1] == self.enermy():
                        self.OneForTwo(state, [[row, col - 1], [row, col + 1]])
                    if state[row][col + 1] == self.enermy():
                        self.TwoForOne(state, [row, col + 1])
                    elif state[row - 1][col + 1] == self.enermy():
                        self.TwoForOne(state, [row - 1, col + 1])
                    if state[row][col - 1] == self.enermy():
                        self.TwoForOne(state, [row, col - 1])
                    elif state[row -1][col - 1] == self.enermy():
                        self.TwoForOne(state, [row - 1, col - 1])
                # Left
                elif Left(col):
                    if state[row][col + 1] == self.enermy():
                        self.TwoForOne(state, [row, col + 1])
                    elif state[row - 1][col + 1] == self.enermy():
                        self.TwoForOne(state, [row - 1, col + 1])
                # Right
                elif Right(col):
                    if state[row][col - 1] == self.enermy():
                        self.TwoForOne(state, [row, col - 1])
                    elif state[row -1][col - 1] == self.enermy():
                        self.TwoForOne(state, [row - 1, col - 1])
                # row under top row 
                if state[row - 1][col] == self.enermy():
                    self.TwoForOne(state, [row - 1, col])                    
            # Chessman in Bottom row
            elif Bottom(row):
                # Position in Bottom row
                # Middle
                if col == 2:
                    if state[row][col - 1] == self.enermy():
                        self.OneForTwo(state, [[row, col - 1], [row, col + 1]])
                    if state[row][col + 1] == self.enermy():
                        self.TwoForOne(state, [row, col + 1])
                    elif state[row + 1][col + 1] == self.enermy():
                        self.TwoForOne(state, [row - 1, col + 1])
                    if state[row][col - 1] == self.enermy():
                        self.TwoForOne(state, [row, col - 1])
                    elif state[row + 1][col - 1] == self.enermy():
                        self.TwoForOne(state, [row - 1, col - 1])
                # Left
                elif Left(col):
                    if state[row][col + 1] == self.enermy():
                        self.TwoForOne(state, [row, col + 1])
                    elif state[row + 1][col + 1] == self.enermy():
                        self.TwoForOne(state, [row - 1, col + 1])
                # Right
                elif Right(col):
                    if state[row][col - 1] == self.enermy():
                        self.TwoForOne(state, [row, col - 1])
                    elif state[row + 1][col - 1] == self.enermy():
                        self.TwoForOne(state, [row - 1, col - 1])
                # row upper Bottom row 
                if state[row + 1][col] == self.enermy():
                    self.TwoForOne(state, [row - 1, col])                    
            # Chessman in Left row (except in corner) 
            # Only row = 2 is match this condition
            elif Left(col):
                if state[row + 1][col] == self.enermy():
                    self.OneForTwo(state, [[row + 1, col], [row - 1, col]])
                if state[row + 1][col] == self.enermy():
                    self.TwoForOne(state, [row + 1, col])
                elif state[row + 1][col + 1] == self.enermy():
                    self.TwoForOne(state, [row + 1, col + 1]) 
                if state[row - 1][col] == self.enermy():
                    self.TwoForOne(state, [row - 1, col])
                elif state[row -1][col + 1] == self.enermy():
                    self.TwoForOne(state, [row - 1, col + 1])
                if state[row][col + 1] == self.enermy():
                    self.TwoForOne(state, [row, col + 1])
            elif Right(col):
                if state[row + 1][col] == self.enermy():
                    self.OneForTwo(state, [[row + 1, col], [row - 1, col]])
                if state[row + 1][col] == self.enermy():
                    self.TwoForOne(state, [row + 1, col])
                elif state[row + 1][col - 1] == self.enermy():
                    self.TwoForOne(state, [row + 1, col - 1]) 
                if state[row - 1][col] == self.enermy():
                    self.TwoForOne(state, [row - 1, col])
                elif state[row -1][col - 1] == self.enermy():
                    self.TwoForOne(state, [row - 1, col - 1])
                if state[row][col - 1] == self.enermy():
                    self.TwoForOne(state, [row, col - 1])
            else:
                if state[row + 1][col] == self.enermy():
                    self.OneForTwo(state, [[row + 1, col], [row - 1, col]])
                elif state[row + 1][col] == self.enermy():
                    self.TwoForOne(state, [row + 1, col])
                elif state[row - 1][col] == self.enermy():
                    self.TwoForOne(state,[row - 1, col])
                if state[row + 1][col + 1] == self.enermy():
                    self.OneForTwo(state, [[row + 1, col + 1], [row - 1, col - 1]])
                elif state[row + 1][col + 1] == self.enermy():
                    self.TwoForOne(state, [row + 1, col + 1])
                elif state[row - 1][col - 1] == self.enermy():
                    self.TwoForOne(state, [row - 1, col - 1])
                if state[row][col + 1] == self.enermy():
                    self.OneForTwo(state, [[row, col + 1], [row, col - 1]])
                elif state[row][col + 1] == self.enermy():
                    self.TwoForOne(state, [row, col + 1])
                elif state[row][col - 1] == self.enermy():
                    self.TwoForOne(state, [row, col - 1])
                if state[row - 1][col + 1] == self.enermy():
                    self.OneForTwo(state, [[row - 1, col + 1], [row + 1, col - 1]])
                elif state[row - 1][col + 1] == self.enermy():
                    self.TwoForOne(state, [row - 1, col + 1])
                elif state[row + 1][col - 1] == self.enermy():
                    self.TwoForOne(state, [row + 1, col - 1])
        else:
            # Chessman in Top row
            if Top(row):
                # Position in top row
                if state[row][col - 1] == self.enermy():
                    self.OneForTwo(state, [[row, col - 1], [row, col + 1]])
                if state[row][col + 1] == self.enermy():
                    self.TwoForOne(state, [row, col + 1])
                if state[row][col - 1] == self.enermy():
                    self.TwoForOne(state, [row, col - 1])
               # row under top row 
                if state[row - 1][col] == self.enermy():
                    self.TwoForOne(state, [row - 1, col])                    
            # Chessman in Bottom row
            elif Bottom(row):
                # Position in Bottom row
                if state[row][col - 1] == self.enermy():
                    self.OneForTwo(state, [[row, col - 1], [row, col + 1]])
                if state[row][col + 1] == self.enermy():
                    self.TwoForOne(state, [row, col + 1])
                if state[row][col - 1] == self.enermy():
                    self.TwoForOne(state, [row, col - 1])
                # row upper Bottom row 
                if state[row + 1][col] == self.enermy():
                    self.TwoForOne(state, [row - 1, col])                    
            # Left row
            elif Left(col):
                if state[row + 1][col] == self.enermy():
                    self.OneForTwo(state, [[row + 1, col], [row - 1, col]])
                if state[row + 1][col] == self.enermy():
                    self.TwoForOne(state, [row + 1, col])
                if state[row][col + 1] == self.enermy():
                    self.TwoForOne(state, [row, col + 1])
                if state[row - 1][col] == self.enermy():
                    self.TwoForOne(state, [row - 1, col])
            elif Right(col):
                if state[row + 1][col] == self.enermy():
                    self.OneForTwo(state, [[row + 1, col], [row - 1, col]])
                if state[row + 1][col] == self.enermy():
                    self.TwoForOne(state, [row + 1, col])
                if state[row - 1][col] == self.enermy():
                    self.TwoForOne(state, [row - 1, col])
                if state[row][col - 1] == self.enermy():
                    self.TwoForOne(state, [row, col - 1])
            else:
                if state[row + 1][col] == self.enermy():
                    self.OneForTwo(state, [[row + 1, col], [row - 1, col]])
                elif state[row + 1][col] == self.enermy():
                    self.TwoForOne(state, [row + 1, col])
                elif state[row - 1][col] == self.enermy():
                    self.TwoForOne(state,[row - 1, col])
                if state[row][col + 1] == self.enermy():
                    self.OneForTwo(state, [[row, col + 1], [row, col - 1]])
                elif state[row][col + 1] == self.enermy():
                    self.TwoForOne(state, [row, col + 1])
                elif state[row][col - 1] == self.enermy():
                    self.TwoForOne(state, [row, col - 1])

    def openStep(self, state):
        enermy_row = -1
        enermy_col = -1 
        for row in [4,3,2,1,0]:
            for col in range(5):
                if self.Last_state[row][col] is not '.' and state[row][col] == '.':
                    enermy_row = row
                    enermy_col = col

        if enermy_row == -1:
            return False

        result = False
        row = enermy_row
        col = enermy_col
        if (row + col) % 2 == 0:
            # Chessman in Top row
            if Top(row):
                # Position in top row
                # Middle
                if col == 2:
                    if state[row][col - 1] == self.str:
                        self.player_move = [[row, col - 1], [enermy_row, enermy_col]]
                        result = True
                    elif state[row][col + 1] == self.str:
                        self.player_move = [[row, col + 1], [enermy_row, enermy_col]]
                        result = True
                    elif state[row - 1][col + 1] == self.str:
                        self.player_move = [[row - 1, col + 1], [enermy_row, enermy_col]]
                        result = True
                    elif state[row][col - 1] == self.str:
                        self.player_move = [[row, col - 1], [enermy_row, enermy_col]]
                        result = True
                    elif state[row - 1][col - 1] == self.str:
                        self.player_move = [[row - 1, col - 1], [enermy_row, enermy_col]]
                        result = True
                    # row under top row 
                    elif state[row - 1][col] == self.str:
                        self.player_move = [[row - 1, col], [enermy_row, enermy_col]]
                        result = True
                # Left
                elif Left(col):
                    if state[row][col + 1] == self.str:
                        self.player_move = [[row, col + 1], [enermy_row, enermy_col]]
                        result = True
                    elif state[row - 1][col + 1] == self.str:
                        self.player_move = [[row - 1, col + 1], [enermy_row, enermy_col]]
                        result = True
                    # row under top row 
                    elif state[row - 1][col] == self.str:
                        self.player_move = [[row - 1, col], [enermy_row, enermy_col]]
                        result = True
                # Right
                elif Right(col):
                    if state[row][col - 1] == self.str:
                        self.player_move = [[row, col - 1], [enermy_row, enermy_col]]
                        result = True
                    elif state[row -1][col - 1] == self.str:
                        self.player_move = [[row - 1, col - 1], [enermy_row, enermy_col]]
                        result = True
                    # row under top row 
                    elif state[row - 1][col] == self.str:
                        self.player_move = [[row - 1, col], [enermy_row, enermy_col]]
                        result = True
            # Chessman in Bottom row
            elif Bottom(row):
                # Position in Bottom row
                # Middle
                if col == 2:
                    if state[row][col - 1] == self.str:
                        self.player_move = [[row, col - 1], [enermy_row, enermy_col]]
                        result = True
                    elif state[row][col + 1] == self.str:
                        self.player_move = [[row, col + 1], [enermy_row, enermy_col]]
                        result = True
                    elif state[row + 1][col + 1] == self.str:
                        self.player_move = [[row + 1, col + 1], [enermy_row, enermy_col]]
                        result = True
                    elif state[row][col - 1] == self.str:
                        self.player_move = [[row, col - 1], [enermy_row, enermy_col]]
                        result = True
                    elif state[row + 1][col - 1] == self.str:
                        self.player_move = [[row + 1, col - 1], [enermy_row, enermy_col]]
                        result = True
                    # row under top row 
                    elif state[row + 1][col] == self.str:
                        self.player_move = [[row + 1, col], [enermy_row, enermy_col]]
                        result = True
                # Left
                elif Left(col):
                    if state[row][col + 1] == self.str:
                        self.player_move = [[row, col + 1], [enermy_row, enermy_col]]
                        result = True
                    elif state[row + 1][col + 1] == self.str:
                        self.player_move = [[row + 1, col + 1], [enermy_row, enermy_col]]
                        result = True
                    # row under top row 
                    elif state[row + 1][col] == self.str:
                        self.player_move = [[row + 1, col], [enermy_row, enermy_col]]
                        result = True
                # Right
                elif Right(col):
                    if state[row][col - 1] == self.str:
                        self.player_move = [[row, col - 1], [enermy_row, enermy_col]]
                        result = True
                    elif state[row + 1][col - 1] == self.str:
                        self.player_move = [[row + 1, col - 1], [enermy_row, enermy_col]]
                        result = True
                    # row under top row 
                    elif state[row + 1][col] == self.str:
                        self.player_move = [[row + 1, col], [enermy_row, enermy_col]]
                        result = True

            # Chessman in Left row (except in corner) 
            # Only row = 2 is match this condition
            elif Left(col):
                if state[row + 1][col] == self.str:
                    self.player_move = [[row + 1, col], [enermy_row, enermy_col]]
                    result = True
                elif state[row + 1][col + 1] == self.str:
                    self.player_move = [[row + 1, col + 1], [enermy_row, enermy_col]]
                    result = True
                elif state[row - 1][col] == self.str:
                    self.player_move = [[row - 1, col], [enermy_row, enermy_col]]
                    result = True
                elif state[row - 1][col + 1] == self.str:
                    self.player_move = [[row - 1, col + 1], [enermy_row, enermy_col]]
                    result = True
                elif state[row][col + 1] == self.str:
                    self.player_move = [[row, col + 1], [enermy_row, enermy_col]]
                    result = True
            # right col
            elif Right(col):
                if state[row + 1][col] == self.str:
                    self.player_move = [[row + 1, col], [enermy_row, enermy_col]]
                    result = True
                elif state[row + 1][col - 1] == self.str:
                    self.player_move = [[row + 1, col - 1], [enermy_row, enermy_col]]
                    result = True
                elif state[row - 1][col] == self.str:
                    self.player_move = [[row - 1, col], [enermy_row, enermy_col]]
                    result = True
                elif state[row - 1][col - 1] == self.str:
                    self.player_move = [[row - 1, col - 1], [enermy_row, enermy_col]]
                    result = True
                elif state[row][col - 1] == self.str:
                    self.player_move = [[row, col - 1], [enermy_row, enermy_col]]
                    result = True
            else:
                if state[row + 1][col] == self.str:
                    self.player_move = [[row + 1, col], [enermy_row, enermy_col]]
                    result = True
                elif state[row - 1][col] == self.str:
                    self.player_move = [[row - 1, col], [enermy_row, enermy_col]]
                    result = True
                elif state[row + 1][col + 1] == self.str:
                    self.player_move = [[row + 1, col + 1], [enermy_row, enermy_col]]
                    result = True
                elif state[row - 1][col - 1] == self.str:
                    self.player_move = [[row - 1, col - 1], [enermy_row, enermy_col]]
                    result = True
                elif state[row][col + 1] == self.str:
                    self.player_move = [[row, col + 1], [enermy_row, enermy_col]]
                    result = True
                elif state[row][col - 1] == self.str:
                    self.player_move = [[row, col - 1], [enermy_row, enermy_col]]
                    result = True
                elif state[row - 1][col + 1] == self.str:
                    self.player_move = [[row - 1, col + 1], [enermy_row, enermy_col]]
                    result = True
                elif state[row + 1][col - 1] == self.str:
                    self.player_move = [[row + 1, col - 1], [enermy_row, enermy_col]]
                    result = True
        else:
            # Chessman in Top row
            if Top(row):
                # Position in top row
                if state[row][col - 1] == self.str:
                    self.player_move = [[row, col - 1], [enermy_row, enermy_col]]
                    result = True
                elif state[row][col + 1] == self.str:
                    self.player_move = [[row, col + 1], [enermy_row, enermy_col]]
                    result = True
               # row under top row 
                elif state[row - 1][col] == self.str:
                    self.player_move = [[row - 1, col], [enermy_row, enermy_col]]
                    result = True
            # Chessman in Bottom row
            elif Bottom(row):
                # Position in Bottom row
                if state[row][col - 1] == self.str:
                    self.player_move = [[row, col - 1], [enermy_row, enermy_col]]
                    result = True
                elif state[row][col + 1] == self.str:
                    self.player_move = [[row, col + 1], [enermy_row, enermy_col]]
                    result = True
                # row upper Bottom row 
                elif state[row + 1][col] == self.str:
                    self.player_move = [[row + 1, col], [enermy_row, enermy_col]]
                    result = True
            # Left row
            elif Left(col):
                if state[row + 1][col] == self.str:
                    self.player_move = [[row + 1, col], [enermy_row, enermy_col]]
                    result = True
                elif state[row][col + 1] == self.str:
                    self.player_move = [[row, col + 1], [enermy_row, enermy_col]]
                    result = True
                elif state[row - 1][col] == self.str:
                    self.player_move = [[row - 1, col], [enermy_row, enermy_col]]
                    result = True
            elif Right(col):
                if state[row + 1][col] == self.str:
                    self.player_move = [[row + 1, col], [enermy_row, enermy_col]]
                    result = True
                elif state[row - 1][col] == self.str:
                    self.player_move = [[row - 1, col], [enermy_row, enermy_col]]
                    result = True
                elif state[row][col - 1] == self.str:
                    self.player_move = [[row, col - 1], [enermy_row, enermy_col]]
                    result = True
            else:
                if state[row + 1][col] == self.str:
                    self.player_move = [[row + 1, col], [enermy_row, enermy_col]]
                    result = True
                elif state[row - 1][col] == self.str:
                    self.player_move = [[row - 1, col], [enermy_row, enermy_col]]
                    result = True
                elif state[row][col + 1] == self.str:
                    self.player_move = [[row, col + 1], [enermy_row, enermy_col]]
                    result = True
                elif state[row][col - 1] == self.str:
                    self.player_move = [[row, col - 1], [enermy_row, enermy_col]]
                    result = True
        return result

    """ Find move move_opportunities for all near by spaces """
    def move_opportunities(self, state, current_post):
        row = current_post[0]
        col = current_post[1]
        if col % 2 == 0:
            if col == 0:
                if row % 2 == 0:
                    # Col 0 row 0 
                    if row == 0:
                        # Right
                        if state[row][col + 1] == '.':
                            new_state = deepcopy(state)
                            self.move(new_state, [row, col], [row, col + 1])
                        # Top - Right
                        if state[row + 1][col + 1] == '.':
                            new_state = deepcopy(state)
                            self.move(new_state, [row, col], [row + 1, col + 1]) 
                        # Top
                        if state[row + 1][col] == '.':
                            new_state = deepcopy(state)
                            self.move(new_state, [row, col], [row + 1, col])
                    # Col 0 row 2
                    elif row == 2:
                        # Right
                        if state[row][col + 1] == '.':
                            new_state = deepcopy(state)
                            self.move(new_state, [row, col], [row, col + 1])
                        # Bottom - Right
                        if state[row - 1][col + 1] == '.':
                            new_state = deepcopy(state)
                            self.move(new_state, [row, col], [row - 1, col + 1]) 
                        # Bottom
                        if state[row - 1][col] == '.':
                            new_state = deepcopy(state)
                            self.move(new_state, [row, col], [row - 1, col])
                        # Top - Right
                        if state[row + 1][col + 1] == '.':
                            new_state = deepcopy(state)
                            self.move(new_state, [row, col], [row + 1, col + 1])
                        # Bottom
                        if state[row + 1][col] == '.':
                            new_state = deepcopy(state)
                            self.move(new_state, [row, col], [row + 1, col])
                    # Col 0 row 4
                    else:
                        # Bottom
                        if state[row - 1][col] == '.':
                            new_state = deepcopy(state)
                            self.move(new_state, [row, col], [row - 1, col])
                        # Bottom - Right
                        if state[row - 1][col + 1] == '.':
                            new_state = deepcopy(state)
                            self.move(new_state, [row, col], [row - 1, col + 1])
                        # Right
                        if state[row][col + 1] == '.':
                            new_state = deepcopy(state)
                            self.move(new_state, [row, col], [row, col + 1])
                else:
                    # Col 0 row 1
                    if row == 1:
                        # Bottom
                        if state[row - 1][col] == '.':
                            new_state = deepcopy(state)
                            self.move(new_state, [row, col], [row - 1, col])
                        # Right
                        if state[row][col + 1] == '.':
                            new_state = deepcopy(state)
                            self.move(new_state, [row, col], [row, col + 1])
                        # Top
                        if state[row + 1][col] == '.':
                            new_state = deepcopy(state)
                            self.move(new_state, [row, col], [row + 1, col])
                    # Col 0 row 3
                    else:
                        # Bottom
                        if state[row -1][col] == '.':
                            new_state = deepcopy(state)
                            self.move(new_state, [row, col], [row - 1, col])
                        # Right
                        if state[row][col + 1] == '.':
                            new_state = deepcopy(state)
                            self.move(new_state, [row, col], [row, col + 1])
                        # Top
                        if state[row + 1][col] == '.':
                            new_state = deepcopy(state)
                            self.move(new_state, [row, col], [row + 1, col])
            elif col == 2:
                if row % 2 == 0:
                    # Row 0 Col 2 
                    if row == 0:
                        # Right
                        if state[row][col + 1] == '.':
                            new_state = deepcopy(state)
                            self.move(new_state, [row, col], [row, col + 1])
                        # Top - Right
                        if state[row + 1][col + 1] == '.':
                            new_state = deepcopy(state)
                            self.move(new_state, [row, col], [row + 1, col + 1]) 
                        # Top 
                        if state[row + 1][col] == '.':
                            new_state = deepcopy(state)
                            self.move(new_state, [row, col], [row + 1, col])
                        # Top - Left
                        if state[row + 1][col - 1] == '.':
                            new_state = deepcopy(state)
                            self.move(new_state, [row, col], [row + 1, col - 1])
                        # Left
                        if state[row][col - 1] == '.':
                            new_state = deepcopy(state)
                            self.move(new_state, [row, col], [row, col - 1])
                    # Row 2 Col 2
                    elif row == 2:
                        # Bottom 
                        if state[row - 1][col] == '.':
                            new_state = deepcopy(state)
                            self.move(new_state, [row, col], [row - 1, col])
                        # Bottom - Right
                        if state[row - 1][col + 1] == '.':
                            new_state = deepcopy(state)
                            self.move(new_state, [row, col], [row - 1, col + 1]) 
                        # Left 
                        if state[row][col + 1] == '.':
                            new_state = deepcopy(state)
                            self.move(new_state, [row, col], [row, col + 1])
                        # Top - Left
                        if state[row + 1][col + 1] == '.':
                            new_state = deepcopy(state)
                            self.move(new_state, [row, col], [row + 1, col + 1])
                        # Top
                        if state[row + 1][col] == '.':
                            new_state = deepcopy(state)
                            self.move(new_state, [row, col], [row + 1, col])
                        # Top - Left
                        if state[row + 1][col - 1] == '.':
                            new_state = deepcopy(state)
                            self.move(new_state, [row, col], [row + 1, col -1])
                        # Left
                        if state[row][col - 1] == '.':
                            new_state = deepcopy(state)
                            self.move(new_state, [row, col], [row, col - 1])
                        # Bottom - Left
                        if state[row - 1][col - 1]:
                            new_state = deepcopy(state)
                            self.move(new_state, [row, col], [row - 1, col - 1])
                    # Row 4 Col 2
                    elif row == 4:
                        # Left 
                        if state[row][col - 1] == '.':
                            new_state = deepcopy(state)
                            self.move(new_state, [row, col], [row, col - 1])
                        # Bottom - Left
                        if state[row - 1][col - 1] == '.':
                            new_state = deepcopy(state)
                            self.move(new_state, [row, col], [row - 1, col - 1])
                        # Bottom
                        if state[row - 1][col] == '.':
                            new_state = deepcopy(state)
                            self.move(new_state, [row, col], [row - 1, col])
                        # Bottom - Right
                        if state[row - 1][col + 1] == '.':
                            new_state = deepcopy(state)
                            self.move(new_state, [row, col], [row - 1, col + 1])
                        # Right
                        if state[row][col + 1] == '.':
                            new_state = deepcopy(state)
                            self.move(new_state, [row, col], [row, col + 1])
                else:
                    # Row 1 Col 2
                    if row == 1:
                        # Left
                        if state[row][col + 1] == '.':
                            new_state = deepcopy(state)
                            self.move(new_state, [row, col], [row, col + 1])
                        # Right
                        if state[row][col + 1] == '.':
                            new_state = deepcopy(state)
                            self.move(new_state, [row, col], [row, col + 1])
                        # Bottom
                        if state[row - 1][col] == '.':
                            new_state = deepcopy(state)
                            self.move(new_state, [row, col], [row - 1, col])
                        # Top
                        if state[row + 1][col] == '.':
                            new_state = deepcopy(state)
                            self.move(new_state, [row, col], [row + 1, col])
                    # Row 3 col 2
                    else:
                        # Bottom
                        if state[row - 1][col] == '.':
                            new_state = deepcopy(state)
                            self.move(new_state, [row, col], [row - 1, col])
                        # Left
                        if state[row][col - 1] == '.':
                            new_state = deepcopy(state)
                            self.move(new_state, [row, col], [row, col - 1])
                        # Top
                        if state[row + 1][col] == '.':
                            new_state = deepcopy(state)
                            self.move(new_state, [row, col], [row + 1, col])
                        # Right
                        if state[row][col + 1] == '.':
                            new_state = deepcopy(state)
                            self.move(new_state, [row, col], [row, col + 1])
            else:
                if row % 2 == 0:
                    # Row 0 Col 4 
                    if row == 0:
                        # Left 
                        if state[row][col - 1] == '.':
                            new_state = deepcopy(state)
                            self.move(new_state, [row, col], [row, col - 1])
                        # Top - Left 
                        if state[row + 1][col - 1] == '.':
                            new_state = deepcopy(state)
                            self.move(new_state, [row, col], [row + 1, col - 1]) 
                        # Top
                        if state[row + 1][col] == '.':
                            new_state = deepcopy(state)
                            self.move(new_state, [row, col], [row + 1, col])
                    # Col 4 row 2
                    elif row == 2:
                        # Left 
                        if state[row][col - 1] == '.':
                            new_state = deepcopy(state)
                            self.move(new_state, [row, col], [row, col - 1])
                        # Bottom - Left 
                        if state[row - 1][col - 1] == '.':
                            new_state = deepcopy(state)
                            self.move(new_state, [row, col], [row - 1, col - 1]) 
                        # Bottom
                        if state[row - 1][col] == '.':
                            new_state = deepcopy(state)
                            self.move(new_state, [row, col], [row - 1, col])
                        # Top - Left 
                        if state[row + 1][col - 1] == '.':
                            new_state = deepcopy(state)
                            self.move(new_state, [row, col], [row + 1, col - 1])
                        # Bottom
                        if state[row + 1][col] == '.':
                            new_state = deepcopy(state)
                            self.move(new_state, [row, col], [row + 1, col])
                    # Col 4 row 4
                    else:
                        # Bottom
                        if state[row - 1][col] == '.':
                            new_state = deepcopy(state)
                            self.move(new_state, [row, col], [row - 1, col])
                        # Bottom - Left 
                        if state[row - 1][col - 1] == '.':
                            new_state = deepcopy(state)
                            self.move(new_state, [row, col], [row - 1, col - 1])
                        # Left 
                        if state[row][col - 1] == '.':
                            new_state = deepcopy(state)
                            self.move(new_state, [row, col], [row, col - 1])
                else:
                    # Col 4 row 1
                    if row == 1:
                        # Bottom
                        if state[row - 1][col] == '.':
                            new_state = deepcopy(state)
                            self.move(new_state, [row, col], [row - 1, col])
                        # Left 
                        if state[row][col - 1] == '.':
                            new_state = deepcopy(state)
                            self.move(new_state, [row, col], [row, col - 1])
                        # Top
                        if state[row + 1][col] == '.':
                            new_state = deepcopy(state)
                            self.move(new_state, [row, col], [row + 1, col])
                    # Col 4 row 3
                    else:
                        # Bottom
                        if state[row - 1][col] == '.':
                            new_state = deepcopy(state)
                            self.move(new_state, [row, col], [row - 1, col])
                        # Left 
                        if state[row][col - 1] == '.':
                            new_state = deepcopy(state)
                            self.move(new_state, [row, col], [row, col - 1])
                        # Top
                        if state[row + 1][col] == '.':
                            new_state = deepcopy(state)
                            self.move(new_state, [row, col], [row + 1, col])
        else:
            if row % 2 == 0:
                # Row 0 Col 1 or Col 3
                if row == 0:
                    # Left
                    if state[row][col - 1] == '.':
                        new_state = deepcopy(state)
                        self.move(new_state, [row, col], [row, col - 1])
                    # Top
                    if state[row + 1][col] == '.':
                        new_state = deepcopy(state)
                        self.move(new_state, [row, col], [row + 1, col])
                    # Right 
                    if state[row][col + 1] == '.':
                        new_state = deepcopy(state) 
                        self.move(new_state, [row, col], [row, col + 1])
                # Row 2 Col 1 or Col 3
                elif row == 2:
                    # Left
                    if state[row][col - 1] == '.':
                        new_state = deepcopy(state)
                        self.move(new_state, [row, col], [row, col - 1])
                    # Top
                    if state[row + 1][col] == '.':
                        new_state = deepcopy(state)
                        self.move(new_state, [row, col], [row + 1, col])
                    # Right 
                    if state[row][col + 1] == '.':
                        new_state = deepcopy(state) 
                        self.move(new_state, [row, col], [row, col + 1])
                    # Bottom
                    if state[row - 1][col] == '.':
                        new_state = deepcopy(state)
                        self.move(new_state, [row, col], [row - 1, col])
                # Row 4 Col 1 or Col 3
                else:
                    # Left
                    if state[row][col - 1] == '.':
                        new_state = deepcopy(state)
                        self.move(new_state, [row, col], [row, col - 1])
                    # Right 
                    if state[row][col + 1] == '.':
                        new_state = deepcopy(state) 
                        self.move(new_state, [row, col], [row, col + 1])
                    # Bottom
                    if state[row - 1][col] == '.':
                        new_state = deepcopy(state)
                        self.move(new_state, [row, col], [row - 1, col])
            else:
                # Left
                if state[row][col - 1] == '.':
                    new_state = deepcopy(state)
                    self.move(new_state, [row, col], [row, col - 1])
                # Top - Left
                if state[row + 1][col - 1] == '.':
                    new_state = deepcopy(state)
                    self.move(new_state, [row, col], [row + 1, col - 1])
                # Top
                if state[row + 1][col] == '.':
                    new_state = deepcopy(state)
                    self.move(new_state, [row, col], [row + 1, col])
                # Top - Right
                if state[row + 1][col + 1] == '.':
                    new_state = deepcopy(state)
                    self.move(new_state, [row, col], [row + 1, col + 1])
                # Right 
                if state[row][col + 1] == '.':
                    new_state = deepcopy(state) 
                    self.move(new_state, [row, col], [row, col + 1])
                # Bottom - Right
                if state[row - 1][col + 1] == '.':
                    new_state = deepcopy(state)
                    self.move(new_state, [row, col], [row - 1, col + 1])
                # Bottom
                if state[row - 1][col] == '.':
                    new_state = deepcopy(state)
                    self.move(new_state, [row, col], [row - 1, col])
                # Bottom - Left
                if state[row - 1][col - 1] == '.':
                    new_state = deepcopy(state)
                    self.move(new_state, [row, col], [row - 1, col - 1])

    """ Moving and get new Evaluate generate all state """
    def generate(self, state):
        new_state = deepcopy(state)
        for row in [4, 3, 2, 1, 0]:
            for col in range(5):
                if new_state[row][col] == self.str:
                    current_post = [row,col]
                    self.move_opportunities(new_state, current_post)
    # Student MUST implement this function
    # The return value should be a move that is denoted by a list of tuples:
    # [(row1, col1), (row2, col2)] with:
        # (row1, col1): current position of selected piece
        # (row2, col2): new position of selected piece
    def next_move(self, state):
        self.Value = 0
        self.player_move = 0
        
        if self.Last_state == 0:
            self.Last_state = deepcopy(state)

        if self.openStep(state) is False:
            self.generate(state)
        
        self.Last_state = deepcopy(state)
        if self.player_move == 0:
            return False
        
        self.move(self.Last_state, self.player_move[0], self.player_move[1])
        selected_chess_row = self.player_move[0][0]
        selected_chess_col = self.player_move[0][1]
        new_position_row = self.player_move[1][0]
        new_position_col = self.player_move[1][1] 

        result = [(selected_chess_row, selected_chess_col), (new_position_row, new_position_col)]
        return result
