import chess

from scripts.collect.puzzle_record import PuzzleRecord

class PuzzleConverter:

    def convert (self, record: PuzzleRecord) -> dict:

        tab = chess.Board(record.fen)
        tab.push_uci(record.moves[0])    
        fen_puzzle = tab.fen()  

        complete_solution = []
        for move in record.moves[1:]:
            moviment_solution = chess.Move.from_uci(move)
            complete_solution.append(tab.san(moviment_solution))
            tab.push_uci(move)


        return {
            "puzzle_id": record.puzzle_id,
            "fen": fen_puzzle,
            "solution": complete_solution,
            "themes": sorted(record.themes),
            "rating": record.rating
        }


        