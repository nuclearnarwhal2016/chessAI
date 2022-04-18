import piece
class board:
    """
    a data type for a chess board with arbitrary dimensions
    """
    def __init__(self) -> None:
        self.width = 8
        self.height = 8
        self.spaces = [[' '] * self.width for i in range(self.height)]

    def __repr__(self) -> str:
        pass

    def add_pieces(self):
        pass

    def move_piece(self, piece:piece.Piece, space):
        pass

    def capture_piece(self, piece:piece.Piece, piece2:piece.Piece):
        pass
  

