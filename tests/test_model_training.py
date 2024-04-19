# tests/test_model_training.py
import unittest
from src.model_training import train_model

class TestModelTraining(unittest.TestCase):
    def test_train_model(self):
        documents = ["This is a document.", "This is another document."]
        labels = [0, 1]
        model, vectorizer = train_model(documents, labels)
        self.assertEqual(len(model.support_vectors_), 2)  # Verificar que el modelo se ha entrenado con dos vectores

if __name__ == '__main__':
    unittest.main()
