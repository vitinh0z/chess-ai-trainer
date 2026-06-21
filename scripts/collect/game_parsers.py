import chess.pgn
import io

class GameParser:

    def parse_games(self, pgn_text: str):
        pgn_io = io.StringIO(pgn_text)
        while True:
            game = chess.pgn.read_game(pgn_io)
            if game is None:
                break
            yield game

