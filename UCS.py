import copy
from queue import PriorityQueue
from structure import colors,movings,targets,Square,Position,Board
from move import State

class Node:
    def __init__(self, state, cost, path):
        self.state = state  # Current board state
        self.cost = cost    # Total cost to reach this state
        self.path = path    # Sequence of moves to reach this state

    def __lt__(self, other):
        return self.cost < other.cost  # For priority queue comparison

def is_goal_state(state):
    board = state.get_board()
    # Check if all moving squares are on their respective target squares
    for row in range(len(board.board)):

        for col in range(len(board.board[row])):
        
            square = board.board[row][col]

            if square in movings:
                # print(square,row,col)
                return False
    return True
def ucs_solve(initial_board):
    initial_state = State(initial_board, None)  # Start state without any move
    frontier = PriorityQueue()
    explored = set()

    frontier.put(Node(initial_state, 0, []))

    visited_nodes = 0  # Counter for the number of visited nodes

    while not frontier.empty():
        current_node = frontier.get()
        current_state = current_node.state

        board_hash = tuple(map(tuple, current_state.get_board().board))
        if board_hash in explored:
            continue

        visited_nodes += 1  # Increment the visited node counter

        if is_goal_state(current_state):
            return current_node.path, current_node.cost, visited_nodes  # Return the path, cost, and visited nodes

        explored.add(board_hash)

        for direction in ["up", "down", "left", "right"]:
            next_state = State(current_state.get_board(), direction)
            next_board_hash = tuple(map(tuple, next_state.get_board().board))

            if next_board_hash not in explored:
                move_cost = 1  # Assuming each move has a cost of 1
                new_path = current_node.path + [direction]
                frontier.put(Node(next_state, current_node.cost + move_cost, new_path))

    return None, None, visited_nodes  # Return visited nodes even if no solution is found

############# Test ###############
if __name__ == "__main__":
    board = Board(3)  # Initialize your board here
    print("Initial Board:")
    board.display_board()

    solution_path, total_cost, visited_nodes = ucs_solve(board)
    if solution_path:
        print("\nSolution found!")
        print(f"Path: {solution_path}")
        print(f"Total cost: {total_cost}")
    else:
        print("\nNo solution found.")

    print(f"Visited nodes: {visited_nodes}")
