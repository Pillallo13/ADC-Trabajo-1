import tkinter as tk
from tkinter import messagebox
from sympy import symbols, simplify_logic, sympify
import string


def crear_variables(n):
    letras = string.ascii_uppercase
    if n > len(letras):
        raise ValueError("Máximo 26 variables (A-Z)")
    return symbols(" ".join(letras[:n]))


def simplificar_expresion():
    try:

        expr_str = entry_expr.get()
        expr = sympify(expr_str)
        simplificada = simplify_logic(expr)

        output_original.config(text=f"Original: {expr_str}")
        output_simplificada.config(text=f"Simplificada: {simplificada}")
    except Exception as e:
        messagebox.showerror("Error", f"Expresión inválida:\n{e}")


# Crear ventana
ventana = tk.Tk()
ventana.title("Simplificador de Expresiones Booleanas")
ventana.geometry("500x300")

# Etiqueta y entrada para número de variables

# Etiqueta y entrada para la expresión
tk.Label(ventana, text="Expresión booleana:").pack(pady=5)
entry_expr = tk.Entry(ventana, width=60)
entry_expr.pack()

# Botón para simplificar
btn = tk.Button(ventana, text="Simplificar", command=simplificar_expresion)
btn.pack(pady=10)

# Resultados
output_original = tk.Label(ventana, text="Original: ", fg="blue")
output_original.pack()

output_simplificada = tk.Label(ventana, text="Simplificada: ", fg="green")
output_simplificada.pack()

# Instrucciones
tk.Label(ventana, text="Usa operadores: & (AND), | (OR), ~ (NOT)", fg="red").pack(
    pady=10
)

# Ejecutar interfaz
ventana.mainloop()
