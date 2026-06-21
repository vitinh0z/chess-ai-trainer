from scripts.collect.game_parsers import GameParser
from scripts.collect.pgn_downloader import PgnDownloader
from scripts.collect.move_sampler import MoveSampler
from scripts.collect.json_repository import JsonRepository

URL = "https://theweekinchess.com/zips/twic1649g.zip"
SKIP_FIRST_N_MOVES = 10
SAMPLE_SIZE = 3

def main():
    downloader = PgnDownloader(URL)
    parser = GameParser()
    sampler = MoveSampler(SKIP_FIRST_N_MOVES, SAMPLE_SIZE)
    repositorio = JsonRepository("data/raw/games.json")

    texto_pgn = downloader.download()

    candidatos_totais = []
    for game in parser.parse_games(texto_pgn):
        candidatos_da_partida = sampler.sample(game)
        candidatos_totais.extend(candidatos_da_partida)

    repositorio.save(candidatos_totais)
    print(f"Salvos {len(candidatos_totais)} candidatos em data/raw/games.json")


if __name__ == "__main__":
    main()