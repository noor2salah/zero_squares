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

def steepest_ascent_hill_climbing(initial_board):
    initial_state = State(initial_board, None)  # Initial state without any move
    current_state = initial_state
    visited_nodes = 0  # Counter for the number of visited nodes
    path = []  # To track the sequence of moves

    while True:
        visited_nodes += 1  # Increment visited nodes count
        current_board = current_state.get_board()
        current_heuristic = calculate_heuristic(current_board)

        # Store the best next state and move
        best_next_state = None
        best_move = None
        best_heuristic = current_heuristic

        # Evaluate all possible moves
        for direction in ["up", "down", "left", "right"]:
            next_state = State(copy.deepcopy(current_board), direction)
            next_board = next_state.get_board()
            next_heuristic = calculate_heuristic(next_board)

            # Update if this move gives a better heuristic
            if next_heuristic < best_heuristic:
                best_next_state = next_state
                best_move = direction
                best_heuristic = next_heuristic

        # If no better state is found, stop
        if best_next_state is None:
            break

        # Move to the best next state
        current_state = best_next_state
        path.append(best_move)

        # Check if the goal is reached
        if is_goal_state(current_state):
            return path, visited_nodes

    return None, visited_nodes  # Return None if no solution is found

############# Test ###############
if __name__ == "__main__":
    board = Board(3)  # Initialize your board here
    print("Initial Board:")
    board.display_board()

    solution_path, visited_nodes = steepest_ascent_hill_climbing(board)
    print("\nSteepest-Ascent Hill Climbing Results:")
    if solution_path:
        print(f"Path to solution: {solution_path}")
    else:
        print("No solution found.")
    print(f"Visited nodes: {visited_nodes}")
