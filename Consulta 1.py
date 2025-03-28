import tkinter as tk
from tkinter import ttk
import pandas as pd
pd.__version__

df_archivo_2=pd.read_csv("Sacramentorealestatetransactions.csv")

class consulta1:
    def __init__(self, root):
        self.root=root
        self.root.title("Consulta 1")
        
        #Consulta 1 (variables)
        self.typev="Condo"
        self.sale_date="Fri May 16 00:00:00 EDT 2008"
        self.price=100000
        self.texto1=tk.Label(self.root, text="Viviendas de tipo condominio con valor mayor a $100,000 vendidas el viernes 16 de mayo")
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
        
        self.consulta1()
        
    #Consulta 1 (funcion)    
    def consulta1(self):
        c1=df_archivo_2.query("`type`==@self.typev and `sale_date`==@self.sale_date and `price`>@self.price")
        for index, row in c1.iterrows():
            self.tree.insert("", "end", values=(row["street"], row["city"], row["zip"], row["state"], row["beds"], row["baths"], row["sq__ft"], row["type"], row["sale_date"], row["price"], row["latitude"], row["longitude"]))
                    
if __name__=="__main__":
    root=tk.Tk()
    consulta1 = consulta1(root)
    root.mainloop()    