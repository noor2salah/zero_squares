
colors=["red","blue","green","pink","yellow"]
movings=["R","B","G","P","Y"]
targets=["TR","TB","TG","TP","TY"]
# targets={"R":"TR","B":"TB","G":"TG","P":"TP","Y":"TY"}

class Position :
    def __init__(self,x,y):
        self.x=x
        self.y=y

class Square :
    def __init__(self, position , color,type ):
        if isinstance(position, Position):  
            self.position = position
        else:
            raise ValueError("position must be an instance of Position class")
        self.color = color
        self.type = type

class Board :
    def __init__(self,select_board) :
        self.board,self.targets_squares, self.init_moving_squares = self.create_board(select_board)

    def create_board(self,select_board) :
        boards = [
            
            [
                ["F", "F", "F", "F", "F", "F", "F"],
                ["F", "TG", "P", "R",  "Y","F", "F"],
            ]
            ,    
            [
                ["F", "F", "F", "F", "F", "F", "F"],
                ["F", "TR", "_", "", "_", "_", "F"],
                ["F", "_", "_", "_", "_", "_", "F"],
                ["F", "_", "_", "F", "_", "B", "F"],
                ["F", "_", "R", "G", "TG", "_", "F"],
                ["F", "_", "_", "F", "F", "TB", "F"],
                ["F", "F", "F", "F", "F", "F", "F"]
            ]
            ,
            [
                ["F", "F", "F", "F", "F", "F", "F"],
                ["F", "_", "_", "_", "_", "F", "F", "F"],
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

        targets_squares=[]
        init_moving_squares=[]
        for row in range(len(selected_board)):
            for col in range(len(selected_board[row])):
                square_type = selected_board[row][col]
                pos = Position(row, col)
                
                if square_type in movings:
                    moving = Square(pos, colors[movings.index(square_type)], square_type)
                    init_moving_squares.append(moving)

                if square_type in targets:
                    target = Square(pos, colors[targets.index(square_type)], square_type)
                    targets_squares.append(target)

        
        return selected_board,targets_squares,init_moving_squares

    def display_board(self):
        print()
        for row in self.board:
            for cell in row:
                print(cell, end=" ")  
            print()  


######## test ########
# board = Board(1)
# board.display_board()