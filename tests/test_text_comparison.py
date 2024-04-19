import unittest
from src.text_comparison import cosine_similarity

class TestTextComparison(unittest.TestCase):
    def test_cosine_similarity(self):
        vec1 = {'test': 2, 'run': 1}
        vec2 = {'test': 1, 'run': 2}
        similarity = cosine_similarity(vec1, vec2)
        self.assertAlmostEqual(similarity, 0.8, places=2)

if __name__ == '__main__':
    unittest.main()
