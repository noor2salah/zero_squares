import copy
from structure import Board, movings
from move import State
from Heuristic import calculate_heuristic  # Use your existing heuristic function

def is_goal_state(state):
    board = state.get_board()
    # Check if all moving squares are on their respective target squares
    for row in range(len(board.board)):
        for col in range(len(board.board[row])):
            square = board.board[row][col]
            if square in movings:  # If there's a moving square, return False (not goal yet)
                return False
    return True  # If no moving square is found, it means the goal is reached

def simple_hill_climbing(initial_board):
    initial_state = State(initial_board, None)  # Initial state without any move
    current_state = initial_state
    visited_nodes = 0  # Counter for the number of visited nodes
    path = []  # To track the sequence of moves

    while True:
        visited_nodes += 1  # Increment visited nodes count
        current_board = current_state.get_board()
        current_heuristic = calculate_heuristic(current_board)
        
        # Flag to track if we find a better move
        found_better = False

        for direction in ["up", "down", "left", "right"]:
            next_state = State(copy.deepcopy(current_board), direction)
            next_board = next_state.get_board()
            next_heuristic = calculate_heuristic(next_board)

            # Ensure next move improves heuristic and doesn't just stop early
            if next_heuristic < current_heuristic:
                # Check if this is a valid state and a potential solution
                if is_goal_state(next_state):  # Ensure goal is reached
                    return path + [direction], visited_nodes
                
                # Move to this state if it improves heuristic
                current_state = next_state
                path.append(direction)
                found_better = True
                break  # Take the first better move immediately

        # If no better move is found, stop
        if not found_better:
            break

    return None, visited_nodes  # Return None if no solution is found

############# Test ###############
if __name__ == "__main__":
    board = Board(3)  # Initialize your board here
    print("Initial Board:")
    board.display_board()

    solution_path, visited_nodes = simple_hill_climbing(board)
    print("\nSimple Hill Climbing Results:")
    if solution_path:
        print(f"Path to solution: {solution_path}")
    else:
        print("No solution found.")
    print(f"Visited nodes: {visited_nodes}")
