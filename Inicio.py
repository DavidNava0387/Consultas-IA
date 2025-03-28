import pandas as pd
import tkinter as tk
from tkinter import messagebox
import subprocess
pd.__version__

df_archivo_1=pd.read_csv("inicio_de_sesion.csv")
df_archivo_1["Usuario"] = df_archivo_1["Usuario"].astype(str).str.strip()
df_archivo_1["Password"] = df_archivo_1["Password"].astype(str).str.strip()

class inicio:
    def __init__(self, root):
        self.root=root
        self.root.title("Bienvenido")
        
        self.usuario_label=tk.Label(root,text="Usuario")
        self.usuario_label.pack()
        self.usuario_entry=tk.Entry(root)
        self.usuario_entry.pack()
        
        self.contraseña_label=tk.Label(root,text="Contraseña")
        self.contraseña_label.pack()
        self.contraseña_entry=tk.Entry(root, show="*")
        self.contraseña_entry.pack()
        
        self.iniciar=tk.Button(root, text="Iniciar sesión", command=self.verificar)
        self.iniciar.pack()
        
    def verificar(self):
        usuario=self.usuario_entry.get().strip()
        contraseña=self.contraseña_entry.get().strip()
        
        if ((df_archivo_1["Usuario"]==usuario) & (df_archivo_1["Password"]==contraseña)).any():
            self.consultas()
        else:
            messagebox.showerror("Error", "Las credenciales que ingresaste son incorrectas")
            
    def consultas(self):
        self.root.destroy()
        subprocess.Popen(["python", "Menu.py"])
        

if __name__=="__main__":
    root=tk.Tk()
    inicio = inicio(root)
    root.mainloop()