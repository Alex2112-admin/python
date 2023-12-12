import tkinter as tk
from tkinter import messagebox


def menu():
    try:
        ent1_value = int(ent1.get())
    except ValueError:
        messagebox.showwarning("Error", "Escribir solo números enteros.")
    else:
        if ent1_value == 1:
            vsismorresistente()
        elif ent1_value == 2:
            vperf_suelos()
        elif ent1_value == 3:
            vz_sismica()
        else:
            messagebox.showwarning("Error", "Escribir la opción correcta")

def salir():
    vprincipal.destroy()

def vsismorresistente():
    vprincipal.withdraw()
    v_sism_rres = tk.Toplevel(vprincipal)
    v_sism_rres.title("ZONAS SISMORRESISTENTE")
    v_sism_rres.geometry("550x500+0+0")
    v_sism_rres.configure(background = "light sky blue")

def vperf_suelos():
    vprincipal.withdraw()
    v_suelos = tk.Toplevel(vprincipal)
    v_suelos.title("PERFILES DE SUELOS")
    v_suelos.geometry("550x500+0+0")
    v_suelos.configure(background = "light sky blue")

#Configuración de la ventana
vprincipal = tk.Tk()
vprincipal.title("SISMICIDAD")
vprincipal.geometry("550x500")
vprincipal.configure(background="light sky blue")

#ETIQUETAS:
#Menu Principal:
...

#ENTRADAS:
#Menu Principal:
ent1 = tk.Entry(vprincipal)
ent1.pack(pady = 1, ipady = 5)

#BOTONES:
#Boton para abrir opciones:
botonmenu = tk.Button(vprincipal, text = "Aceptar", fg = "black", command = menu)
botonmenu.pack(padx = 5, pady = 5)

botonsalir = tk.Button(vprincipal, text = "Salir", fg = "black", command = salir)
botonsalir.pack(padx = 5, pady = 5)

vprincipal.mainloop()