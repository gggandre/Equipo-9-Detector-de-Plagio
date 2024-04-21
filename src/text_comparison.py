# text_comparison.py

def jaccard_similarity(vec1, vec2):
    #"""Calcula la similitud de Jaccard entre dos vectores de características."""
    intersection = set(vec1.keys()) & set(vec2.keys())
    union = set(vec1.keys()) | set(vec2.keys())
    
    if len(union) == 0:
        return 1.0  # Si ambos conjuntos son vacíos, la similitud de Jaccard es 1.0
    else:
        return len(intersection) / len(union)

