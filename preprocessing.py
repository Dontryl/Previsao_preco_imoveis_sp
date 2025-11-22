import pandas as pd
import numpy as np
import seaborn as sns


def load_data(caminho_arquivo: str = None) -> pd.DataFrame:
	"""Carrega o CSV e retorna um DataFrame.

	Se nenhum caminho for fornecido, usa o arquivo padrão do projeto.
	"""
	if caminho_arquivo is None:
		caminho_arquivo = r"C:\Users\lipin\OneDrive\Área de Trabalho\Projetos de AI\sao-paulo-properties-april-2019.csv"
	df = pd.read_csv(caminho_arquivo)
	return df


if __name__ == "__main__":
	# Comportamento útil ao executar o arquivo diretamente
	df = load_data()
	print(df)


def create_features(df: pd.DataFrame) -> pd.DataFrame:
	"""Cria features adicionais e aplica encoding nas colunas categóricas.

	- Adiciona a coluna `Total_de_comodos` como Rooms + Toilets
	- Aplica `pd.get_dummies` nas colunas categóricas usadas no notebook original
	"""
	df = df.copy()
	# Criar a feature solicitada no notebook
	if "Rooms" in df.columns and "Toilets" in df.columns:
		df["Total_de_comodos"] = df["Rooms"] + df["Toilets"]

	# Colunas categóricas que o notebook usava
	cat_cols = [c for c in ["District", "Negotiation Type", "Property Type"] if c in df.columns]
	if cat_cols:
		df_encoded = pd.get_dummies(df, columns=cat_cols, drop_first=True)
	else:
		df_encoded = df

	return df_encoded