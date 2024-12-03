
from structure import colors,movings,targets,Square,Position,Board
from move import State


def calculate_heuristic(board):
    """
    Calculate the heuristic value of the board state based on the current positions
    of the moving squares and their targets.

    Args:
        board (Board): The current board state.

    Returns:
        int: The total heuristic value.
    """
    heuristic_value = 0

    # Iterate through all cells in the current board matrix to find moving squares
    for row in range(len(board.board)):
        for col in range(len(board.board[row])):
            square_type = board.board[row][col]
            
            if square_type in movings:  # Check if this is a moving square
                moving_color = colors[movings.index(square_type)]

                # Find the target square corresponding to this moving square
                for target in board.targets_squares:
                    if target.color == moving_color:
                        # Calculate Manhattan distance
                        distance = abs(row - target.position.x) + abs(col - target.position.y)
                        heuristic_value += distance

    return heuristic_value




################################ test #######################

# board = Board(1)
# print("Initial Board:")
# board.display_board()

# initial_heuristic = calculate_heuristic(board)
# print(f"Initial Heuristic Value: {initial_heuristic}")

# state = State(board, "down")
# print("\nBoard After Moving Down:")
# state.get_board().display_board()

# new_heuristic = calculate_heuristic(state.get_board())
# print(f"Heuristic Value After Moving Down: {new_heuristic}")

# state = State(state.get_board(), "right")
# print("\nBoard After Moving Right:")
# state.get_board().display_board()

# new_heuristic = calculate_heuristic(state.get_board())
# print(f"Heuristic Value After Moving Right: {new_heuristic}")


# state = State(state.get_board(), "up")
# print("\nBoard After Moving up:")
# state.get_board().display_board()

# new_heuristic = calculate_heuristic(state.get_board())
# print(f"Heuristic Value After Moving up: {new_heuristic}")