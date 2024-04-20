import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import os
from utilities import load_document, save_results_to_txt, save_results_to_excel
from preprocessing import preprocess_text
from feature_extraction import build_feature_vector
from text_comparison import jaccard_similarity

class PlagiarismCheckerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Plagiarism Detection System")
        
        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=20, pady=20)

        self.load_btn = tk.Button(self.frame, text="Load Suspicious Documents", command=self.load_suspicious_files)
        self.load_btn.pack(side=tk.TOP, fill=tk.X)

        self.run_btn = tk.Button(self.frame, text="Check Plagiarism", command=self.check_plagiarism)
        self.run_btn.pack(side=tk.TOP, fill=tk.X)

        self.clear_btn = tk.Button(self.frame, text="Clear Results", command=self.clear_results)
        self.clear_btn.pack(side=tk.TOP, fill=tk.X)

        self.text_area = scrolledtext.ScrolledText(self.frame, wrap=tk.WORD, height=10, width=60)
        self.text_area.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
        self.original_documents = []
        self.suspicious_documents = []

    def load_suspicious_files(self):
        filenames = filedialog.askopenfilenames(title="Select Suspicious Documents", filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
        if filenames:
            self.suspicious_documents = [load_document(filename) for filename in filenames]
            self.text_area.insert(tk.END, f"Loaded {len(self.suspicious_documents)} suspicious documents.\n")
        else:
            messagebox.showinfo("Information", "No file selected.")

    def check_plagiarism(self):
        if not self.suspicious_documents or not self.original_documents:
            messagebox.showwarning("Warning", "Please load both suspicious and original documents.")
            return

        processed_suspicious_docs = [preprocess_text(doc) for doc in self.suspicious_documents]
        processed_original_docs = [preprocess_text(doc) for doc in self.original_documents]

        all_results = []  # Lista para almacenar todos los resultados

        # Iterar sobre cada documento sospechoso
        for j, suspicious_doc in enumerate(processed_suspicious_docs):
            results = []  # Lista para almacenar los resultados de este documento sospechoso
            # Iterar sobre cada documento original
            for i, original_doc in enumerate(processed_original_docs):
                similarity = jaccard_similarity(build_feature_vector(original_doc), build_feature_vector(suspicious_doc))
                results.append((f"Original Document {i+1}", f"Suspicious Document {j+1}", similarity))
                self.text_area.insert(tk.END, f"Jaccard Similarity between Original Document {i+1} and Suspicious Document {j+1}: {similarity*100:.2f}%\n")
            # Agregar los resultados de este documento sospechoso a la lista de todos los resultados
            all_results.append(results)

        save_results_to_txt(all_results, 'results/similarity_scores.txt')
        save_results_to_excel(all_results, 'results/similarity_scores.xlsx')
        messagebox.showinfo("Success", "Results saved to files.")



    def clear_results(self):
        self.text_area.delete(1.0, tk.END)

def load_original_documents(directory):
    original_documents = []
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            original_documents.append(load_document(os.path.join(directory, filename)))
    return original_documents

def main():
    root = tk.Tk()
    app = PlagiarismCheckerApp(root)
    root.mainloop()

if __name__ == '__main__':
    # Obtenemos la ruta del directorio del script
    script_dir = os.path.dirname(os.path.realpath(__file__))
    original_documents_directory = os.path.join(script_dir,"..", "data", "original")
    app = PlagiarismCheckerApp(tk.Tk())
    app.original_documents = load_original_documents(original_documents_directory)
    app.root.mainloop()
