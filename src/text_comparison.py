def cosine_similarity(vec1, vec2):
    """ Calcula la similitud del coseno entre dos vectores de características. """
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x]**2 for x in vec1.keys()])
    sum2 = sum([vec2[x]**2 for x in vec2.keys()])
    denominator = (sum1**0.5) * (sum2**0.5)
    
    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator
