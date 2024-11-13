
colors=["red","blue","green","pink","yellow"]
movings=["R","B","G","P","Y"]
targets=["TR","TB","TG","TP","TY"]


class Position :
    def __init__(self,x,y):
        self.x=x
        self.y=y

class Square :
    def __init__(self, position , color ):
        if isinstance(position, Position):  # Check to ensure position is a Position object
            self.position = position
        else:
            raise ValueError("position must be an instance of Position class")
        self.color = color

class Board :
    def __init__(self,select_board) :
        self.board = self.create_board(select_board)

    def create_board(self,select_board) :
        boards = [
            
            [
                ["F", "F", "F", "F", "F", "F", "F"],
                ["F", "TG", "P", "R",  "Y","F", "F"],
            ]
            ,    
            [
                ["F", "F", "F", "F", "F", "F", "F"],
                ["F", "TB", "_", "TG", "_", "_", "F"],
                ["F", "_", "_", "_", "_", "_", "F"],
                ["F", "_", "", "F", "_", "B", "F"],
                ["F", "_", "R", "G", "_", "_", "F"],
                ["F", "_", "_", "F", "F", "TR", "F"],
                ["F", "F", "F", "F", "F", "F", "F"]
            ]
            ,
            [
                ["F", "F", "F", "F", "F", "F", "F"],
                ["F", "_", "_", "_", "_", "_", "F", "F"],
                ["F", "_", "_", "_", "_", "B", "_", "F"],
                ["F", "TR", "_", "F", "_", "_","_", "F"],
                ["_", "F", "_", "R", "_", "_","_", "F"],
                ["_", "F", "_", "_", "F", "_", "_", "F"],
                ["_", "F", "_", "_", "_", "_", "TB", "F"],
                ["_", "F", "F", "F", "F", "F", "F", "F"]
            ]
            ,
            [
                ["_", "F", "F", "F", "F", "F", "_", "_", "_", "_", "_"],
                ["F", "F", "R", "_", "_", "F", "F", "F", "F", "F", "_"],
                ["F", "_", "_", "_", "_", "F", "F", "TB", "_", "F", "_"],
                ["F", "_", "_", "_", "_", "_", "_", "_", "_", "F", "F"],
                ["F", "_", "_", "_", "F", "F", "F", "_", "_", "TR", "F"],
                ["F", "_", "_", "_", "_", "_", "_", "_", "_", "F", "F"],
                ["F", "F", "B", "_", "F", "F", "F", "F", "F", "F", "_"],
                ["_", "F", "F", "F", "F", "_", "_", "_", "_", "_", "_"],
            ]

        ]

        selected_board = boards[select_board]
        
        return selected_board

    def display_board(self):
        # Loop through each row in the 2D list
        for row in self.board:
            for cell in row:
                print(cell, end=" ")  # Print each cell followed by a space
            print()  # Move to the next line after each row

# board = Board(1)
# board.display_board()