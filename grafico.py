import tkinter as tk
from tkinter import messagebox

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Mi Primera Aplicación")
ventana.geometry("300x200")

# Función que se ejecuta cuando se presiona el botón
def saludar():
    nombre = entrada.get()
    if nombre:
        messagebox.showinfo("Saludo", f"¡Hola, {nombre}!")
    else:
        messagebox.showwarning("Advertencia", "Por favor, ingresa tu nombre")

# Crear etiqueta
etiqueta = tk.Label(ventana, text="¡Hola! Ingresa tu nombre:")
etiqueta.pack(pady=10)

# Crear campo de entrada
entrada = tk.Entry(ventana)
entrada.pack(pady=10)

# Crear botón
boton = tk.Button(ventana, text="Saludar", command=saludar)
boton.pack(pady=10)

# Iniciar el bucle principal de la aplicación
ventana.mainloop()