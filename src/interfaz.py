# interfaz.py
import tkinter as tk
from tkinter import messagebox
from operaciones import guardar_usuario, obtener_usuario, obtener_profesores, obtener_estudiantes, obtener_todos_los_usuarios

def registrar():
    nombre = entry_nombre.get().strip().lower()
    rol = rol_var.get()
    materias = [m.strip() for m in entry_materias.get().strip().split(",") if m.strip()]

    if not nombre or not rol or not materias:
        messagebox.showwarning("Campos vacíos", "Por favor, completa todos los campos.")
        return

    guardar_usuario(nombre, rol, materias)
    messagebox.showinfo("Registro exitoso", f"{nombre} registrado como {rol}")
    entry_nombre.delete(0, tk.END)
    entry_materias.delete(0, tk.END)

def entrar_como(rol):
    nombre_input = entry_nombre.get().strip().lower()
    usuario_data = obtener_usuario(nombre_input, rol)

    if not usuario_data:
        messagebox.showerror("Error", "Nombre incorrecto o no coincide con el rol.")
        return

    if rol == "Estudiante":
        mostrar_info_estudiante(usuario_data)
    elif rol == "Profesor":
        mostrar_info_profesor(usuario_data)
    elif rol == "Administrador":
        mostrar_info_admin()
    else:
        messagebox.showerror("Error", "Rol no reconocido.")

def mostrar_info_estudiante(usuario_data):
    mensaje = "Eres estudiante. Materias:\n"
    for materia in usuario_data.get("materias", []):
        profesores = obtener_profesores(materia)
        mensaje += f"  - {materia} (Profesor: {profesores[0] if profesores else 'Ninguno'})\n"
    messagebox.showinfo("Información", mensaje)

def mostrar_info_profesor(usuario_data):
    mensaje = "Eres profesor. Materias:\n"
    for materia in usuario_data.get("materias", []):
        estudiantes = obtener_estudiantes(materia)
        mensaje += f"  - {materia} (Estudiantes: {', '.join(estudiantes) if estudiantes else 'Ninguno'})\n"
    messagebox.showinfo("Información", mensaje)

def mostrar_info_admin():
    usuarios = obtener_todos_los_usuarios()
    mensaje = "Usuarios registrados:\n"
    roles = {"Estudiante": [], "Profesor": [], "Administrador": []}
    for nombre, rol in usuarios:
        roles[rol].append(nombre)

    for rol in roles:
        mensaje += f"\n{rol}s:\n"
        for nombre in roles[rol]:
            mensaje += f"  - {nombre}\n"

    messagebox.showinfo("Información!", mensaje)

# Interfaz
ventana = tk.Tk()
ventana.title("Mini Mundo Escolar")
ventana.geometry("550x450")
ventana.configure(bg="#b1d2df")

titulo = tk.Label(ventana, text="Mini Mundo Escolar", font=("Helvetica", 18, "bold"), bg="#f0f8ff", fg="#1e3d59")
titulo.pack(pady=20)

frame = tk.Frame(ventana, bg="#f0f8ff")
frame.pack()

tk.Label(frame, text="Nombre:", font=("Arial", 12), bg="#f0f8ff").grid(row=0, column=0, padx=10, pady=5)
entry_nombre = tk.Entry(frame, font=("Arial", 12))
entry_nombre.grid(row=0, column=1, pady=5)

tk.Label(frame, text="Rol:", font=("Arial", 12), bg="#f0f8ff").grid(row=1, column=0, padx=10, pady=5)
rol_var = tk.StringVar()
roles = ["Estudiante", "Profesor", "Administrador"]
rol_menu = tk.OptionMenu(frame, rol_var, *roles)
rol_menu.grid(row=1, column=1, pady=5)

tk.Label(frame, text="Materias (separadas por coma):", font=("Arial", 12), bg="#f0f8ff").grid(row=2, column=0, columnspan=2, padx=10, pady=5)
entry_materias = tk.Entry(frame, font=("Arial", 12))
entry_materias.grid(row=3, column=0, columnspan=2, pady=5, ipadx=50)

btn_registrar = tk.Button(ventana, text="Registrar Usuario", command=registrar, bg="#4caf50", fg="white", font=("Arial", 12, "bold"))
btn_registrar.pack(pady=10)

btn_estudiante = tk.Button(ventana, text="Entrar como Estudiante", command=lambda: entrar_como("Estudiante"), bg="#2196f3", fg="white", font=("Arial", 12, "bold"))
btn_estudiante.pack(pady=5)

btn_profesor = tk.Button(ventana, text="Entrar como Profesor", command=lambda: entrar_como("Profesor"), bg="#ff9800", fg="white", font=("Arial", 12, "bold"))
btn_profesor.pack(pady=5)

btn_admin = tk.Button(ventana, text="Entrar como Administrador", command=lambda: entrar_como("Administrador"), bg="#9c27b0", fg="white", font=("Arial", 12, "bold"))
btn_admin.pack(pady=5)
ventana.mainloop()
