# model.py
from db import conectar  # db.py debe tener la función de conexión con PostgreSQL

def registrar_usuario(nombre, rol, materias):
    with conectar() as conn:
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO usuarios (nombre, rol, materias)
            VALUES (%s, %s, %s)
            ON CONFLICT (nombre) DO UPDATE SET rol = EXCLUDED.rol, materias = EXCLUDED.materias;
        """, (nombre.lower(), rol, ",".join(materias)))
        conn.commit()

def obtener_usuario(nombre, rol):
    with conectar() as conn:
        cur = conn.cursor()
        cur.execute("""
            SELECT nombre, rol, materias FROM usuarios
            WHERE LOWER(nombre) = %s AND rol = %s;
        """, (nombre.lower(), rol))
        return cur.fetchone()

def obtener_profesores(materia):
    with conectar() as conn:
        cur = conn.cursor()
        cur.execute("""
            SELECT nombre FROM usuarios
            WHERE rol = 'Profesor' AND materias ILIKE %s;
        """, (f"%{materia}%",))
        return [fila[0] for fila in cur.fetchall()]

def obtener_estudiantes(materia):
    with conectar() as conn:
        cur = conn.cursor()
        cur.execute("""
            SELECT nombre FROM usuarios
            WHERE rol = 'Estudiante' AND materias ILIKE %s;
        """, (f"%{materia}%",))
        return [fila[0] for fila in cur.fetchall()]

def obtener_todos_los_usuarios():
    with conectar() as conn:
        cur = conn.cursor()
        cur.execute("SELECT nombre, rol FROM usuarios;")
        return cur.fetchall()