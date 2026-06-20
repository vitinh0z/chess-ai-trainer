class PuzzleRecord:

    def __init__(self, puzzle_id: str, fen: str, moves: list[str], themes: set[str], rating: int):
        self.puzzle_id = puzzle_id
        self.fen = fen
        self.moves = moves
        self.themes = themes
        self.rating = rating
    
    @classmethod
    def from_csv_row(cls, row: dict[str, str]) -> 'PuzzleRecord':
        puzzle_id = row["PuzzleId"]
        fen = row["FEN"]
        moves = row["Moves"].split()
        themes = set(row["Themes"].split())
        rating = int(row["Rating"])
        return cls(puzzle_id, fen, moves, themes, rating)
    



