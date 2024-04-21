# Autores: A01745312 - Paula Sophia Santoyo Arteaga
#          A01753176 - Gilberto André García Gaytán
#          A01379299 - Ricardo Ramírez Condado

import pandas as pd

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
        plagiarism_results (list): Lista de tuplas conteniendo los máximos de similitud encontrados para cada documento.
        filepath (str): Ruta al archivo de texto donde se guardarán los resultados.
    """
    with open(filepath, 'w', encoding='utf-8') as file:
        print(plagiarism_results)
        for results, max_similarity in zip(all_results, plagiarism_results):
            for result in results:
                file.write(f"{result[0]} vs {result[1]}: {result[2]*100:.2f}% similar\n")
            # Insertar el máximo de similitud para este documento
            file.write(f"Maximum plagiarism observed in {max_similarity[0]} vs {max_similarity[1]}: {max_similarity[2]*100:.2f}% similar\n")
            file.write("\n---\n\n")


def save_results_to_excel(results, filepath):
    """
    Guarda los resultados de similitud en un archivo Excel con las columnas Document 1, Document 2 y Similarity.
    Args:
        results (list): Lista de tuplas conteniendo los nombres de los documentos y sus similitudes.
        filepath (str): Ruta al archivo Excel donde se guardarán los resultados.
    """
    df = pd.DataFrame(results, columns=['Document 1', 'Document 2', 'Similarity'])
    df['Similarity'] = df['Similarity'] * 100  # Convertir la similitud a porcentaje
    df.to_excel(filepath, index=False)

def evaluate_results(plagiarism_results, real_labels):
    """
    Evalúa los resultados de una detección de plagio comparando los resultados esperados con los obtenidos.
    Args:
        plagiarism_results (list): Lista de resultados obtenidos (etiquetas 'plagiarism' o 'genuine').
        real_labels (list): Lista de etiquetas reales ('plagiarism' o 'genuine').
    Returns:
        tuple: Contiene los conteos de verdaderos positivos (TP), falsos positivos (FP),
        verdaderos negativos (TN) y falsos negativos (FN).
    """
    TP = FP = TN = FN = 0
    for result, real_label in zip(plagiarism_results, real_labels):
        if result == "plagiarism" and real_label == "plagiarism":
            TP += 1
        elif result == "plagiarism" and real_label == "genuine":
            FP += 1
        elif result == "genuine" and real_label == "genuine":
            TN += 1
        elif result == "genuine" and real_label == "plagiarism":
            FN += 1
    return TP, FP, TN, FN
