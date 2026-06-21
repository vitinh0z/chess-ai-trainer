import json

from scripts.collect.explanation_generator import ExplanationGenerator
from scripts.collect.dataset_formatter import DatasetFormatter
from scripts.collect.dataset_repository import DatasetRepository


def main():
    with open("data/raw/puzzles.json", "r", encoding="utf-8") as file:
        puzzles = json.load(file)

    gerador = ExplanationGenerator()
    formatter = DatasetFormatter(gerador)
    repositorio = DatasetRepository("data/processed/dataset.jsonl")

    exemplos_formatados = []

    for puzzle in puzzles:
        exemplo = formatter.format(puzzle)
        exemplos_formatados.append(exemplo)

    repositorio.save(exemplos_formatados)
    print(f"Salvos {len(exemplos_formatados)} exemplos em data/processed/dataset.jsonl")


if __name__ == "__main__":
    main()
