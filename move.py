from structure import colors,movings,targets,Square,Position,Board
import copy

class Move:
    def __init__(self, board, direction):
        self.original_boad=board
        self.board = copy.deepcopy(board)
        self.final_positions = {}
        self.new_pos,self.target_squares,self.moving_squares=self.move(direction)

    def check_available_moves(self):
        for row in self.board.board:
            for col in self.board.board[row]:
                square = self.board.board[row][col]
                
                if square in movings: 

                    # print(f"Checking moves for {square.type} at ({row}, {col})")
                    
                    moves = {
                        "up": self.find_moves_in_direction(row, col, -1, 0),
                        "down": self.find_moves_in_direction(row, col, 1, 0),
                        "left": self.find_moves_in_direction(row, col, 0, -1),
                        "right": self.find_moves_in_direction(row, col, 0, 1),
                    }
                    # print(f"Available moves for {square.type}: {moves}")
        return moves        

    def find_moves_in_direction(self, row, col, row_delta, col_delta):
        moves=()
        row += row_delta
        col += col_delta

        if row < 0 or row >= len(self.board.board) or col < 0 or col >= len(self.board.board[0]):
            
            return

        next_square = self.board.board[row][col]
        if next_square and next_square == "F" or next_square in movings :

            return
        
        else:
            moves=(row,col) 
        return moves


    def move(self, direction):

        moved=[]
        target_squares=self.board.targets_squares
        moving_squares=self.board.init_moving_squares
        squares_can_move=[]
        

        delta_row, delta_col = 0, 0
        if direction == "left":
            delta_col = -1
        elif direction == "right":
            delta_col = 1
        elif direction == "up":
            delta_row = -1
        elif direction == "down":
            delta_row = 1


        row_range = (
            range(len(self.board.board) - 1, -1, -1) 
            if direction == "down" or direction=="right" else range(len(self.board.board))
        )
        col_range = (
            range(len(self.board.board[0]) - 1, -1, -1) 
            if direction == "right" or direction=="right" else range(len(self.board.board[0]))
        )
        for row in row_range:
            for col in col_range:
                square = self.board.board[row][col]
                for m_square in moving_squares:
                    if m_square.type==square:
                        the_move = self.find_moves_in_direction(row, col, delta_row, delta_col)
                        # print(the_move)
                        # new_pos = (row, col)
                        
                        arrive=False
                        
                        if the_move is not None and square not in moved:
                            # print(square,square not in moved)
                            new_pos = the_move
                            squares_can_move.append(square)

        old_positions={}
        while(True):
            # print("ksjaaaaaaajjjjjjjjjjjjjjjj")
            # print(old_positions)
            # print(self.final_positions)
            # print(squares_can_move)
            old_positions=copy.deepcopy(self.final_positions)
            
            for row in row_range:
                for col in col_range:
                    square = self.board.board[row][col]
                    for m_square in squares_can_move:
                        if m_square==square:
                            the_move = self.find_moves_in_direction(row, col, delta_row, delta_col)
                            # print(square,the_move)
                            # new_pos = (row, col)
                            
                            arrive=False
                            
                            if the_move is not None :
                                # print(square,square not in moved)
                                new_pos = the_move
                                self.final_positions[square] = new_pos
                                # print("in if",self.final_positions)
                                moved.append(square)
                                
                                for its_target in target_squares:
                                    # print(its_target.color,its_target.position.x,its_target.position.y)
                                    for moving in moving_squares:
                                    #   print(moving.color)
                                        if (
                                            moving.type==square 
                                            and moving.color==its_target.color 
                                            and its_target.position.x == new_pos[0] 
                                            and its_target.position.y == new_pos[1]
                                        ):

                                            arrive=True
                                                        
                                if(not arrive):    
                                    self.board.board[new_pos[0]][new_pos[1]]=square
                                    self.board.board[row][col]="_"
            # print(old_positions)
            # print(self.final_positions)                        
            if(old_positions == self.final_positions):
                
                break    
                            # print(f"Final position for {square} moving {direction}: {new_pos}")

        # print("\nFinal positions after moving", direction, "are:", self.final_positions)
        # print(moved)
        # print(old_positions)

        return self.final_positions,target_squares,moving_squares

class State:
    def __init__(self, board, direction):
        self.board  = copy.deepcopy(board)
        self.direction = direction
        self.next_state()


    def next_state(self):

        the_move = Move(self.board, self.direction)
        moving_types=[]
        movings_in_board=[]

        for s in the_move.moving_squares:
            moving_types.append(s.type)

        for row in range(len(self.board.board)):

            for col in range(len(self.board.board[row])):
            
                square = self.board.board[row][col]
            
                if square in moving_types :
                    movings_in_board.append(square)
                    if square in the_move.new_pos :
                        self.board.board[row][col] = "_"


        for t in the_move.target_squares:
            for m in the_move.moving_squares:
                if (
                    m.type in movings_in_board 
                    and m.color==t.color 
                    and self.board.board[t.position.x][t.position.y]=="_"
                    ):

                    self.board.board[t.position.x][t.position.y] = t.type

        for square,pos in the_move.new_pos.items():

            row, col = pos
            self.board.board[row][col] = square

            for t in the_move.target_squares:
                if t.position.x==row and t.position.y==col:
                    for m in the_move.moving_squares:
                        if t.color==m.color and m.type==square:
                            self.board.board[row][col]="_"    

        
        # self.get_board().display_board()     

        return self.board

    def get_board(self):

        return self.board 

def play_game(initial_board):
    state = State(initial_board, None)  
    print("Initial Board:")
    state.get_board().display_board()

    while True:
        direction = input("Enter your move (up, down, left, right) or 'exit' to quit: ").strip().lower()
        if direction == "exit":
            print("Game exited. Goodbye!")
            break

        if direction not in ["up", "down", "left", "right"]:
            print("Invalid direction! Please enter 'up', 'down', 'left', or 'right'.")
            continue

        state = State(state.get_board(), direction)

        if not any(square in movings for row in state.get_board().board for square in row):
            print("Congratulations! You won!")
            break


########## Test ##########

# board = Board(1)
# play_game(board)
      



      
##########  test 2 #########
# board = Board(1)
# print("Initial Board:")
# board.display_board()


# print("\nOriginal Board remains unchanged:")
# board.display_board()


# state = State(board, "down")
# print("\nNew Board after moving down:")
# state.get_board().display_board()  


# state = State(board, "left")
# print("\nNew Board after moving left:")
# state.get_board().display_board()  

# state = State(state.get_board(), "right")
# print("\nBoard after moving right:")
# state.get_board().display_board()


# state = State(state.get_board(), "left")
# print("\nBoard after moving left:")
# state.get_board().display_board()


# state = State(state.get_board(), "up")
# print("\nBoard after moving up:")
# state.get_board().display_board()


# state = State(state.get_board(), "right")
# print("\nNew Board after moving right:")
# state.get_board().display_board()  


# state = State(state.get_board(), "up")
# print("\nBoard after moving up:")
# state.get_board().display_board()

# state = State(state.get_board(), "left")
# print("\nBoard after moving left:")
# state.get_board().display_board()

# state = State(state.get_board(), "down")
# print("\nBoard after moving down:")
# state.get_board().display_board()

# state = State(state.get_board(), "down")
# print("\nBoard after moving down:")
# state.get_board().display_board()
