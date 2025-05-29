# controller.py
from Modelado.src.model import (
    registrar_usuario,
    obtener_usuario,
    obtener_profesores,
    obtener_estudiantes,
    obtener_todos_los_usuarios
)

def manejar_registro(nombre, rol, materias):
    if not nombre or not rol or not materias:
        return False, "Por favor, completa todos los campos."

    registrar_usuario(nombre, rol, materias)
    return True, f"{nombre} registrado como {rol}"

def manejar_ingreso(nombre, rol):
    usuario = obtener_usuario(nombre, rol)
    if not usuario:
        return None, "Nombre incorrecto o no coincide con el rol."

    nombre, rol, materias_str = usuario
    materias = [m.strip() for m in materias_str.split(",") if m.strip()]
    return {"nombre": nombre, "rol": rol, "materias": materias}, None

def obtener_info_estudiante(usuario):
    mensaje = "Eres estudiante. Materias:\n"
    for materia in usuario["materias"]:
        profesores = obtener_profesores(materia)
        prof = profesores[0] if profesores else "Ninguno"
        mensaje += f"  - {materia} (Profesor: {prof})\n"
    return mensaje

def obtener_info_profesor(usuario):
    mensaje = "Eres profesor. Materias:\n"
    for materia in usuario["materias"]:
        estudiantes = obtener_estudiantes(materia)
        est = ", ".join(estudiantes) if estudiantes else "Ninguno"
        mensaje += f"  - {materia} (Estudiantes: {est})\n"
    return mensaje

def obtener_info_admin():
    mensaje = "Usuarios registrados:\n"
    roles = {"Estudiante": [], "Profesor": [], "Administrador": []}
    for nombre, rol in obtener_todos_los_usuarios():
        roles[rol].append(nombre)

    for rol, nombres in roles.items():
        mensaje += f"\n{rol}s:\n"
        for n in nombres:
            mensaje += f"  - {n}\n"
    return mensaje