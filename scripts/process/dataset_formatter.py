
from scripts.process.explanation_generator import ExplanationGenerator

class DatasetFormatter:

    SYSTEM_PROMPT = "Você é um treinador de xadrez experiente que explica conceitos em português brasileiro de forma didática."

    def __init__(self, explanation_generator: ExplanationGenerator):
        self.explanation_generator = explanation_generator


    def format(self, puzzle: dict) -> dict:
        
        question = f"Nesta posição: {puzzle['fen']}\nQual é o melhor lance e por quê?"
        raw_explanation = self.explanation_generator.generate_explanation(puzzle)

        return {
            "messages": [
                {"role": "system", "content": self.SYSTEM_PROMPT},
                {"role": "user", "content": question},
                {"role": "assistant", "content": raw_explanation},
            ]
        }