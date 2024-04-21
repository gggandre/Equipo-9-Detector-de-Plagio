# Autores: A01745312 - Paula Sophia Santoyo Arteaga
#          A01753176 - Gilberto André García Gaytán
#          A01379299 - Ricardo Ramírez Condado

import unittest
from unittest.mock import mock_open, patch
import sys
import os
# Esto agrega la carpeta 'src' al path para que puedas importar
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
import utilities

class TestUtilities(unittest.TestCase):

    def test_load_document(self):
        # Test para verificar que la función load_document carga correctamente el contenido de un archivo.
        with patch('builtins.open', mock_open(read_data="test content")) as mocked_file:
            result = utilities.load_document("fake_path.txt")
            mocked_file.assert_called_once_with("fake_path.txt", 'r', encoding='latin1')
            self.assertEqual(result, "test content")

    def test_load_stopwords(self):
        # Test para verificar que la función load_stopwords carga correctamente un conjunto de stopwords.
        stopwords_data = "stopword1\nstopword2\nstopword3"
        with patch('builtins.open', mock_open(read_data=stopwords_data)) as mocked_file:
            result = utilities.load_stopwords("fake_path.txt")
            mocked_file.assert_called_once_with("fake_path.txt", 'r', encoding='utf-8')
            self.assertEqual(result, {"stopword1", "stopword2", "stopword3"})

    def test_save_results_to_txt(self):
        # Test para verificar que se llama correctamente a la función de guardado en texto.
        results = [(("Doc1", "Doc2", 0.9),), (("Doc3", "Doc4", 0.75),)]
        max_plagiarism = [('Original Document 76', 'Suspicious Document 1', 0.6197183098591549)]
        with patch('builtins.open', mock_open()) as mocked_file:
            utilities.save_results_to_txt(results, max_plagiarism, "fake_path.txt")
            mocked_file.assert_called_once_with("fake_path.txt", 'w', encoding='utf-8')
            handle = mocked_file()
            handle.write.assert_called()  # Verifica que se llamó al menos una vez

    def test_save_results_to_excel(self):
        # Test para verificar que se llama correctamente a la función de guardado en Excel.
        results = [("Doc1", "Doc2", 0.9), ("Doc3", "Doc4", 0.75)]
        with patch('pandas.DataFrame.to_excel') as mocked_to_excel:
            utilities.save_results_to_excel(results, "fake_path.xlsx")
            mocked_to_excel.assert_called_once_with("fake_path.xlsx", index=False)

if __name__ == '__main__':
    unittest.main()
