# feature_extraction.py
from collections import Counter
from nltk.util import ngrams

def build_feature_vector(tokens, n=1):
    """ Construye un vector de características basado en la frecuencia de palabras o n-grams. """
    if n == 1:
        return Counter(tokens)
    else:
        ngram_tokens = ngrams(tokens, n)
        return Counter(ngram_tokens)
