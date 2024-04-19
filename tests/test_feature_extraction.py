import unittest
from src.feature_extraction import build_feature_vector

class TestFeatureExtraction(unittest.TestCase):
    def test_build_feature_vector(self):
        tokens = ['test', 'run', 'test']
        vector = build_feature_vector(tokens)
        self.assertEqual(vector, {'test': 2, 'run': 1})

if __name__ == '__main__':
    unittest.main()
