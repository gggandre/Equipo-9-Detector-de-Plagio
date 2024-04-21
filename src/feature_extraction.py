# Autores: A01745312 - Paula Sophia Santoyo Arteaga
#          A01753176 - Gilberto André García Gaytán
#          A01379299 - Ricardo Ramírez Condado

from collections import Counter
from nltk.util import ngrams

def build_feature_vector(tokens, n=1):
    """
    Construye un vector de características basado en la frecuencia de palabras o n-grams.
    Parámetros:
    tokens (list): Lista de palabras o tokens de un texto.
    n (int): El número de elementos en los n-grams; por defecto es 1, lo que significa unigramas.
    Retorna:
    Counter: Un objeto contador que mapea cada palabra o n-gram a su frecuencia en los tokens.
    """
    if n == 1:
        return Counter(tokens)
    else:
        ngram_tokens = ngrams(tokens, n)
        return Counter(ngram_tokens)
