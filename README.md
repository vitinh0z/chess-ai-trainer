# chess-ai-trainer

Pipeline de coleta de dados, processamento e fine-tuning de um modelo de linguagem para atuar como assistente de xadrez em português brasileiro.

Projeto complementar ao [Chess Analyzer](https://github.com/vitinh0z/project-athena). O modelo treinado aqui substitui a dependência de APIs externas (Claude, GPT) dentro do Chess Analyzer.

---

## O que este repo faz

O Stockfish já cuida da análise técnica — avaliação de posições, sugestão de lances, classificação de erros. Este pipeline treina um modelo separado com uma função diferente: explicar o que aconteceu em cada lance, responder perguntas sobre xadrez e adaptar a linguagem ao nível do jogador.

---

## Estrutura

```
chess-ai-trainer/
├── data/
│   ├── raw/          # PGNs, artigos e puzzles baixados (gitignored)
│   └── processed/    # datasets JSONL prontos para treino
├── scripts/
│   ├── collect/      # coleta de dados (Lichess, Wikipedia, puzzles)
│   ├── process/      # transformação para o formato de treino
│   └── train/        # fine-tuning com LoRA
├── notebooks/        # notebooks prontos para rodar no Google Colab
├── Modelfile         # configuração para deploy com Ollama
├── requirements.txt
└── README.md
```

---

## Fontes de dados

| Fonte | Tipo | Link |
|---|---|---|
| Lichess Database | Partidas em PGN | database.lichess.org |
| Lichess Puzzles | Puzzles com tema e solução | lichess.org/api/puzzle/next |
| TWIC | Torneios profissionais semanais | theweekinchess.com |
| Wikipedia | Artigos sobre aberturas e conceitos | wikipedia.org |

---

## Formato do dataset

Cada linha do arquivo JSONL segue o padrão de mensagens para fine-tuning supervisionado:

```json
{
  "messages": [
    {
      "role": "system",
      "content": "Você é um treinador de xadrez experiente que explica conceitos em português brasileiro de forma didática."
    },
    {
      "role": "user",
      "content": "O que é um garfo no xadrez?"
    },
    {
      "role": "assistant",
      "content": "Um garfo é um ataque duplo onde uma peça ameaça duas peças inimigas ao mesmo tempo..."
    }
  ]
}
```

---

## Requisitos

```
python >= 3.10
torch
transformers
peft
trl
datasets
python-chess
```

Instale com:

```bash
pip install -r requirements.txt
```

---

## Modelo base

O fine-tuning usa LoRA (Low-Rank Adaptation), o que permite treinar em hardware modesto sem alterar o modelo base.

Modelos recomendados:

- `meta-llama/Meta-Llama-3.1-8B` — ponto de partida recomendado
- `mistralai/Mistral-7B-v0.1` — alternativa leve
- `maritaca-ai/sabia-3` — português brasileiro nativo

---

## Hardware

Você não precisa de GPU para começar. O Google Colab gratuito (T4 16GB) é suficiente para os primeiros experimentos.

| Opção | GPU | Ideal para |
|---|---|---|
| Google Colab (grátis) | T4 16GB | Experimentação inicial |
| Google Colab Pro | A100 40GB | Treino com datasets maiores |
| Vast.ai / RunPod | Variado | Treinos longos por demanda |

---

## Integração com o Chess Analyzer

Após o treino, exporte o modelo e suba com Ollama:

```bash
ollama create chess-ai -f ./Modelfile
ollama run chess-ai
```

No Chess Analyzer, configure o `.env`:

```
LLM_PROVIDER=ollama
LLM_MODEL=chess-ai
```

---

## Roadmap

- [ ] Script de coleta de puzzles via Lichess API
- [ ] Script de coleta e parsing de PGNs
- [ ] Pipeline de formatação para JSONL
- [ ] Notebook de fine-tuning no Colab (LLaMA 3.1 8B + LoRA)
- [ ] Notebook de avaliação do modelo
- [ ] Modelfile para Ollama
- [ ] Documentação de contribuição

---

## Licença

MIT
