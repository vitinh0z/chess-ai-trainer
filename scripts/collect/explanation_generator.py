

class ExplanationGenerator:

    TEMPLATES = {

       "fork": "Esse lance cria um garfo: uma única peça passa a atacar duas peças inimigas ao mesmo tempo. "
       "O adversário só consegue salvar uma delas, então a outra fica perdida.",

        "pin": "Esse lance é uma cravada: a peça inimiga fica imobilizada, porque se ela se mover, "
        "vai expor uma peça mais valiosa (ou o próprio rei) atrás dela, na mesma linha de ataque.",

        "skewer": "Esse lance é um espeto: ataca duas peças inimigas alinhadas. "
        "Ao capturar ou forçar o movimento da peça da frente, a peça mais valiosa atrás também fica exposta ao ataque.",
    }

    def generate_explanation (self, puzzle: dict) -> str:
        fist_puzzle = puzzle["themes"][0]
        explain_theme = self.TEMPLATES[fist_puzzle]
        best_solution = puzzle["solution"][0]
        return f"O melhor lance é {best_solution}. {explain_theme}"