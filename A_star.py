import copy
from queue import PriorityQueue
from structure import colors, movings, targets, Square, Position, Board
from move import State
from Heuristic import calculate_heuristic  # Import the existing heuristic function

class Node:
    def __init__(self, state, cost, heuristic, path):
        self.state = state  # Current board state
        self.cost = cost    # Total cost to reach this state (g)
        self.heuristic = heuristic  # Heuristic (h)
        self.f = cost + heuristic  # Total cost (f = g + h)
        self.path = path  # Sequence of moves to reach this state

    def __lt__(self, other):
        return self.f < other.f  # For priority queue comparison based on f value

def is_goal_state(state):
    board = state.get_board()
    # Check if all moving squares are on their respective target squares
    for row in range(len(board.board)):
        for col in range(len(board.board[row])):
            square = board.board[row][col]
            if square in movings:  # If there's a moving square, return False (not goal yet)
                return False
    return True  # If no moving square is found, it means the goal is reached

def a_star_solve(initial_board):
    initial_state = State(initial_board, None)  # Start state without any move
    frontier = PriorityQueue()
    explored = set()

    initial_heuristic = calculate_heuristic(initial_state.get_board())  # Calculate heuristic for the start state
    frontier.put(Node(initial_state, 0, initial_heuristic, []))  # Put the start state in the frontier with f = g + h

    visited_nodes = 0  # Counter for the number of visited nodes

    while not frontier.empty():
        current_node = frontier.get()
        current_state = current_node.state

        board_hash = tuple(map(tuple, current_state.get_board().board))  # To store the board state as a tuple for hashing
        if board_hash in explored:
            continue


        if is_goal_state(current_state):
            return current_node.path, current_node.cost, visited_nodes  # Return the path, cost, and visited nodes if goal state is reached

        explored.add(board_hash)

        for direction in ["up", "down", "left", "right"]:

            visited_nodes += 1  # Increment the visited node counter

            next_state = State(current_state.get_board(), direction)
            next_board_hash = tuple(map(tuple, next_state.get_board().board))

            if next_board_hash not in explored:
                move_cost = 1  # Assuming each move has a cost of 1
                next_heuristic = calculate_heuristic(next_state.get_board())  # Calculate the heuristic for the next state
                new_path = current_node.path + [direction]
                frontier.put(Node(next_state, current_node.cost + move_cost, next_heuristic, new_path))  # Add the new node to the frontier

    return None, None, visited_nodes  # If no solution is found, return visited nodes for analysis

############# Test ###############
if __name__ == "__main__":
    board = Board(3)  # Initialize your board here
    print("Initial Board:")
    board.display_board()

    solution_path, total_cost, visited_nodes = a_star_solve(board)
    if solution_path:
        print("\nSolution found!")
        print(f"Path: {solution_path}")
        print(f"Total cost: {total_cost}")
    else:
        print("\nNo solution found.")

    print(f"Visited nodes: {visited_nodes}")
