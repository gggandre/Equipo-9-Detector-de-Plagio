import re

def tokenize(text):
    """ Divide el texto en tokens basados en espacios y puntuación. """
    return re.findall(r'\b\w+\b', text.lower())

def remove_stopwords(tokens, stopwords):
    """ Elimina stopwords de una lista de tokens. """
    return [token for token in tokens if token not in stopwords]

def lemmatize_word(word):
    """ Aplica reglas básicas para lematización de palabras en inglés. """
    if word.endswith('ies') and len(word) > 4:
        return word[:-3] + 'y'
    elif word.endswith('es'):
        if word[-3] in 'sxz' or word[-4:-2] in ('sh', 'ch'):
            return word[:-2]
        else:
            return word[:-1]
    elif word.endswith('s'):
        return word[:-1]
    return word

def stem_words(tokens):
    """ Aplica un enfoque simple de stemming a cada token, usando lematización manual. """
    return [lemmatize_word(token) for token in tokens]

def preprocess_text(text, stopwords):
    """ Preprocesa el texto completo aplicando tokenización, remoción de stopwords y stemming. """
    tokens = tokenize(text)
    tokens = remove_stopwords(tokens, stopwords)
    return stem_words(tokens)
