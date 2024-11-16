
from structure import colors,movings,targets,Square,Position,Board
from move import Move ,State
from collections import deque
import copy

class DFSSolver:
    def __init__(self, board):
        self.board = board
        self.visited = set()  # To track visited states
        self.solution = []

    def board_to_tuple(self, board):
        # Convert the board into a tuple representation for hashing
        return tuple(tuple(row) for row in board.board)

    def is_solved(self, board):
        # Check if all moving squares are on their respective target squares
        for row in range(len(board.board)):

            for col in range(len(board.board[row])):
            
                square = board.board[row][col]

                if square in movings:
                    # print(square,row,col)
                    return False
        return True

    def dfs(self, current_board, path):
        board_tuple = self.board_to_tuple(current_board)
        
        # If the current board configuration is already visited, skip it
        if board_tuple in self.visited:
            return False

        # Mark the current board as visited
        self.visited.add(board_tuple)

        # Check if the current board configuration is the solution
        if self.is_solved(current_board):
            self.solution = path
            return True

        # Explore all possible moves
        for direction in ["down", "up", "left", "right"]:
            # Generate the next state by making a move
            next_state = State(current_board, direction)
            new_board = next_state.get_board()

            # Recursive DFS call with the new state
            
            if self.dfs(new_board, path + [direction]):

                print(path)
                
                return True

        return False

    def solve(self):
        # Start DFS from the initial board state
        if self.dfs(self.board, []):
            print("Solution found:", self.solution)
        else:
            print("No solution found")
        return self.solution
    

class BFSSolver:
    def __init__(self, board):
        self.board = board
        self.visited = set()  # To track visited states
        self.solution = []

    def board_to_tuple(self, board):
        # Convert the board into a tuple representation for hashing
        return tuple(tuple(row) for row in board.board)

    def is_solved(self, board):
        # Check if all moving squares are on their respective target squares
        for row in range(len(board.board)):
            for col in range(len(board.board[row])):
                square = board.board[row][col]
                if square in movings:
                    return False
        return True

    def bfs(self):
        # Initialize the queue with the initial state and an empty path
        queue = deque([(self.board, [])])
        
        while queue:
            current_board, path = queue.popleft()
            board_tuple = self.board_to_tuple(current_board)

            # If the current board configuration is already visited, skip it
            if board_tuple in self.visited:
                continue

            # Mark the current board as visited
            self.visited.add(board_tuple)

            # Check if the current board configuration is the solution
            if self.is_solved(current_board):
                self.solution = path
                return True

            # Explore all possible moves
            for direction in ["down", "up", "left", "right"]:
                # Generate the next state by making a move
                next_state = State(current_board, direction)
                new_board = next_state.get_board()

                # Add the new state to the queue with the updated path
                queue.append((new_board, path + [direction]))

            print(path)

        return False

    def solve(self):
        # Start BFS from the initial board state
        if self.bfs():
            print("Solution found:", self.solution)
        else:
            print("No solution found")
        return self.solution


############# Test BFS Solver ################

print("----------BFS SOLVE------------")
print()
initial_board = Board(1)
print("Initial Board:")
initial_board.display_board()
print()
solver = BFSSolver(initial_board)
solution = solver.solve()

############### Test DFS Solver ############
print()
print("--------------DFS SOLVE------------")
print()
initial_board = Board(1)
print("Initial Board:")
initial_board.display_board()
print()

solver = DFSSolver(initial_board)
solution = solver.solve()

