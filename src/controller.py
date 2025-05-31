# controller.py
from tkinter import messagebox
import model

def registrar(nombre, rol, materias_str, entry_nombre, entry_materias):
    nombre = nombre.strip().lower()
    materias = [m.strip() for m in materias_str.split(",") if m.strip()]

    if not nombre or not rol or not materias:
        messagebox.showwarning("Campos vacíos", "Por favor, completa todos los campos.")
        return

    model.registrar_usuario(nombre, rol, materias)
    messagebox.showinfo("Registro exitoso", f"{nombre} registrado como {rol}")
    entry_nombre.delete(0, "end")
    entry_materias.delete(0, "end")

def entrar_como(nombre, rol):
    usuario = model.obtener_usuario(nombre, rol)
    if not usuario:
        messagebox.showerror("Error", "Nombre incorrecto o no coincide con el rol.")
        return

    if rol == "Estudiante":
        mostrar_info_estudiante(usuario)
    elif rol == "Profesor":
        mostrar_info_profesor(usuario)
    elif rol == "Administrador":
        mostrar_info_admin()
    else:
        messagebox.showerror("Error", "Rol no reconocido.")

def mostrar_info_estudiante(usuario_data):
    nombre, rol, materias_str = usuario_data
    materias = [m.strip() for m in materias_str.split(",")]
    mensaje = "Eres estudiante. Materias:\n"
    for materia in materias:
        profesores = model.obtener_profesores(materia)
        mensaje += f"  - {materia} (Profesor: {profesores[0] if profesores else 'Ninguno'})\n"
    messagebox.showinfo("Información", mensaje)

def mostrar_info_profesor(usuario_data):
    nombre, rol, materias_str = usuario_data
    materias = [m.strip() for m in materias_str.split(",")]
    mensaje = "Eres profesor. Materias:\n"
    for materia in materias:
        estudiantes = model.obtener_estudiantes(materia)
        mensaje += f"  - {materia} (Estudiantes: {', '.join(estudiantes) if estudiantes else 'Ninguno'})\n"
    messagebox.showinfo("Información", mensaje)

def mostrar_info_admin():
    usuarios = model.obtener_todos_los_usuarios()
    mensaje = "Usuarios registrados:\n"
    roles = {"Estudiante": [], "Profesor": [], "Administrador": []}

    for nombre, rol in usuarios:
        roles[rol].append(nombre)

    for rol, nombres in roles.items():
        mensaje += f"\n{rol}s:\n"
        for nombre in nombres:
            mensaje += f"  - {nombre}\n"

    messagebox.showinfo("Información", mensaje)