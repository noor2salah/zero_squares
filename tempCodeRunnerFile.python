from structure import colors, movings, targets, Square, Position, Board
from move import Move, State

import heapq
import copy

class PrioritizedBoard:
    def __init__(self, cost, board, moves):
        self.cost = cost
        self.board = board
        self.moves = moves  # Track the sequence of moves

    def __lt__(self, other):
        return self.cost < other.cost  # Compare based on cost


class UCS:
    def __init__(self, initial_board):
        self.initial_board = initial_board
        self.priority_queue = []
        self.visited_states = set()
        # Push the initial state with no moves and zero cost
        heapq.heappush(self.priority_queue, PrioritizedBoard(0, self.initial_board, []))

        print("KKKKKKKKKKKKKKKK")
    def is_goal_state(self, board):
        """
        Check if the board is in the goal state.
        """
        for target in board.targets_squares:
            target_color = target.color
            target_position = (target.position.x, target.position.y)

            found = False
            for moving_square in board.init_moving_squares:
                if (
                    moving_square.color == target_color
                    and (moving_square.position.x, moving_square.position.y) == target_position
                ):
                    found = True
                    break
            if not found:
                return False
        return True

    def get_state_key(self, board):
        """
        Generate a unique hashable key for the board's state to avoid revisiting.
        """
        state_key = []
        for row in board.board:
            state_key.append(tuple(row))
        return tuple(state_key)

    def expand_state(self, current_board):
        """
        Generate all possible next states by applying moves.
        """
        directions = ["up", "down", "left", "right"]
        next_states = []

        for direction in directions:
            state = State(current_board, direction)
            next_states.append((state.get_board(), direction))
        return next_states

    def search(self):
        """
        Perform Uniform Cost Search.
        """
        while self.priority_queue:
            current = heapq.heappop(self.priority_queue)  # Get the board with the lowest cost
            cost = current.cost
            current_board = current.board
            moves = current.moves

            # Debug: Print current state
            print(f"Exploring state with cost {cost} and moves {moves}...")
            current_board.display_board()

            # Check if the state is already visited
            state_key = self.get_state_key(current_board)
            if state_key in self.visited_states:
                print("State already visited, skipping.")
                continue
            self.visited_states.add(state_key)

            # Goal test
            if self.is_goal_state(current_board):
                # Print the solution
                print("\nGoal reached!")
                print("Total cost:", cost)
                print("Solution Path:")
                for move in moves:
                    print(f"Move: {move}")
                current_board.display_board()  # Print the final board state
                return

            # Expand current state
            for next_board, direction in self.expand_state(current_board):
                if self.get_state_key(next_board) not in self.visited_states:
                    new_moves = moves + [direction]
                    heapq.heappush(self.priority_queue, PrioritizedBoard(cost + 1, next_board, new_moves))

        print("No solution found.")
