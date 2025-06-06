# model.py
from supabase_client import supabase

def registrar_usuario(nombre, rol, materias):
    materias_str = ",".join(materias)
    # Insertar o actualizar (no hay UPSERT directo, pero se puede simular)
    response = supabase.table("usuarios").select("*").eq("nombre", nombre).execute()
    if response.data:
        # Usuario ya existe → actualizar
        supabase.table("usuarios").update({
            "rol": rol,
            "materias": materias_str
        }).eq("nombre", nombre).execute()
    else:
        # Usuario nuevo → insertar
        supabase.table("usuarios").insert({
            "nombre": nombre,
            "rol": rol,
            "materias": materias_str
        }).execute()

def obtener_usuario(nombre, rol):
    response = supabase.table("usuarios").select("nombre, rol, materias")\
        .eq("nombre", nombre.lower()).eq("rol", rol).execute()
    if response.data:
        usuario = response.data[0]
        return (usuario["nombre"], usuario["rol"], usuario["materias"])
    return None

def obtener_profesores(materia):
    response = supabase.table("usuarios").select("nombre")\
        .eq("rol", "Profesor").like("materias", f"%{materia}%").execute()
    return [u["nombre"] for u in response.data]

def obtener_estudiantes(materia):
    response = supabase.table("usuarios").select("nombre")\
        .eq("rol", "Estudiante").like("materias", f"%{materia}%").execute()
    return [u["nombre"] for u in response.data]

def obtener_todos_los_usuarios():
    response = supabase.table("usuarios").select("nombre", "rol").execute()
    return [(u["nombre"], u["rol"]) for u in response.data]
