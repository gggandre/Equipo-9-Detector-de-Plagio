# utilities.py

import pandas as pd

def load_document(filepath):
    """Carga un documento desde un archivo de texto."""
    with open(filepath, 'r', encoding='latin1') as file:
        return file.read()


def load_stopwords(filepath='data/stopwords.txt'):
    """Carga una lista de stopwords desde un archivo de texto."""
    with open(filepath, 'r', encoding='utf-8') as file:
        return set(file.read().split())

def save_results_to_txt(all_results, filepath):
    """Guarda los resultados de similitud en un archivo de texto."""
    with open(filepath, 'w', encoding='utf-8') as file:
        for results in all_results:
            for result in results:
                file.write(f"{result[0]} vs {result[1]}: {result[2]*100:.2f}% similar\n")
            # Insertar separación entre grupos de resultados
            file.write("\n---\n\n")


def save_results_to_excel(results, filepath):
    """Guarda los resultados de similitud en un archivo Excel."""
    df = pd.DataFrame(results, columns=['Document 1', 'Document 2', 'Similarity'])
    df['Similarity'] = df['Similarity'] * 100  # Convertir a porcentaje
    df.to_excel(filepath, index=False)


