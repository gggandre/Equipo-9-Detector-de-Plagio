import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from utilities import load_document, load_stopwords, save_results_to_txt, save_results_to_excel
from preprocessing import preprocess_text
from feature_extraction import build_feature_vector
from text_comparison import cosine_similarity

class PlagiarismCheckerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Plagiarism Detection System")
        
        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=20, pady=20)

        self.load_btn = tk.Button(self.frame, text="Load Documents", command=self.load_files)
        self.load_btn.pack(side=tk.TOP, fill=tk.X)

        self.run_btn = tk.Button(self.frame, text="Check Plagiarism", command=self.check_plagiarism)
        self.run_btn.pack(side=tk.TOP, fill=tk.X)

        self.text_area = scrolledtext.ScrolledText(self.frame, wrap=tk.WORD, height=10, width=60)
        self.text_area.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
        self.stopwords = load_stopwords('data/stopwords.txt')
        self.documents = []

    def load_files(self):
        filenames = filedialog.askopenfilenames(title="Select Documents", filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
        if filenames:
            self.documents = [load_document(filename) for filename in filenames]
            self.text_area.insert(tk.END, f"Loaded {len(self.documents)} documents.\n")
        else:
            messagebox.showinfo("Information", "No file selected.")

    def check_plagiarism(self):
        if not self.documents:
            messagebox.showwarning("Warning", "Please load documents first.")
            return

        processed_docs = [preprocess_text(doc, self.stopwords) for doc in self.documents]
        feature_vectors = [build_feature_vector(doc) for doc in processed_docs]

        results = []
        for i in range(len(feature_vectors)):
            for j in range(i + 1, len(feature_vectors)):
                similarity = cosine_similarity(feature_vectors[i], feature_vectors[j])
                results.append((f"Document {i+1}", f"Document {j+1}", similarity))
                self.text_area.insert(tk.END, f"Similarity between Document {i+1} and Document {j+1}: {similarity*100:.2f}%\n")

        save_results_to_txt(results, 'results/similarity_scores.txt')
        save_results_to_excel(results, 'results/similarity_scores.xlsx')
        messagebox.showinfo("Success", "Results saved to files.")

def main():
    root = tk.Tk()
    app = PlagiarismCheckerApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()
