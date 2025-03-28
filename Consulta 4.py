import tkinter as tk
from tkinter import ttk
import pandas as pd
import subprocess
pd.__version__

df_archivo_2=pd.read_csv("Sacramentorealestatetransactions.csv")

class consulta4:
    def __init__(self, root):
        self.root=root
        self.root.title("Consulta 4")
        
        #Consulta 4 (variables)
        self.ciudad="SACRAMENTO"
        self.precio=95000
        self.habitaciones=2
        self.texto1=tk.Label(self.root, text="Viviendas que no sean de la ciudad de Sacramento, que valgan $95000 o más y tengan 2 o más camas")
        self.texto1.pack()
        
        self.tree=ttk.Treeview(self.root, columns=("Street", "City", "Zip", "State", "Beds", "Baths", "Sq__ft", "Type", "Sale_date", "Price", "Latitude", "Longitude"), show="headings")
        self.tree.pack(expand=True, fill="both")
        self.tree.heading("Street", text="Calle")
        self.tree.heading("City", text="Ciudad")
        self.tree.heading("Zip", text="CP")
        self.tree.heading("State", text="Estado")
        self.tree.heading("Beds", text="Habitaciones")
        self.tree.heading("Baths", text="Baños")
        self.tree.heading("Sq__ft", text="Pies cuadrados")
        self.tree.heading("Type", text="Tipo")
        self.tree.heading("Sale_date", text="Fecha")
        self.tree.heading("Price", text="Precio")
        self.tree.heading("Latitude", text="Latitud")
        self.tree.heading("Longitude", text="Longitud")
        self.tree.column("Street", width=200)
        self.tree.column("City", width=85)
        self.tree.column("Zip", width=85)
        self.tree.column("State", width=85)
        self.tree.column("Beds", width=85)
        self.tree.column("Baths", width=150)
        self.tree.column("Sq__ft", width=150)
        self.tree.column("Type", width=85)
        self.tree.column("Sale_date", width=150)
        self.tree.column("Price", width=85)
        self.tree.column("Latitude", width=100)
        self.tree.column("Longitude", width=100)
        
        self.consulta4()
        
        self.regresar=tk.Button(root, text="Regresar", command=self.regreso)
        self.regresar.pack()
            
    #Consulta 4 (funcion) 
    def consulta4(self):
        c2=df_archivo_2.query("`city`!=@self.ciudad and `price`>=@self.precio and `beds`>=@self.habitaciones")
        for index, row in c2.iterrows():
            self.tree.insert("", "end", values=(row["street"], row["city"], row["zip"], row["state"], row["beds"], row["baths"], row["sq__ft"], row["type"], row["sale_date"], row["price"], row["latitude"], row["longitude"]))
    
    def regreso(self):
        self.root.destroy()
        subprocess.Popen(["python", "Menu.py"])
        
if __name__=="__main__":
    root=tk.Tk()
    consulta4 = consulta4(root)
    root.mainloop()    