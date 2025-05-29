# view.py
import tkinter as tk
from tkinter import messagebox
import controller

class MiniMundoEscolarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mini Mundo Escolar")
        self.root.geometry("550x450")
        self.root.configure(bg="#b1d2df")

        titulo = tk.Label(root, text="Mini Mundo Escolar", font=("Helvetica", 18, "bold"), bg="#f0f8ff", fg="#1e3d59")
        titulo.pack(pady=20)

        frame = tk.Frame(root, bg="#f0f8ff")
        frame.pack()

        tk.Label(frame, text="Nombre:", font=("Arial", 12), bg="#f0f8ff").grid(row=0, column=0, padx=10, pady=5)
        self.entry_nombre = tk.Entry(frame, font=("Arial", 12))
        self.entry_nombre.grid(row=0, column=1, pady=5)

        tk.Label(frame, text="Rol:", font=("Arial", 12), bg="#f0f8ff").grid(row=1, column=0, padx=10, pady=5)
        self.rol_var = tk.StringVar()
        roles = ["Estudiante", "Profesor", "Administrador"]
        rol_menu = tk.OptionMenu(frame, self.rol_var, *roles)
        rol_menu.grid(row=1, column=1, pady=5)

        tk.Label(frame, text="Materias (separadas por coma):", font=("Arial", 12), bg="#f0f8ff").grid(row=2, column=0, columnspan=2, padx=10, pady=5)
        self.entry_materias = tk.Entry(frame, font=("Arial", 12))
        self.entry_materias.grid(row=3, column=0, columnspan=2, pady=5, ipadx=50)

        btn_registrar = tk.Button(root, text="Registrar Usuario", command=self.registrar_usuario,
                                  bg="#4caf50", fg="white", font=("Arial", 12, "bold"))
        btn_registrar.pack(pady=10)

        btn_estudiante = tk.Button(root, text="Entrar como Estudiante", command=lambda: self.entrar_como("Estudiante"),
                                   bg="#2196f3", fg="white", font=("Arial", 12, "bold"))
        btn_estudiante.pack(pady=5)

        btn_profesor = tk.Button(root, text="Entrar como Profesor", command=lambda: self.entrar_como("Profesor"),
                                 bg="#ff9800", fg="white", font=("Arial", 12, "bold"))
        btn_profesor.pack(pady=5)

        btn_admin = tk.Button(root, text="Entrar como Administrador", command=lambda: self.entrar_como("Administrador"),
                              bg="#9c27b0", fg="white", font=("Arial", 12, "bold"))
        btn_admin.pack(pady=5)

    def registrar_usuario(self):
        nombre = self.entry_nombre.get().strip().lower()
        rol = self.rol_var.get()
        materias = [m.strip() for m in self.entry_materias.get().split(",") if m.strip()]

        exito, mensaje = controller.manejar_registro(nombre, rol, materias)
        if exito:
            messagebox.showinfo("Registro exitoso", mensaje)
            self.entry_nombre.delete(0, tk.END)
            self.entry_materias.delete(0, tk.END)
        else:
            messagebox.showwarning("Campos vacíos", mensaje)

    def entrar_como(self, rol):
        nombre = self.entry_nombre.get().strip().lower()
        usuario, error = controller.manejar_ingreso(nombre, rol)
        if error:
            messagebox.showerror("Error", error)
            return

        if rol == "Estudiante":
            info = controller.obtener_info_estudiante(usuario)
        elif rol == "Profesor":
            info = controller.obtener_info_profesor(usuario)
        elif rol == "Administrador":
            info = controller.obtener_info_admin()
        else:
            messagebox.showerror("Error", "Rol no reconocido.")
            return

        messagebox.showinfo("Información", info)