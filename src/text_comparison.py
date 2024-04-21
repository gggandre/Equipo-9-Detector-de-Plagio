# Autores: A01745312 - Paula Sophia Santoyo Arteaga
#          A01753176 - Gilberto André García Gaytán
#          A01379299 - Ricardo Ramírez Condado

def jaccard_similarity(vec1, vec2):
    """
    Calcula la similitud de Jaccard entre dos vectores de características, que son diccionarios donde las llaves son los
    elementos y los valores son las frecuencias de esos elementos.
    La similitud de Jaccard se define como el tamaño de la intersección dividido por el tamaño de la unión de los conjuntos
    de llaves de ambos vectores.
    Args:
        vec1 (dict): Primer vector de características.
        vec2 (dict): Segundo vector de características.
    Returns:
        float: Coeficiente de similitud de Jaccard, que varía entre 0 (sin similitud) y 1 (idénticos), inclusive.
    """
    # Determina la intersección de las llaves de ambos vectores
    intersection = set(vec1.keys()) & set(vec2.keys())
    # Determina la unión de las llaves de ambos vectores
    union = set(vec1.keys()) | set(vec2.keys())
    
    # Maneja el caso especial donde ambos vectores son vacíos
    if len(union) == 0:
        return 1.0  # Si ambos conjuntos son vacíos, la similitud de Jaccard es 1.0
    else:
        # Calcula la similitud de Jaccard como el tamaño de la intersección dividido por el tamaño de la unión
        return len(intersection) / len(union)

