
from structure import colors,movings,targets,Square,Position,Board
from move import Move ,State
from collections import deque
import copy

class DFSSolver:
    def __init__(self, board):
        self.board = board
        self.visited = set()  
        self.solution = []

    def board_to_tuple(self, board):
        return tuple(tuple(row) for row in board.board)

    def is_solved(self, board):
        for row in range(len(board.board)):

            for col in range(len(board.board[row])):
            
                square = board.board[row][col]

                if square in movings:
                    # print(square,row,col)
                    return False
        return True

    def dfs(self, current_board, path):
        board_tuple = self.board_to_tuple(current_board)
        
        if board_tuple in self.visited:
            return False

        self.visited.add(board_tuple)

        if self.is_solved(current_board):
            self.solution = path
            return True

        for direction in ["down", "up", "left", "right"]:
            next_state = State(current_board, direction)
            new_board = next_state.get_board()

            
            if self.dfs(new_board, path + [direction]):

                print(path)
                
                return True

        return False

    def solve(self):
        if self.dfs(self.board, []):
            print("Solution found:", self.solution)
        else:
            print("No solution found")
        return self.solution
    

class BFSSolver:
    def __init__(self, board):
        self.board = board
        self.visited = set()  
        self.solution = []

    def board_to_tuple(self, board):
        return tuple(tuple(row) for row in board.board)

    def is_solved(self, board):
        for row in range(len(board.board)):
            for col in range(len(board.board[row])):
                square = board.board[row][col]
                if square in movings:
                    return False
        return True

    def bfs(self):
        queue = deque([(self.board, [])])
        
        while queue:
            current_board, path = queue.popleft()
            board_tuple = self.board_to_tuple(current_board)

            if board_tuple in self.visited:
                continue

            self.visited.add(board_tuple)

            if self.is_solved(current_board):
                self.solution = path
                return True

            for direction in ["down", "up", "left", "right"]:
                next_state = State(current_board, direction)
                new_board = next_state.get_board()

                queue.append((new_board, path + [direction]))

            print(path)

        return False

    def solve(self):
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

