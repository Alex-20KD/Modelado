# operaciones.py
from db import conectar

def guardar_usuario(nombre, rol, materias):
    materias_str = ",".join(materias)
    with conectar() as conn:
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO usuarios (nombre, rol, materias)
            VALUES (%s, %s, %s)
            ON CONFLICT (nombre) DO UPDATE 
            SET rol = EXCLUDED.rol, materias = EXCLUDED.materias
        """, (nombre, rol, materias_str))
        conn.commit()

def obtener_usuario(nombre, rol):
    with conectar() as conn:
        cur = conn.cursor()
        cur.execute("SELECT nombre, rol, materias FROM usuarios WHERE nombre = %s AND rol = %s", (nombre, rol))
        fila = cur.fetchone()
        if fila:
            return {"nombre": fila[0], "rol": fila[1], "materias": fila[2].split(",")}
        return None

def obtener_profesores(materia):
    with conectar() as conn:
        cur = conn.cursor()
        cur.execute("SELECT nombre FROM usuarios WHERE rol = 'Profesor' AND materias ILIKE %s", (f"%{materia}%",))
        return [fila[0] for fila in cur.fetchall()]

def obtener_estudiantes(materia):
    with conectar() as conn:
        cur = conn.cursor()
        cur.execute("SELECT nombre FROM usuarios WHERE rol = 'Estudiante' AND materias ILIKE %s", (f"%{materia}%",))
        return [fila[0] for fila in cur.fetchall()]

def obtener_todos_los_usuarios():
    with conectar() as conn:
        cur = conn.cursor()
        cur.execute("SELECT nombre, rol FROM usuarios ORDER BY rol")
        return cur.fetchall()
