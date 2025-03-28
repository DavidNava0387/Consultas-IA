import tkinter as tk
from tkinter import ttk
import pandas as pd
import subprocess
pd.__version__

df_archivo_3=pd.read_csv("csv_camaras_2.csv")

class consulta9:
    def __init__(self, root):
        self.root=root
        self.root.title("Consulta 9")
        
        #Consulta 9 (variables)
        self.zoom=200
        self.dimensiones=70
        self.price=130
        self.texto1=tk.Label(self.root, text="Cámaras con un zoom de mínimo 200 de dimensiones iguales a mayores a 70 que cuesten mas de $130")
        self.texto1.pack()
        
        self.tree=ttk.Treeview(self.root, columns=("Model", "Zoom tele (T)", "Normal focus range", "Macro focus range", "Storage included", "Weight (inc. batteries)", "Dimensions", "Price"), show="headings")
        self.tree.pack(expand=True, fill="both")
        self.tree.heading("Model", text="Modelo")
        self.tree.heading("Zoom tele (T)", text="Zoom tele")
        self.tree.heading("Normal focus range", text="Enfoque normal")
        self.tree.heading("Macro focus range", text="Enfoque macro ")
        self.tree.heading("Storage included", text="Almacenamiento")
        self.tree.heading("Weight (inc. batteries)", text="Peso con pilas")
        self.tree.heading("Dimensions", text="Dimensiones")
        self.tree.heading("Price", text="Precio")
        self.tree.column("Model", width=200)
        self.tree.column("Zoom tele (T)", width=85)
        self.tree.column("Normal focus range", width=85)
        self.tree.column("Macro focus range", width=85)
        self.tree.column("Storage included", width=85)
        self.tree.column("Weight (inc. batteries)", width=150)
        self.tree.column("Dimensions", width=150)
        self.tree.column("Price", width=85)
        
        self.consulta9()
        
        self.regresar=tk.Button(root, text="Regresar", command=self.regreso)
        self.regresar.pack()
        
    #Consulta 9 (funcion)    
    def consulta9(self):
        c1=df_archivo_3.query("`Zoom tele (T)`>=@self.zoom and `Dimensions`>=@self.dimensiones and `Price`>=@self.price")
        for index, row in c1.iterrows():
            self.tree.insert("", "end", values=(row["Model"], row["Zoom tele (T)"], row["Normal focus range"], row["Macro focus range"], row["Storage included"], row["Weight (inc. batteries)"], row["Dimensions"], row["Price"]))
    
    def regreso(self):
        self.root.destroy()
        subprocess.Popen(["python", "Menu.py"])
                    
if __name__=="__main__":
    root=tk.Tk()
    consulta9 = consulta9(root)
    root.mainloop()    