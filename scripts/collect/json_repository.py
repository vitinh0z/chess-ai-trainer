import json
import os

class JsonRepository:

    def __init__(self, path: str):
        self.path = path

    def save(self, puzzles: list[dict]) -> None:
        if directory := os.path.dirname(self.path):
            os.makedirs(directory, exist_ok=True)
        with open(self.path, "w", encoding="utf-8") as file:
            json.dump(puzzles, file, ensure_ascii=False, indent=2)
            