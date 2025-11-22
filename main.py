from preprocessing import load_data, create_features
from train import prepare_data, train_model, evaluate_model
import argparse
import pickle


def main(caminho_arquivo: str = None, save_model_path: str = None):
	# 1) Carregar dados
	df = load_data(caminho_arquivo)

	# 2) Criar features
	df_encoded = create_features(df)

	# 3) Preparar dados e dividir
	X_train, X_test, y_train, y_test = prepare_data(df_encoded, target_col="Price")

	# 4) Treinar modelo diretamente com X (Random Forest não depende de escala)
	model = train_model(X_train, y_train)

	# 5) Avaliar
	metrics = evaluate_model(model, X_test, y_test)

	print("--- Resultados do Treinamento ---")
	print(f"R²: {metrics['r2']:.2f}")
	print(f"MAE: R$ {metrics['mae']:,.2f}")

	if save_model_path:
		# Salvar modelo junto com as colunas de features usadas no treino
		# para garantir alinhamento na fase de predição
		feature_columns = X_train.columns.tolist()
		payload = {"model": model, "feature_columns": feature_columns}
		with open(save_model_path, "wb") as f:
			pickle.dump(payload, f)
		print(f"Modelo salvo em: {save_model_path} (com feature_columns)")


def _parse_args():
	parser = argparse.ArgumentParser(description="Pipeline de treino de modelo de preços")
	parser.add_argument("--caminho", type=str, default=None, help="Caminho para o CSV de dados")
	parser.add_argument("--save-model", type=str, default=None, help="Caminho para salvar o modelo treinado (pickle)")
	return parser.parse_args()


if __name__ == "__main__":
	args = _parse_args()
	main(caminho_arquivo=args.caminho, save_model_path=args.save_model)

