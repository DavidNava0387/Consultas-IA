import tkinter as tk
from tkinter import messagebox
import subprocess

class menu:
    def __init__(self, root):
        self.root=root
        self.root.title("Menú")
        
        self.consulta1=tk.Button(root, text="Consulta 1", command=self.c1)
        self.consulta1.pack()
        self.consulta2=tk.Button(root, text="Consulta 2", command=self.c2)
        self.consulta2.pack()
        self.consulta3=tk.Button(root, text="Consulta 3", command=self.c3)
        self.consulta3.pack()
        self.consulta4=tk.Button(root, text="Consulta 4", command=self.c4)
        self.consulta4.pack()
        self.consulta5=tk.Button(root, text="Consulta 5", command=self.c5)
        self.consulta5.pack()
        self.consulta6=tk.Button(root, text="Consulta 6", command=self.c6)
        self.consulta6.pack()
        self.consulta7=tk.Button(root, text="Consulta 7", command=self.c7)
        self.consulta7.pack()
        self.consulta8=tk.Button(root, text="Consulta 8", command=self.c8)
        self.consulta8.pack()
        self.consulta9=tk.Button(root, text="Consulta 9", command=self.c9)
        self.consulta9.pack()
        self.consulta10=tk.Button(root, text="Consulta 10", command=self.c10)
        self.consulta10.pack()
        
    def c1(self):
        self.root.destroy()
        subprocess.Popen(["python", "Consulta 1.py"])
    def c2(self):
        self.root.destroy()
        subprocess.Popen(["python", "Consulta 2.py"])
    def c3(self):
        self.root.destroy()
        subprocess.Popen(["python", "Consulta 3.py"])
    def c4(self):
        self.root.destroy()
        subprocess.Popen(["python", "Consulta 4.py"])
    def c5(self):
        self.root.destroy()
        subprocess.Popen(["python", "Consulta 5.py"])
    def c6(self):
        self.root.destroy()
        subprocess.Popen(["python", "Consulta 6.py"])
    def c7(self):
        self.root.destroy()
        subprocess.Popen(["python", "Consulta 7.py"])
    def c8(self):
        self.root.destroy()
        subprocess.Popen(["python", "Consulta 8.py"])
    def c9(self):
        self.root.destroy()
        subprocess.Popen(["python", "Consulta 9.py"])
    def c10(self):
        self.root.destroy()
        subprocess.Popen(["python", "Consulta 10.py"])
        
if __name__=="__main__":
    root=tk.Tk()
    menu = menu(root)
    root.mainloop()
    