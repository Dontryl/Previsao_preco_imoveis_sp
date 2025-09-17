# 🚀 Meu Projeto de Previsão de Preços de Imóveis em São Paulo

## 📝 Sobre o Projeto

Olá! Bem-vindo ao meu projeto de previsão de preços de imóveis. Neste repositório, apresento o processo que segui para construir e otimizar um modelo de Machine Learning capaz de estimar valores de imóveis na cidade de São Paulo, com base em dados de abril de 2019.

Meu objetivo aqui foi documentar uma jornada realista de um projeto de ciência de dados: comecei com uma abordagem simples para criar um ponto de partida (baseline) e, a partir da análise dos seus resultados, evoluí para um modelo muito mais preciso e robusto.

**Autor:** Felipe Henrique Rommani
**Contato:** www.linkedin.com/in/felipe-henrique-romani-ia ou felipe.hri@outlook.com 

---

## 📂 Dados Utilizados

Para este projeto, utilizei um dataset público do Kaggle, que contém informações sobre anúncios de imóveis (apartamentos e casas) para venda e aluguel em São Paulo.

* **Link para o Dataset:** [São Paulo Real Estate - April 2019](https://www.kaggle.com/code/galdinolucas/saopaulo-housing-predictions)

---

## 🏗️ Minha Metodologia e a Evolução do Modelo

Eu estruturei o projeto em dois notebooks para mostrar claramente a evolução do meu trabalho.

1.  **`1_modelo_baseline_regressao_linear.ipynb`**:
    * Minha primeira abordagem, onde utilizei um modelo de Regressão Linear para ter uma primeira estimativa da complexidade do problema e definir um baseline de performance.

2.  **`2_modelo_avancado_random_forest.ipynb`**:
    * Aqui, foco em refinar a solução. Após analisar os resultados do primeiro modelo, apliquei técnicas mais avançadas para construir uma versão final muito mais precisa.

### Etapa 1: Construindo o Modelo Baseline

Para iniciar o projeto, decidi construir um modelo de baseline utilizando **Regressão Linear**. Meu foco nesta etapa foi realizar um pré-processamento essencial, como o tratamento de variáveis categóricas (`District`, `Property Type`) através do One-Hot Encoding, para que o algoritmo pudesse processar os dados.

Os resultados foram:
* **R² (Coeficiente de Determinação): 0.49**
* **MAE (Erro Médio Absoluto): R$ 225.015,62**

Ao analisar esses números, concluí que, embora o baseline fosse um bom ponto de partida, o modelo linear era muito simples para capturar as complexas nuances do mercado imobiliário. O erro médio de previsão era muito alto para ser considerado útil na prática.

### Etapa 2: Desenvolvendo o Modelo Avançado

Para superar as limitações do modelo anterior, decidi evoluir o projeto aplicando técnicas mais sofisticadas:

1.  **Novo Algoritmo - `RandomForestRegressor`**: Optei pelo RandomForest por sua alta capacidade de modelar relações não-lineares e capturar interações complexas entre as características dos imóveis, algo que a Regressão Linear não consegue fazer tão bem.

2.  **Engenharia de Features**: Para enriquecer o modelo com mais informações, criei a feature `Total_de_comodos`, somando o número de quartos e banheiros.

3.  **Pré-processamento Robusto**: Mantive o One-Hot Encoding e adicionei o `StandardScaler` para normalizar as features, garantindo que todas tivessem a mesma escala de importância para o modelo.

---

## 📊 Resultados: A Evolução da Performance

A transição para uma abordagem mais avançada resultou em uma melhoria drástica na performance, validando minhas decisões e o potencial das técnicas aplicadas.

| Métrica | Modelo Baseline (Linear) | **Modelo Avançado (Random Forest)** |
| **R² (Coeficiente de Determinação)** | 0.49 | 0.93 |
| **MAE (Erro Médio Absoluto)** | R$ 225.015,62 | R$ 44.695,03 |

---

## 🚀 Como Executar o Projeto

Para rodar os notebooks e ver meu trabalho na prática, siga os passos:

1.  Clone este repositório:
    ```bash
    git clone (https://github.com/Dontryl/Previsao_preco_imoveis_sp.git)
    ```
2.  Navegue até o diretório do projeto:
    ```bash
    cd Previsao_preco_imoveis_sp
    ```
3.  Instale as dependências (recomendo o uso de um ambiente virtual):
    ```bash
    pip install -r requirements.txt
    ```
4.  Abra os notebooks (`.ipynb`) no seu ambiente Jupyter preferido e execute as células.

---

## 🧠 O Que Aprendi com Este Projeto

* A **diferença prática e de performance** entre modelos lineares e modelos baseados em árvores para problemas com dados complexos.
* O **impacto da Engenharia de Features** para fornecer mais contexto ao modelo.
* A importância de seguir um **fluxo de trabalho metodológico**, começando com um baseline e iterando com melhorias baseadas em diagnósticos claros.

Obrigado por visitar meu repositório!
