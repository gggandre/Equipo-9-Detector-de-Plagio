# Autores: A01745312 - Paula Sophia Santoyo Arteaga
#          A01753176 - Gilberto André García Gaytán
#          A01379299 - Ricardo Ramírez Condado

import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import re

def tokenize(text):
    """
    Divide el texto en tokens, eliminando caracteres especiales y conservando solo palabras alfabéticas y números.
    Args:
        text (str): Texto a tokenizar.
    Returns:
        list: Lista de tokens extraídos del texto.
    """
    # Utiliza expresiones regulares para encontrar palabras o números
    return re.findall(r'\b\w+\b', text.lower())

def remove_stopwords(tokens):
    """
    Elimina las stopwords de una lista de tokens.
    Args:
        tokens (list): Lista de tokens.
    Returns:
        list: Lista de tokens sin stopwords.
    """
    # Obtiene el conjunto de stopwords del inglés
    stop_words = set(stopwords.words('english'))
    # Filtra los tokens para remover las stopwords
    return [token for token in tokens if token not in stop_words]

def stem_words(tokens):
    """
    Aplica el proceso de stemming a cada token utilizando el algoritmo de Porter.
    Args:
        tokens (list): Lista de tokens a los cuales se les aplicará stemming.
    Returns:
        list: Lista de tokens después de aplicar stemming.
    """
    # Instancia un objeto PorterStemmer
    stemmer = PorterStemmer()
    # Aplica stemming a cada token
    return [stemmer.stem(token) for token in tokens]

def preprocess_text(text):
    """
    Preprocesa el texto realizando tokenización, eliminación de stopwords y stemming en secuencia.
    Args:
        text (str): Texto a preprocesar.
    Returns:
        list: Lista de tokens preprocesados.
    """
    # Aplica tokenización
    tokens = tokenize(text)
    # Elimina stopwords
    tokens = remove_stopwords(tokens)
    # Aplica stemming
    return stem_words(tokens)
