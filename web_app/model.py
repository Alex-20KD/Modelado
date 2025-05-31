from db import ConexionBD

def registrar_usuario(nombre, rol, materias):
    conexion_singleton = ConexionBD()
    conn = conexion_singleton.obtener_conexion()
    try:
        cur = conn.cursor()
        materias_str = ",".join(materias)
        cur.execute(
            """
            INSERT INTO usuarios (nombre, rol, materias) 
            VALUES (%s, %s, %s)
            ON CONFLICT (nombre) DO UPDATE SET rol=EXCLUDED.rol, materias=EXCLUDED.materias;
            """,
            (nombre, rol, materias_str)
        )
        conn.commit()
    finally:
        cur.close()
        conexion_singleton.liberar_conexion(conn)

def obtener_usuario(nombre, rol):
    conexion_singleton = ConexionBD()
    conn = conexion_singleton.obtener_conexion()
    try:
        cur = conn.cursor()
        cur.execute("SELECT nombre, rol, materias FROM usuarios WHERE LOWER(nombre) = %s AND rol = %s", (nombre.lower(), rol))
        fila = cur.fetchone()
        if fila:
            return fila  # (nombre, rol, materias)
        return None
    finally:
        cur.close()
        conexion_singleton.liberar_conexion(conn)

def obtener_profesores(materia):
    conexion_singleton = ConexionBD()
    conn = conexion_singleton.obtener_conexion()
    try:
        cur = conn.cursor()
        cur.execute("""
            SELECT nombre FROM usuarios 
            WHERE rol = 'Profesor' AND materias ILIKE %s
        """, (f'%{materia}%',))
        return [fila[0] for fila in cur.fetchall()]
    finally:
        cur.close()
        conexion_singleton.liberar_conexion(conn)

def obtener_estudiantes(materia):
    conexion_singleton = ConexionBD()
    conn = conexion_singleton.obtener_conexion()
    try:
        cur = conn.cursor()
        cur.execute("""
            SELECT nombre FROM usuarios 
            WHERE rol = 'Estudiante' AND materias ILIKE %s
        """, (f'%{materia}%',))
        return [fila[0] for fila in cur.fetchall()]
    finally:
        cur.close()
        conexion_singleton.liberar_conexion(conn)

def obtener_todos_los_usuarios():
    conexion_singleton = ConexionBD()
    conn = conexion_singleton.obtener_conexion()
    try:
        cur = conn.cursor()
        cur.execute("SELECT nombre, rol FROM usuarios")
        return cur.fetchall()
    finally:
        cur.close()
        conexion_singleton.liberar_conexion(conn)