import tkinter as tk
from tkinter import messagebox
import subprocess
import os

class GraphAnalyzerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Бабабой")
        self.create_gui()

    def create_gui(self):
        # Buttons for selecting graph, tree, and compression
        graph_button = tk.Button(self.master, text="Граф", command=self.open_graph)
        graph_button.pack(side=tk.LEFT, padx=5)

        tree_button = tk.Button(self.master, text="Дерево", command=self.open_tree)
        tree_button.pack(side=tk.LEFT, padx=5)

        compression_button = tk.Button(self.master, text="Сжатие", command=self.open_compression)
        compression_button.pack(side=tk.LEFT, padx=5)

    def open_graph(self):
        self.execute_file("graph.py")

    def open_tree(self):
        self.execute_file("tree.py")

    def open_compression(self):
        self.execute_file("shf.py")

    def execute_file(self, file_name):
        file_path = os.path.join(os.getcwd(), file_name)
        try:
            subprocess.run(["python", file_path], check=True, shell=True)
            messagebox.showinfo("Успех", f"Файл {file_path} успешно выполнен.")
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Ошибка", f"Ошибка при выполнении файла {file_path}: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = GraphAnalyzerApp(root)
    root.mainloop()