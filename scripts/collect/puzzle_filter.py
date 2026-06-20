class PuzzleFilter:

    def __init__(self, wanted_themes: set[str]):
        self.wanted_themes = wanted_themes
        
    def accepts(self, puzzle: 'PuzzleRecord') -> bool:
        return bool(puzzle.themes & self.wanted_themes)

    