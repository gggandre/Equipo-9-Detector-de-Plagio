import unittest
from src.preprocessing import tokenize, remove_stopwords, stem_words

class TestPreprocessing(unittest.TestCase):
    def test_tokenize(self):
        text = "Hello, world! This is a test."
        tokens = tokenize(text)
        self.assertEqual(tokens, ['hello', 'world', 'this', 'is', 'a', 'test'])
    
    def test_remove_stopwords(self):
        tokens = ['this', 'is', 'a', 'test']
        stopwords = {'is', 'a'}
        filtered_tokens = remove_stopwords(tokens, stopwords)
        self.assertEqual(filtered_tokens, ['this', 'test'])

    def test_stem_words(self):
        tokens = ['tests', 'running', 'faster']
        stemmed_tokens = stem_words(tokens)
        self.assertEqual(stemmed_tokens, ['test', 'run', 'faster'])

if __name__ == '__main__':
    unittest.main()
