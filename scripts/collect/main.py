from scripts.collect.puzzle_database_downloader import PuzzleDatabaseDownloader
from scripts.collect.puzzle_filter import PuzzleFilter
from scripts.collect.puzzle_record import PuzzleRecord
from scripts.collect.puzzle_converter import PuzzleConverter
from scripts.collect.puzzle_repository import PuzzleRepository

URL = "https://database.lichess.org/lichess_db_puzzle.csv.zst"
TEMAS_QUERIDOS = {"fork", "pin", "skewer"}
LIMITE = 5000

def main():
    downloader = PuzzleDatabaseDownloader(URL)
    filtro = PuzzleFilter(TEMAS_QUERIDOS)
    conversor = PuzzleConverter()
    repositorio = PuzzleRepository("data/raw/puzzles.json")

    puzzles_aceitos = []

    for linha in downloader.streams_rows():
        record = PuzzleRecord.from_csv_row(linha)

        if filtro.accepts(record):
            puzzle = conversor.convert(record)
            puzzles_aceitos.append(puzzle)

        if len(puzzles_aceitos) >= LIMITE:
            break

    repositorio.save(puzzles_aceitos)
    print(f"Salvos {len(puzzles_aceitos)} puzzles em data/raw/puzzles.json")


if __name__ == "__main__":
    main()