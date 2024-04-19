from collections import Counter

def build_feature_vector(tokens):
    """ Construye un vector de características basado en la frecuencia de palabras. """
    return Counter(tokens)
