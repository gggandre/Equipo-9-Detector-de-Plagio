import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import re

def tokenize(text):
    """ Divide el texto en tokens, excluyendo caracteres especiales y manteniendo sólo palabras alfabéticas y números. """
    return re.findall(r'\b\w+\b', text.lower())

def remove_stopwords(tokens):
    """ Elimina stopwords de una lista de tokens. """
    stop_words = set(stopwords.words('english'))
    return [token for token in tokens if token not in stop_words]

def stem_words(tokens):
    """ Aplica stemming a cada token utilizando el algoritmo de Porter. """
    stemmer = PorterStemmer()
    return [stemmer.stem(token) for token in tokens]

def preprocess_text(text):
    """ Preprocesa el texto completo aplicando tokenización, remoción de stopwords y stemming. """
    tokens = tokenize(text)
    tokens = remove_stopwords(tokens)
    return stem_words(tokens)
