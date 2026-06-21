

class ExplanationGenerator:

    TEMPLATES = {

       "fork": "Esse lance cria um garfo: uma única peça passa a atacar duas peças inimigas ao mesmo tempo. "
       "O adversário só consegue salvar uma delas, então a outra fica perdida.",

        "pin": "Esse lance é uma cravada: a peça inimiga fica imobilizada, porque se ela se mover, "
        "vai expor uma peça mais valiosa (ou o próprio rei) atrás dela, na mesma linha de ataque.",

        "skewer": "Esse lance é um espeto: ataca duas peças inimigas alinhadas. "
        "Ao capturar ou forçar o movimento da peça da frente, a peça mais valiosa atrás também fica exposta ao ataque.",
    }

    def generate_explanation(self, puzzle: dict) -> str:
        themes = puzzle.get("themes", [])
        best_solution = puzzle.get("solution", [None])[0]
        first_supported_theme = next((t for t in themes if t in self.TEMPLATES), None)
        if not first_supported_theme or not best_solution:
            return "Não foi possível gerar uma explicação para este puzzle."
        explain_theme = self.TEMPLATES[first_supported_theme]
        return f"O melhor lance é {best_solution}. {explain_theme}"