import tkinter as tk
from tkinter import ttk
import pandas as pd
pd.__version__

df_archivo_3=pd.read_csv("csv_camaras_2.csv")

class consulta7:
    def __init__(self, root):
        self.root=root
        self.root.title("Consulta 7")
        
        #Consulta 7 (variables)
        self.dimensiones=110
        self.almacenamiento=10
        self.price=100
        self.texto1=tk.Label(self.root, text="Cámaras con dimensiones de 110, almacenamineto mayor a 10 y costo mayor o igual a $100")
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
        
        self.consulta7()
        
    #Consulta 7 (funcion)    
    def consulta7(self):
        c1=df_archivo_3.query("`Storage included`>@self.almacenamiento and `Dimensions`==@self.dimensiones and `Price`>=@self.price")
        for index, row in c1.iterrows():
            self.tree.insert("", "end", values=(row["Model"], row["Zoom tele (T)"], row["Normal focus range"], row["Macro focus range"], row["Storage included"], row["Weight (inc. batteries)"], row["Dimensions"], row["Price"]))
                    
if __name__=="__main__":
    root=tk.Tk()
    consulta7 = consulta7(root)
    root.mainloop()    