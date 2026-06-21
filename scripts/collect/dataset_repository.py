import os
import json

class DatasetRepository:

    def __init__(self, path: str):
        self.path = path

    def save(self, examples: list[dict]) -> None:
        if directory := os.path.dirname(self.path):
            os.makedirs(directory, exist_ok=True)
        with open(self.path, "w", encoding="utf-8") as file:
            for example in examples:
                line = json.dumps(example, ensure_ascii=False)
                file.write(line + "\n")        