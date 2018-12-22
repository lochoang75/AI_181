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

    def __enermy__(self):
        if self.str == "r":
            self.enermy = "b"
        else:
            self.enermy = "r"

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


    """One for two"""
    def OneForTwo (self, state, position):
        # Check and change the chessman color 
        # ? self.str ?
        if state[position[0]] == self.enermy and state[position[1]] == self.enermy:
            return True
        else:
            return False

    """Two for one"""
    def TwoForOne (self, state, position):
        # Check and change the chessman color
        # self.str self.enermy ?
        if state[position] == self.str:
            return True 
        else:
            return False 

    """ Change color """
    def change_color(self, state, position):
        row = position[0]
        col = position[1]
        if not Top(row) and not Bottom(row) and not Left(col) and not Right(col):
            # ? x x
            # x * x
            # x x ?
            if state[row + 1][col - 1] == self.enermy:
                unknow_post = [(row + 1, col - 1), (row - 1, col + 1)]
                if self.OneForTwo(state, unknow_post):
                    state[row + 1][col - 1] = self.str
                    state[row - 1][col + 1] = self.str
                else:
                    # ? x x
                    # x r x
                    # x x b
                    if not Top(row + 1) and not Left(col - 1):
                        if self.TwoForOne(state, (row + 2, col - 2)):
                            # b x x 
                            # x r x
                            # x x b
                            state[row + 1][col - 1] = self.str
            # x ? x
            # x * x
            # x ? x
            if state[row + 1][col] == self.enermy:
                unknow_post = [(row + 1, col), (row - 1, col)]
                if self.OneForTwo(state, unknow_post):
                    state[row + 1][col] = self.str
                    state[row - 1][col] = self.str
                else:
                    # x ? x
                    # x r x
                    # x b x
                    if not Top(row + 1):
                        if self.TwoForOne(state, (row + 2, col)):
                            # x b x 
                            # x r x
                            # x b x
                            state[row + 1][col] = self.str
            # x x ?
            # x * x
            # ? x x
            if state[row + 1][col + 1] == self.enermy:
                unknow_post = [(row + 1, col + 1), (row - 1, col - 1)]
                if self.OneForTwo(state, unknow_post):
                    state[row + 1][col + 1] = self.str
                    state[row - 1][col - 1] = self.str
                else:
                    # x x ?
                    # x r x
                    # b x x
                    if not Top(row + 1) and not Right(col + 1):
                        if self.TwoForOne(state, (row + 2, col + 2)):
                            # x x b 
                            # x r x
                            # b x x
                            state[row + 1][col + 1] = self.str
            # x x x
            # ? * ?
            # x x x
            if state[row][col + 1] == self.enermy:
                unknow_post = [(row, col + 1), (row, col - 1)]
                if self.OneForTwo(state, unknow_post) :
                    state[row][col + 1] = self.str
                    state[row][col - 1] = self.str
                else:
                    # x x x
                    # b r ?
                    # x x x
                    if not Right(col + 1):
                        if self.TwoForOne(state, (row, col + 2)):
                            # x x x 
                            # b r b
                            # x x x
                            state[row][col + 1] = self.str
            # x x x
            # x * x
            # x x ?
            if state[row - 1][col + 1] == self.enermy:
                # b x x
                # x r x
                # x x ?
                if not Right(col + 1) and not Bottom(row - 1):
                    if self.TwoForOne(state, (row - 2, col + 2)):
                        # b x x 
                        # x r x
                        # x x b
                        state[row -1][col + 1] = self.str

            # x x x
            # x * x
            # x ? x
            if state[row - 1][col] == self.enermy:
                # x b x
                # x r x
                # x ? x
                if not Bottom(row - 1):
                    if self.TwoForOne(state, (row - 2, col)):
                        # x b x 
                        # x r x
                        # x b x
                        state[row -1][col] = self.str

            # x x x
            # x * x
            # ? x x
            if state[row - 1][col - 1] == self.enermy:
                # x x b
                # x r x
                # ? x x
                if not Bottom(row - 1) and not Left(col - 1):
                    if self.TwoForOne(state, (row - 2, col - 2)):
                        # x x b 
                        # x r x
                        # b x x
                        state[row -1][col - 1] = self.str

            # x x x
            # ? * x
            # x x x
            if state[row][col - 1] == self.enermy:
                # x x x
                # ? r b
                # x x x
                if not Left(col - 1):
                    if self.TwoForOne(state, (row, col - 2)):
                        # x x x 
                        # b r b
                        # x x x
                        state[row][col - 1] = self.str
        # -------
        # ? * ?
        # ? ? ?
        elif Top(row):
            #-------
            #| * ? ?
            #| ? ? ?
            #| ? ? ?
            if Left(col):
                #-------
                #| b r ?
                #| x x x
                #| x x x
                if state[row][col + 1] == self.enermy:
                    if self.TwoForOne(state, (row, col + 2)):
                        # b r b
                        # x x x
                        # x x x
                        state[row][col + 1] = self.str
                #-------
                #| b x x
                #| x r x
                #| x x ?
                if state[row - 1][col +1] == self.enermy:
                    if self.TwoForOne(state, (row - 2, col + 2)):
                        # b x x
                        # x r x
                        # x x b
                        state[row - 1][col + 1] == self.str

                #-------
                #| b x x
                #| r x x
                #| ? x x
                if state[row - 1][col] == self.enermy:
                    if self.TwoForOne(state, (row - 2, col)):
                        # b x x
                        # r x x
                        # b x x
                        state[row - 1][col] == self.str

            #-------
            # * ? ?|
            # ? ? ?|
            # ? ? ?|
            elif Right(col):
                #-------
                # ? r b|
                # x x x|
                # x x x|
                if state[row][col - 1] == self.enermy:
                    if self.TwoForOne(state, (row, col - 2)):
                        # b r b
                        # x x x
                        # x x x
                        state[row][col - 1] = self.str
                #-------
                # x x b|
                # x r x|
                # ? x x|
                if state[row - 1][col - 1] == self.enermy:
                    if self.TwoForOne(state, (row - 2, col - 2)):
                        # x x b
                        # x r x
                        # b x x
                        state[row - 1][col - 1] == self.str
                #-------
                # x x b|
                # x x r|
                # x x ?|
                if state[row - 1][col] == self.enermy:
                    if self.TwoForOne(state, (row - 2, col)):
                        # x x b
                        # x x r
                        # x x b
                        state[row - 1][col] == self.str

            #-------
            # ? * ?
            # ? ? ?
            # ? ? ?
            else:
                #-------
                # r * ?
                # x x x
                # x x x
                if state[row][col - 1] == self.enermy:
                    unknow_post = [(row, col - 1), (row, col + 1)]
                    # r b r
                    # x x x
                    # x x x
                    if self.OneForTwo(state, unknow_post):
                        state[row][col - 1] = self.str
                        state[row][col + 1] = self.str
                    # b r b
                    # x x x
                    # x x x
                    else:
                        if not Left(col - 1):
                            if self.TwoForOne(state, (row, col - 2)):
                                state[row][col - 1] = self.str
                #-------
                # x x b
                # x r x
                # ? x x
                if state[row - 1][col - 1] == self.enermy:
                    if not Left(col - 1):
                        #-------
                        # x x b
                        # x r x
                        # b x x
                        if self.TwoForOne(state, (row - 2, col - 2)):
                            state[row -1][col - 1] = self.str
                #-------
                # x x b
                # x x r
                # x x ?
                if state[row - 1][col]:
                    #-------
                    # x x b
                    # x r x
                    # b x x
                    if self.TwoForOne(state, (row - 2, col)):
                        state[row -1][col] = self.str
                #-------
                # b x x
                # x r x
                # x x ?
                if state[row - 1][col + 1]:
                    if not Right(col + 1):
                        #-------
                        # x x b
                        # x r x
                        # b x x
                        if self.TwoForOne(state, (row - 2, col + 2)):
                            state[row - 1][col + 1] = self.str
                #-------
                # b r ?
                # x x x
                # x x x
                if state[row][col + 1]:
                    if not Right(col + 1):
                        #-------
                        # b r b
                        # x x x
                        # x x x
                        if self.TwoForOne(state, (row, col + 2)):
                            state[row][col + 1] = self.str
        elif Bottom(row):
            #| ? ? ?
            #| ? ? ?
            #| * ? ?
            #-------
            if Left(col):
                #| ? x x
                #| r x x
                #| b x x
                #-------
                if state[row + 1][col] == self.enermy:
                    if self.TwoForOne(state, (row + 2, col)):
                        # b x x
                        # r x x
                        # b x x
                        state[row + 2][col] = self.str
                #| x x ?
                #| x r x
                #| b x x
                #-------
                if state[row + 1][col + 1] == self.enermy:
                    if self.TwoForOne(state, (row + 2, col + 2)):
                        # x x b
                        # x r x
                        # b x x
                        state[row + 1][col + 1] == self.str
                #| x x x
                #| x x x
                #| b r ?
                #--------
                if state[row][col + 1] == self.enermy:
                    if self.TwoForOne(state, (row, col + 2)):
                        # x x x
                        # x x x
                        # b r b
                        state[row][col + 1] == self.str
            # ? ? ?|
            # ? ? ?|
            # ? ? *|
            #-------
            elif Right(col):
                # x x x|
                # x x x|
                # x r b|
                #-------
                if state[row][col - 1] == self.enermy:
                    if self.TwoForOne(state, (row, col - 2)):
                        # x x x
                        # x x x
                        # b r b
                        state[row][col - 1] = self.str
                # x x x|
                # x r x|
                # x x b|
                #-------
                if state[row + 1][col - 1] == self.enermy:
                    if self.TwoForOne(state, (row + 2, col - 2)):
                        # b x x
                        # x r x
                        # x x b
                        state[row + 1][col - 1] == self.str
                # x x ?|
                # x x r|
                # x x b|
                #-------
                if state[row + 1][col] == self.enermy:
                    if self.TwoForOne(state, (row + 2, col)):
                        # x x b
                        # x x r
                        # x x b
                        state[row + 1][col] == self.str
            # ? ? ?
            # ? ? ?
            # ? * ?
            #------
            else:
                # x x x
                # x x x
                # x * x
                #------
                if state[row][col - 1] == self.enermy:
                    unknow_post = [(row, col - 1), (row, col + 1)]
                    # x x x
                    # x x x
                    # r b r
                    if self.OneForTwo(state, unknow_post):
                        state[row][col - 1] = self.str
                        state[row][col + 1] = self.str
                    # x x x
                    # x x x
                    # b r b
                    else:
                        if not Left(col - 1):
                            if self.TwoForOne(state, (row, col - 2)):
                                state[row][col - 1] = self.str
                # ? x x
                # x r x
                # x x b
                #------
                if state[row + 1][col - 1] == self.enermy:
                    if not Left (col - 1):
                        # ? x x
                        # x r x
                        # x x b
                        #------
                        if self.TwoForOne(state, (row - 2, col - 2)):
                            state[row + 1][col - 1] = self.str
                # x x ?
                # x x r
                # x x b
                #------
                if state[row + 1][col]:
                    # x x b
                    # x x r
                    # x x b
                    #-------
                    if self.TwoForOne(state, (row + 2, col)):
                        state[row -1][col] = self.str
                # x x ?
                # x r x
                # b x x
                #------
                if state[row + 1][col + 1]:
                    if not Right(col + 1):
                        #-------
                        # x x b
                        # x r x
                        # b x x
                        if self.TwoForOne(state, (row + 2, col + 2)):
                            state[row + 1][col + 1] = self.str
                # x x x
                # x x x
                # b r ?
                #------
                if state[row][col + 1]:
                    if not Right(col + 1):
                        # x x x
                        # x x x
                        # b r b
                        #------
                        if self.TwoForOne(state, (row, col + 2)):
                            state[row][col + 1] = self.str
        elif Left(col):
            #| r x x
            #| b x x
            #| x x x
            if state[row + 1][col] == self.enermy:
                # Doesn't need to handle Top and Botton b/c if b in 
                # top or botton function before must handle it
                unknow_post = [(row + 1,col), (row - 1, col)]
                if self.OneForTwo(state, unknow_post):
                    state[row + 1][col] = self.str
                    state[row - 1][col] = self.str
                elif not Top(row + 1):
                    if self.TwoForOne(state, (row + 2, col)):
                        #------
                        #| b x x
                        #| r x x
                        #| b x x
                        state[row + 2][col] = self.str
            #| x x ?
            #| x r x
            #| b x x
            if state[row + 1][col + 1]:
                if not Top(row + 1):
                    #| x x b
                    #| x r x
                    #| b x x
                    if self.TwoForOne(state, (row + 2, col + 2)):
                        state[row + 1][col + 1] = self.str
            #| x x x
            #| b r ?
            #| x x x
            if state[row][col + 1] == self.enermy:
                #| x x x
                #| b r b
                #| x x x
                if self.TwoForOne(state, (row, col + 2)):
                    state[row][col + 1] = self.str
            #| b x x
            #| x r x
            #| x x ?
            if state[row - 1][col + 1] == self.enermy:
                if not Bottom(row - 1):
                    #| b x x
                    #| x r x
                    #| x x ?
                    if self.TwoForOne(state, (row - 2, col + 2)):
                        # b x x
                        # x r x
                        # x x b
                        state[row - 1][col + 1] == self.str
            #| b x x
            #| r x x
            #| ? x x
            if state[row - 1][col] == self.enermy:
                if not Bottom(row - 1):
                    #| b x x
                    #| r x x
                    #| b x x
                    if self.TwoForOne(state, (row - 2, col)):
                        # b x x
                        # r x x
                        # b x x
                        state[row - 1][col] == self.str
        elif Right(col):
            # x x r|
            # x x b|
            # x x x|
            if state[row + 1][col] == self.enermy:
                # Doesn't need to handle Top and Botton b/c if b in 
                # top or botton function before must handle it
                unknow_post = [(row + 1,col), (row - 1, col)]
                if self.OneForTwo(state, unknow_post):
                    state[row + 1][col] = self.str
                    state[row - 1][col] = self.str
                elif not Top(row + 1):
                    if self.TwoForOne(state, (row + 2, col)):
                        #------
                        #| b x x
                        #| r x x
                        #| b x x
                        state[row + 2][col] = self.str
            # ? x x|
            # x r x|
            # x x b|
            if state[row - 1][col - 1] == self.enermy:
                if not Top(row + 1):
                    # b x x|
                    # x r x|
                    # x x b|
                    if self.TwoForOne(state, (row + 2, col - 2)):
                        state[row][col + 1] = self.str
            # x x x|
            # b r ?|
            # x x x|
            if state[row][col + 1] == self.enermy:
                #| x x x
                #| b r ?
                #| x x x
                if self.TwoForOne(state, (row, col + 2)):
                    # x x x
                    # b r b
                    # x x x
                    state[row][col + 1] == self.str
            # x x b|
            # x r x|
            # ? x x|
            if state[row - 1][col - 1] == self.enermy:
                if not Bottom(row - 1):
                    # x x b|
                    # x r x|
                    # ? x x|
                    if self.TwoForOne(state, (row - 2, col -2)):
                        # x x b|
                        # x r x|
                        # b x x|
                        state[row - 1][col - 1] == self.str
            # x x b|
            # x x r|
            # x x ?|
            if state[row - 1][col] == self.enermy:
                if not Bottom(row - 1):
                    # x x b|
                    # x x r|
                    # x x ?|
                    if self.TwoForOne(state, (row - 2, col)):
                        # x x b|
                        # x x r|
                        # x x b|
                        state[row - 1][col] == self.str

                    
    """ Find move move_opportunities for all near by spaces """
    def move_opportunities(self, state, current_post):
        row = current_post[0]
        col = current_post[1]
        #   * . *   * * *
        #   * * * =>* . *
        #   * * *   * * * 
        if not Top(row) and state[row + 1][col] == '.':
            new_state = deepcopy(state)
            new_post = [row + 1, col]
            self.move(new_state, current_post, new_post)
            print(current_post)
            print_state(new_state)

        #   . * *   * * *
        #   * * * =>* . *
        #   * * *   * * * 
        if not Top(row) and not Left(col) and state[row + 1][col - 1] == '.':
            new_state = deepcopy(state)
            new_post = [row + 1, col - 1]
            self.move(new_state, current_post, new_post)
            print(current_post)
            print_state(new_state)

        #   * * *   * * *
        #   . * * =>* . *
        #   * * *   * * * 
        if not Left(col) and state[row][col - 1] == '.':
            new_state = deepcopy(state)
            new_post = [row, col -1]
            self.move(new_state, current_post, new_post)
            print(current_post)
            print_state(new_state)
        
        #   * * *   * * *
        #   * * * =>* . *
        #   . * *   * * * 
        if not Left(col) and not Bottom(row) and state[row - 1][col - 1] == '.':
            new_state = deepcopy(state)
            new_post = [row - 1, col - 1]
            self.move(new_state, current_post, new_post)
            print(current_post)
            print_state(new_state)
            
        #   * * *   * * *
        #   * * * =>* . *
        #   * . *   * * * 
        if not Bottom(row) and state[row - 1][col] == '.':
            new_state = deepcopy(state)
            new_post = [row - 1, col]
            self.move(new_state, current_post, new_post)
            print(current_post)
            print_state(new_state)

        #   * * *   * * *
        #   * * * =>* . *
        #   * * .   * * * 
        if not Bottom(row) and not Right(col) and state[row - 1][col + 1] == '.':
            new_state = deepcopy(state)
            new_post = [row - 1, col + 1]
            self.move(new_state, current_post, new_post)
            print(current_post)
            print_state(new_state)

        #   * * *   * * *
        #   * * . =>* . *
        #   * * *   * * * 
        if not Right(col) and state[row][col + 1] == '.':
            new_state = deepcopy(state)
            new_post = [row, col + 1]
            self.move(new_state, current_post, new_post)
            print(current_post)
            print_state(new_state)

        #   * * .   * * *
        #   * * * =>* . *
        #   * * *   * * * 
        if not Top(row) and not Right(col) and state[row + 1][col + 1] == '.':
            new_state = deepcopy(state)
            new_post = [row + 1, col + 1]
            self.move(new_state, current_post, new_post)
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
