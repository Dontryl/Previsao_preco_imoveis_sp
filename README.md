## Meu Projeto de Previsão de Preços de Imóveis em São Paulo


Olá! Bem-vindo ao meu projeto de previsão de preços de imóveis. Neste repositório, apresento o processo que segui para construir e otimizar um modelo de Machine Learning capaz de estimar valores de imóveis na cidade de São Paulo, com base em dados de abril de 2019.

Meu objetivo aqui foi documentar uma jornada realista de um projeto de ciência de dados: comecei com uma abordagem simples para criar um ponto de partida (baseline) e, a partir da análise dos seus resultados, evoluí para um modelo muito mais preciso e robusto.

Autor: Felipe Henrique Rommani Contato: www.linkedin.com/in/felipe-henrique-romani-ia ou felipe.hri@outlook.com

## Dados

Eu usei um dataset público (abril/2019) com anúncios de imóveis em São Paulo. O CSV original está no repositório. Referência: https://www.kaggle.com/code/galdinolucas/saopaulo-housing-predictions

## Atualizações
Nessa atualização eu organizei o trabalho em notebooks e módulos para deixar o fluxo reprodutível: carregamento, engenharia de features, treino e uma API para servir predições.

## Estrutura do repositório

- `preprocessing.py` — contém `load_data()` e `create_features(df)` (carregamento e engenharia de features).
- `train.py` — contém `prepare_data()`, `train_model()` e `evaluate_model()` (split, treino e métricas).
- `main.py` — orquestração do pipeline; tem CLI com `--caminho` e `--save-model` (quando salvo o modelo eu também salvo a lista `feature_columns`).
- `api.py` — API com `FastAPI` (endpoints: `/train`, `/predict`, `/health`).
- `1_modelo_baseline_regressao_linear.ipynb` — notebook do baseline (regressão linear).
- `2_modelo_avancado_random_forest.ipynb` — notebook do modelo avançado (atualizado para usar os módulos).
- `requirements.txt` — dependências.
- `.gitignore` — arquivos e artefatos ignorados.


## Como executar

1. Instale as dependências (recomendo usar um ambiente virtual):

```bash
pip install -r Requeriments.txt
```

2. Treine e salve o modelo (opcional):

```bash
python main.py --save-model modelo.pkl
```

3. Rode a API localmente:

```bash
uvicorn api:app --reload --port 8000
```

4. Exemplo de predição com `curl`:

```bash
curl -X POST "http://127.0.0.1:8000/predict" -H "Content-Type: application/json" -d '{"data": {"Rooms": 2, "Toilets": 1, "District": "Pinheiros", "Size": 50}}'
```

Observações:

- O endpoint `/predict` aplica `create_features()` ao JSON recebido e alinha as colunas com as usadas no treino (preenche colunas ausentes com 0).
- Use `POST /train` na API para treinar diretamente e gerar `modelo.pkl` no servidor.

## O que foi feito nesta atualização do repositório

Nesta atualização eu reorganizei o projeto e adicionei uma API para servir o modelo. Em resumo:

- Modularizei o pipeline
    - Criei `preprocessing.py` com `load_data()` e `create_features()`.
    - Criei `train.py` com `prepare_data()`, `train_model()` e `evaluate_model()`.
    - Atualizei `2_modelo_avancado_random_forest.ipynb` para importar os módulos e evitar duplicação de código.

- Orquestração e CLI
    - Criei `main.py` com argumentos `--caminho` e `--save-model`.
    - Ao salvar o modelo, incluo também `feature_columns` no pickle para garantir alinhamento em predições.

- API e serving
    - Adicionei `api.py` (FastAPI) com endpoints `POST /train`, `POST /predict` e `GET /health`.

- Documentação e artefatos
    - Atualizei `README.md`.
    - Atualizei `requirements.txt` (inclui `fastapi` e `uvicorn`).
    - Adicionei `.gitignore` para evitar commitar modelos e caches.

## O que eu aprendi durante essa atualização e todo o projeto. 

- A diferença prática e de performance entre modelos lineares e modelos baseados em árvores para problemas com dados complexos.
- O impacto da Engenharia de Features para fornecer mais contexto ao modelo.
- A importância de seguir um fluxo de trabalho metodológico, começando com um baseline e iterando com melhorias baseadas em diagnósticos claros.
- Como modularizar um projeto de machine learning deixando o código reusável.
- A importância de salvar metadados do treino (ex.: `feature_columns`) junto com o modelo.
- Como expor fluxo de treino e predição via API com `FastAPI`.
- Como resolver conflitos simples no Git e manter o repositório organizado.

Obrigado por visitar meu repositório!