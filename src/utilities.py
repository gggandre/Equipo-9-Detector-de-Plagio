# Autores: A01745312 - Paula Sophia Santoyo Arteaga
#          A01753176 - Gilberto André García Gaytán
#          A01379299 - Ricardo Ramírez Condado

import pandas as pd
from sklearn.metrics import roc_auc_score

def load_document(filepath):
    """
    Carga un documento desde un archivo de texto.
    Args:
        filepath (str): La ruta al archivo que se desea cargar.
    Returns:
        str: El contenido del archivo como una cadena de texto.
    """
    with open(filepath, 'r', encoding='latin1') as file:
        return file.read()

def load_stopwords(filepath='data/stopwords.txt'):
    """
    Carga una lista de stopwords desde un archivo de texto, donde cada stopword está separada por espacios.
    Args:
        filepath (str): Ruta al archivo que contiene las stopwords. Valor predeterminado a 'data/stopwords.txt'.
    Returns:
        set: Conjunto de stopwords.
    """
    with open(filepath, 'r', encoding='utf-8') as file:
        return set(file.read().split())

def save_results_to_txt(all_results, plagiarism_results, filepath):
    """
    Guarda los resultados de similitud en un archivo de texto, mostrando la comparación entre pares de documentos.
    Args:
        all_results (list): Lista de listas conteniendo resultados de similitud entre pares de documentos.
        plagiarism_results (str): Cadena que contiene los resultados de plagio para ser incluida en el archivo.
        filepath (str): Ruta al archivo de texto donde se guardarán los resultados.
    """
    with open(filepath, 'w', encoding='utf-8') as file:
        for results in all_results:
            for result in results:
                file.write(f"{result[0]} vs {result[1]}: {result[2]*100:.2f}% similar\n")
            # Insertar separación entre grupos de resultados
            file.write("\n---\n\n")
        file.write(plagiarism_results)

def save_results_to_excel(all_results, filepath):
    """
    Guarda los resultados de similitud en un archivo Excel de manera organizada en columnas.

    Args:
        all_results (list): Lista de listas que contienen tuplas con la comparación entre documentos y su similitud.
        filepath (str): Ruta al archivo Excel donde se guardarán los resultados.
    """
    # Preparar los datos para el DataFrame
    data = []
    for result_set in all_results:
        for result in result_set:
            data.append({
                'Document 1': result[0],
                'Document 2': result[1],
                'Similarity (%)': result[2] * 100  # Convertir la similitud a porcentaje
            })
    
    # Crear DataFrame con los datos
    df = pd.DataFrame(data)
    # Guardar DataFrame en un archivo Excel
    df.to_excel(filepath, index=False)

def evaluate_results(plagiarism_results, real_labels, scores):
    """
    Evalúa los resultados de una detección de plagio comparando los resultados esperados con los obtenidos,
    y calcula el AUC.
    Args:
        plagiarism_results (list): Lista de resultados obtenidos (etiquetas 'plagiarism' o 'genuine').
        real_labels (list): Lista de etiquetas reales ('plagiarism' o 'genuine').
        scores (list): Lista de puntuaciones (probabilidades o similitudes) asociadas a cada resultado.
    Returns:
        dict: Contiene los conteos de TP, FP, TN, FN y el valor de AUC.
    """
    TP = FP = TN = FN = 0
    binary_real_labels = [1 if label == "plagiarism" else 0 for label in real_labels]

    for result, real_label in zip(plagiarism_results, real_labels):
        if result == "plagiarism" and real_label == "plagiarism":
            TP += 1
        elif result == "plagiarism" and real_label == "genuine":
            FP += 1
        elif result == "genuine" and real_label == "genuine":
            TN += 1
        elif result == "genuine" and real_label == "plagiarism":
            FN += 1

    auc = roc_auc_score(binary_real_labels, scores)
    return {"TP": TP, "FP": FP, "TN": TN, "FN": FN, "AUC": auc}