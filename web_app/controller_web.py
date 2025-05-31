import model

def manejar_registro(nombre, rol, materias):
    if not nombre or not rol or not materias:
        return False, "Por favor, completa todos los campos."
    model.registrar_usuario(nombre, rol, materias)
    return True, f"{nombre} registrado como {rol}"

def manejar_ingreso(nombre, rol):
    usuario = model.obtener_usuario(nombre, rol)
    if not usuario:
        return None, "Nombre incorrecto o no coincide con el rol."
    return usuario, None

def obtener_info_estudiante(usuario_data):
    if not usuario_data or len(usuario_data) != 3:
        return "Error al obtener datos del estudiante."
    
    nombre, rol, materias_str = usuario_data
    materias = [m.strip() for m in materias_str.split(",") if m.strip()]
    mensaje = "Eres estudiante. Materias:<br>"
    for materia in materias:
        profesores = model.obtener_profesores(materia)
        mensaje += f"- {materia} (Profesor: {profesores[0] if profesores else 'Ninguno'})<br>"
    return mensaje


def obtener_info_profesor(usuario_data):
    if not usuario_data or len(usuario_data) != 3:
        return "Error al obtener datos del profesor."
    
    nombre, rol, materias_str = usuario_data
    materias = [m.strip() for m in materias_str.split(",") if m.strip()]
    mensaje = "Eres profesor. Materias:<br>"
    for materia in materias:
        estudiantes = model.obtener_estudiantes(materia)
        mensaje += f"- {materia} (Estudiantes: {', '.join(estudiantes) if estudiantes else 'Ninguno'})<br>"
    return mensaje


def obtener_info_admin():
    usuarios = model.obtener_todos_los_usuarios()
    mensaje = "Usuarios registrados:<br>"
    roles = {"Estudiante": [], "Profesor": [], "Administrador": []}
    for nombre, rol in usuarios:
        roles[rol].append(nombre)
    for rol, nombres in roles.items():
        mensaje += f"<br>{rol}s:<br>"
        for nombre in nombres:
            mensaje += f"- {nombre}<br>"
    return mensaje
