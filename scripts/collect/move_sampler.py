import random
import chess.pgn

class MoveSampler:

    def __init__(self, skip_first_n_moves: int, sample_size: int):
        self.skip_first_n_moves = skip_first_n_moves
        self.sample_size = sample_size

    def sample(self, game: chess.pgn.Game) -> list[dict]:
        board =game.board()
        candidates = []

        for number_moves, move in enumerate(game.mainline_moves()):
            if number_moves >= self.skip_first_n_moves:
                candidate = {
                "fen": board.fen(),
                "move": board.san(move),
                }
                candidates.append(candidate)
                
            board.push(move)

        return random.sample(candidates, min(self.sample_size, len(candidates)))