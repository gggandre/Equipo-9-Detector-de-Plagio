# Autores: A01745312 - Paula Sophia Santoyo Arteaga
#          A01753176 - Gilberto André García Gaytán
#          A01379299 - Ricardo Ramírez Condado

import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import os
import pandas as pd
from utilities import load_document, save_results_to_txt, save_results_to_excel, evaluate_results, roc_auc_score, evaluate_results
from preprocessing import preprocess_text
from feature_extraction import build_feature_vector
from text_comparison import jaccard_similarity

class PlagiarismCheckerApp:
    """Clase que implementa la interfaz de usuario para un sistema de detección de plagio usando Tkinter."""
    def __init__(self, root):
        """
        Inicializa la interfaz de usuario del sistema de detección de plagio.
        Args:
            root (tk.Tk): Ventana principal de la aplicación Tkinter.
        """
        self.root = root
        self.root.title("Plagiarism Detection System")
        self.root.geometry("800x600")  # Establece las dimensiones de la ventana
        self.root.configure(background="#FEFAF6")  # Configura el color de fondo de la ventana
        # Inicialización de componentes de la interfaz de usuario
        self.frame = tk.Frame(self.root, bg="black")
        self.frame.pack(padx=20, pady=20)
        # Botones para cargar documentos y verificar el plagio
        self.load_btn = tk.Button(self.frame, text="Load Suspicious Documents", command=self.load_suspicious_files, bg="#EADBC8", fg="black")
        self.load_btn.pack(side=tk.TOP, fill=tk.X)
        self.run_btn = tk.Button(self.frame, text="Check Plagiarism", command=self.check_plagiarism, bg="#EADBC8", fg="black")
        self.run_btn.pack(side=tk.TOP, fill=tk.X)
        self.clear_btn = tk.Button(self.frame, text="Clear Results", command=self.clear_results, bg="#102C57", fg="white")
        self.clear_btn.pack(side=tk.BOTTOM, fill=tk.X)
        # Área de texto para mostrar resultados
        self.text_area = scrolledtext.ScrolledText(self.frame, wrap=tk.WORD, bg="#FEFAF6")
        self.text_area.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
        self.original_documents = []
        self.suspicious_documents = []

    def load_suspicious_files(self):
        """
        Carga archivos sospechosos usando un diálogo de archivo y los añade a la lista de documentos sospechosos.
        """
        filenames = filedialog.askopenfilenames(title="Select Suspicious Documents", filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
        if filenames:
            self.suspicious_documents = [load_document(filename) for filename in filenames]
            self.text_area.insert(tk.END, f"Loaded {len(self.suspicious_documents)} suspicious documents.\n")
        else:
            messagebox.showinfo("Information", "No file selected.")

    def check_plagiarism(self):
        """
        Verifica el plagio comparando documentos sospechosos con documentos originales y muestra los resultados.
        """
        if not self.suspicious_documents or not self.original_documents:
            messagebox.showwarning("Warning", "Please load both suspicious and original documents.")
            return
        
        # Proceso de detección de plagio
        processed_suspicious_docs = [preprocess_text(doc) for doc in self.suspicious_documents]
        processed_original_docs = [preprocess_text(doc) for doc in self.original_documents]
        plagiarism_results, real_labels, all_results, scores = [], [], [], []
        
        # Umbral de similitud para considerar un documento como plagiado
        SIMILARITY_THRESHOLD = 0.8  # Este es un valor aproximado
        
        for j, suspicious_doc in enumerate(processed_suspicious_docs):
            max_similarity, plagiarism_result = 0, "genuine"
            results = []
            
            for i, original_doc in enumerate(processed_original_docs):
                similarity = jaccard_similarity(build_feature_vector(original_doc), build_feature_vector(suspicious_doc))
                results.append((f"Original Document {i+1}", f"Suspicious Document {j+1}", similarity))
                if similarity > max_similarity:
                    max_similarity = similarity
                    plagiarism_result = "plagiarism" if similarity >= SIMILARITY_THRESHOLD else "genuine"
            all_results.append(results)
            plagiarism_results.append(plagiarism_result)
            # La etiqueta real se basaría en si supera el umbral de similitud
            real_labels.append(plagiarism_result)
            scores.append(max_similarity)  # Guarda la máxima similitud encontrada para uso en el cálculo del AUC
            
            # Ordenar los resultados por similitud y obtener el top 5
            sorted_results = sorted(results, key=lambda x: x[2], reverse=True)[:5]
            self.text_area.insert(tk.END, f"\nTop 5 most similar original documents to Suspicious Document {j+1}:\n")
            for result in sorted_results:
                self.text_area.insert(tk.END, f"{result[0]} with {result[1]}: {result[2]*100:.2f}% similar\n")
        
        # Manejo de la diversidad de clases para el cálculo de AUC
        if len(set(real_labels)) < 2:
            messagebox.showwarning("AUC Calculation", "AUC cannot be calculated with only one class present in real labels.")
        else:
            # Evaluación de resultados
            evaluation_results = evaluate_results(plagiarism_results, real_labels, scores)
            # Calcular AUC utilizando sklearn.metrics.roc_auc_score
            evaluation_results = evaluate_results(plagiarism_results, real_labels, scores)
            TP, FP, TN, FN, auc_score = evaluation_results.values()
            messagebox.showinfo("Plagiarism Check Results", f"True Positives: {TP}\nFalse Positives: {FP}\nTrue Negatives: {TN}\nFalse Negatives: {FN}\nAUC: {auc_score:.2f}")
        # Guardar resultados en archivos
        # Concatena los resultados de plagio en una cadena de texto
        plagiarism_results_str = "\n".join(f"Suspicious Document {i+1} detected as {result}" for i, result in enumerate(plagiarism_results))
        # Guardar resultados en archivo de texto
        save_results_to_txt(all_results, plagiarism_results_str, 'results/similarity_scores.txt')
        save_results_to_excel(all_results, 'results/similarity_scores.xlsx')
        messagebox.showinfo("Success", "Results saved to text and Excel files.")

    def clear_results(self):
        """
        Limpia los resultados mostrados en la interfaz gráfica.
        """
        self.text_area.delete(1.0, tk.END)

def load_original_documents(directory):
    """
    Carga documentos originales de un directorio especificado.
    Args:
        directory (str): Ruta del directorio donde se encuentran los documentos originales.
    Returns:
        list: Lista de documentos originales cargados.
    """
    original_documents = []
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            original_documents.append(load_document(os.path.join(directory, filename)))
    return original_documents

def main():
    """
    Función principal para ejecutar la aplicación de detección de plagio.
    """
    root = tk.Tk()
    app = PlagiarismCheckerApp(root)
    root.mainloop()

if __name__ == '__main__':
    # Obtenemos la ruta del directorio del script
    script_dir = os.path.dirname(os.path.realpath(__file__))
    original_documents_directory = os.path.join(script_dir, "..", "data", "original")
    app = PlagiarismCheckerApp(tk.Tk())
    app.original_documents = load_original_documents(original_documents_directory)
    app.root.mainloop()
