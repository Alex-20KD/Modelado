from flask import Flask, render_template, request
import controller_web

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    mensaje = ""
    if request.method == "POST":
        nombre = request.form["nombre"].strip().lower()
        rol = request.form["rol"]
        materias_str = request.form["materias"]
        materias = [m.strip() for m in materias_str.split(",") if m.strip()]
        mensaje = controller_web.manejar_registro(nombre, rol, materias)
    return render_template("index.html", mensaje=mensaje)

@app.route("/ingresar", methods=["POST"])
def ingresar():
    nombre = request.form["nombre"].strip().lower()
    rol = request.form["rol"]
    usuario, error = controller_web.manejar_ingreso(nombre, rol)

    if error:
        return render_template("resultado.html", info=error)

    if rol == "Estudiante":
        info = controller_web.obtener_info_estudiante(usuario)
    elif rol == "Profesor":
        info = controller_web.obtener_info_profesor(usuario)
    elif rol == "Administrador":
        info = controller_web.obtener_info_admin()
    else:
        info = "Rol no reconocido."

    return render_template("resultado.html", info=info)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)  