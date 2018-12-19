from copy import deepcopy

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

    """One for two"""
    def OneForTwo (self, state, position):
    """Two for one"""
    def TwoForOne (self, state, position):
    """ Change color """
    def change_color(self, state, position):
    


    """ Find move move_opportunities for all near by spaces """
    def move_opportunities(self, state, current_post):
        row = current_post[0]
        col = current_post[1]
        #   * . *   * * *
        #   * * * =>* . *
        #   * * *   * * * 
        if not Top(row) and state[row + 1][col] == '.':
            new_state = deepcopy(state)
            self.move(new_state, current_post, [row + 1, col])
            print(current_post)
            print_state(new_state)

        #   . * *   * * *
        #   * * * =>* . *
        #   * * *   * * * 
        if not Top(row) and not Left(col) and state[row + 1][col - 1] == '.':
            new_state = deepcopy(state)
            self.move(new_state, current_post, [row + 1, col - 1])
            print(current_post)
            print_state(new_state)

        #   * * *   * * *
        #   . * * =>* . *
        #   * * *   * * * 
        if not Left(col) and state[row][col - 1] == '.':
            new_state = deepcopy(state)
            self.move(new_state, current_post, [row, col - 1])
            print(current_post)
            print_state(new_state)
        
        #   * * *   * * *
        #   * * * =>* . *
        #   . * *   * * * 
        if not Left(col) and not Bottom(row) and state[row - 1][col - 1] == '.':
            new_state = deepcopy(state)
            self.move(new_state, current_post, [row - 1, col - 1])
            print(current_post)
            print_state(new_state)
            
        #   * * *   * * *
        #   * * * =>* . *
        #   * . *   * * * 
        if not Bottom(row) and state[row - 1][col] == '.':
            new_state = deepcopy(state)
            self.move(new_state, current_post, [row - 1, col])
            print(current_post)
            print_state(new_state)

        #   * * *   * * *
        #   * * * =>* . *
        #   * * .   * * * 
        if not Bottom(row) and not Right(col) and state[row - 1][col + 1] == '.':
            new_state = deepcopy(state)
            self.move(new_state, current_post, [row - 1, col + 1])
            print(current_post)
            print_state(new_state)

        #   * * *   * * *
        #   * * . =>* . *
        #   * * *   * * * 
        if not Right(col) and state[row][col + 1] == '.':
            new_state = deepcopy(state)
            self.move(new_state, current_post, [row, col + 1])
            print(current_post)
            print_state(new_state)
        #   * * .   * * *
        #   * * * =>* . *
        #   * * *   * * * 
        if not Top(row) and not Right(col) and state[row + 1][col + 1] == '.':
            new_state = deepcopy(state)
            self.move(new_state, current_post, [row + 1, col + 1])
            print(current_post)
            print_state(new_state)
    
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
        self.generate(state)
        result = [(2, 0), (3, 1)]
        return result
