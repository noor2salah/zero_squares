from structure import colors,movings,targets,Square,Position,Board
import copy
class Available_moves:
    def __init__(self, board):
        self.board = board

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



class Move:
    def __init__(self, board, direction):
        self.board = board
        self.final_positions = {}
        self.move(direction)


    def move(self, direction):
        for row in range(len(self.board.board)):
            for col in range(len(self.board.board[row])):
                square = self.board.board[row][col]
                if square in movings:
                    delta_row, delta_col = 0, 0
                    if direction == "left":
                        delta_col = -1
                    elif direction == "right":
                        delta_col = 1
                    elif direction == "up":
                        delta_row = -1
                    elif direction == "down":
                        delta_row = 1

                    the_move = Available_moves(self.board).find_moves_in_direction(row, col, delta_row, delta_col)
                    new_pos = (row, col)

                    while the_move is not None:
                        new_pos = the_move
                        the_move = Available_moves(self.board).find_moves_in_direction(new_pos[0], new_pos[1], delta_row, delta_col)

                    self.final_positions[square] = new_pos
                    # print(f"Final position for {square.type} moving {direction}: {new_pos}")

        print("\nFinal positions after moving", direction, "are:", self.final_positions)
        return self.final_positions

class State:
    def __init__(self, board, direction):
        self.board = copy.deepcopy(board)
        self.direction = direction
        self.next_state()

    def next_state(self):

        new_pos = Move(self.board, self.direction)
        
        for row in range(len(self.board.board)):
            for col in range(len(self.board.board[row])):
                square = self.board.board[row][col]
                if square in movings:
                    self.board.board[row][col] = "_"

        for pos, square in new_pos.final_positions.items():
            row, col = square
            self.board.board[row][col] = pos

        return self.board

    def get_board(self):

        return self.board    
      
##########  test  #########
board = Board(1)
print("Initial Board:")
board.display_board()

state = State(board, "left")
print("\nNew Board after moving left:")
state.get_board().display_board()  


# print("\nOriginal Board remains unchanged:")
# board.display_board()

state = State(state.get_board(), "down")
print("\nBoard after moving down:")
state.get_board().display_board()

state = State(state.get_board(), "right")
print("\nBoard after moving down:")
state.get_board().display_board()

state = State(state.get_board(), "up")
print("\nBoard after moving down:")
state.get_board().display_board()