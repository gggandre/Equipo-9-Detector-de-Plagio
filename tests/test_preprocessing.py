import unittest
from src.preprocessing import tokenize, remove_stopwords, stem_words, preprocess_text

class TestPreprocessing(unittest.TestCase):
    def test_tokenize(self):
        # Casos de prueba para la función tokenize
        self.assertEqual(tokenize(""), [])  # Prueba con cadena vacía
        self.assertEqual(tokenize("Hello World"), ["hello", "world"])  # Prueba con una cadena simple
        self.assertEqual(tokenize("This is a test."), ["this", "is", "a", "test"])  # Prueba con puntuación
        self.assertEqual(tokenize("1 2 3"), ["1", "2", "3"])  # Prueba con números
        self.assertEqual(tokenize("special_characters!@#$%^&*()"), ["special", "characters"])  # Prueba con caracteres especiales
        self.assertEqual(tokenize("   leading_and_trailing_spaces   "), ["leading_and_trailing_spaces"])  # Prueba con espacios al principio y al final

    def test_remove_stopwords(self):
        # Casos de prueba para la función remove_stopwords
        self.assertEqual(remove_stopwords(["this", "is", "a", "test"]), ["test"])  # Prueba con palabras no stopwords
        self.assertEqual(remove_stopwords(["this", "is", "a", "test", "of", "stopwords"]), ["test"])  # Prueba con algunas stopwords
        self.assertEqual(remove_stopwords([]), [])  # Prueba con una lista vacía
        self.assertEqual(remove_stopwords([""]), [""])  # Prueba con una lista que contiene una cadena vacía
        self.assertEqual(remove_stopwords(["stopword"]), [])  # Prueba con una lista que contiene solo una stopword
        self.assertEqual(remove_stopwords(["this", "is", "a", "test", "of", "stopwords"], ["this", "is", "of"]), ["test", "stopwords"])  # Prueba con stopwords personalizadas
        self.assertEqual(remove_stopwords(["this", "is", "a", "test", "of", "stopwords"], ["this", "is", "of", "a", "test"]), [])  # Prueba con todas las palabras como stopwords

    def test_stem_words(self):
        # Casos de prueba para la función stem_words
        self.assertEqual(stem_words([]), [])  # Prueba con una lista vacía
        self.assertEqual(stem_words(["running", "walked"]), ["run", "walk"])  # Prueba con palabras verbales
        self.assertEqual(stem_words(["running", "walking", "walked"]), ["run", "walk", "walk"])  # Prueba con formas verbales diferentes
        self.assertEqual(stem_words(["running", "runs", "run"]), ["run", "run", "run"])  # Prueba con diferentes formas verbales del mismo verbo
        self.assertEqual(stem_words(["run", "runner", "running"]), ["run", "runner", "run"])  # Prueba con formas verbales diferentes y el mismo verbo
        self.assertEqual(stem_words(["happiness", "happy", "happier"]), ["happi", "happi", "happier"])  # Prueba con adjetivos
        self.assertEqual(stem_words(["eat", "eats", "eating"]), ["eat", "eat", "eat"])  # Prueba con formas verbales diferentes del verbo "eat"

    def test_preprocess_text(self):
        # Casos de prueba para la función preprocess_text
        self.assertEqual(preprocess_text(""), [])  # Prueba con cadena vacía
        self.assertEqual(preprocess_text("This is a test."), ["test"])  # Prueba con una cadena simple
        self.assertEqual(preprocess_text("Remove stopwords and Stem words"), ["remov", "stopword", "stem", "word"])  # Prueba con stopwords y stemming
        self.assertEqual(preprocess_text("This test contains numbers like 123."), ["test", "contain", "number", "like"])  # Prueba con números
        self.assertEqual(preprocess_text("¡Hola! ¿Cómo estás?"), ["hola", "cómo", "estás"])  # Prueba con caracteres no ASCII
        self.assertEqual(preprocess_text("   leading_and_trailing_spaces   "), ["leading_and_trailing_spaces"])  # Prueba con espacios al principio y al final
        self.assertEqual(preprocess_text("This text has\nnew\nlines"), ["text", "new", "line"])  # Prueba con saltos de línea


    def test_tokenize_empty_string(self):
        # Prueba con cadena vacía
        self.assertEqual(tokenize(""), [])  

    def test_tokenize_simple_string(self):
        # Prueba con una cadena simple
        self.assertEqual(tokenize("Hello World"), ["hello", "world"])  

    def test_tokenize_string_with_punctuation(self):
        # Prueba con puntuación
        self.assertEqual(tokenize("This is a test."), ["this", "is", "a", "test"])  

    def test_tokenize_string_with_numbers(self):
        # Prueba con números
        self.assertEqual(tokenize("1 2 3"), ["1", "2", "3"])  

    def test_tokenize_string_with_special_characters(self):
        # Prueba con caracteres especiales
        self.assertEqual(tokenize("special_characters!@#$%^&*()"), ["special", "characters"])  

    def test_tokenize_string_with_non_ascii_characters(self):
        # Prueba con caracteres no ASCII
        self.assertEqual(tokenize("¿Cómo estás?"), ["cómo", "estás"])  

    def test_tokenize_string_with_leading_and_trailing_spaces(self):
        # Prueba con espacios al principio y al final
        self.assertEqual(tokenize("   leading_and_trailing_spaces   "), ["leading_and_trailing_spaces"])  

    def test_remove_stopwords_custom_stopwords(self):
        # Prueba con stopwords personalizadas
        self.assertEqual(remove_stopwords(["this", "is", "a", "test", "of", "stopwords"], ["this", "is", "of"]), ["test", "stopwords"])  

    def test_stem_words_verbs(self):
        # Prueba con palabras verbales
        self.assertEqual(stem_words(["running", "walked"]), ["run", "walk"])  

    def test_stem_words_adjectives(self):
        # Prueba con adjetivos
        self.assertEqual(stem_words(["happiness", "happy", "happier"]), ["happi", "happi", "happier"])  

    def test_preprocess_text_string_with_new_lines(self):
        # Prueba con saltos de línea
        self.assertEqual(preprocess_text("This text has\nnew\nlines"), ["text", "new", "line"])  

    def test_preprocess_text_mixed_case_string(self):
        # Prueba con mayúsculas y minúsculas mixtas
        self.assertEqual(preprocess_text("ThiS iS a TesT"), ["test"])  

if __name__ == '__main__':
    unittest.main()
