import tkinter as tk
from controller import registrar, entrar_como

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

btn_registrar = tk.Button(ventana, text="Registrar Usuario",
    command=lambda: registrar(entry_nombre.get(), rol_var.get(), entry_materias.get(), entry_nombre, entry_materias),
    bg="#4caf50", fg="white", font=("Arial", 12, "bold"))
btn_registrar.pack(pady=10)

btn_estudiante = tk.Button(ventana, text="Entrar como Estudiante",
    command=lambda: entrar_como(entry_nombre.get(), "Estudiante"),
    bg="#2196f3", fg="white", font=("Arial", 12, "bold"))
btn_estudiante.pack(pady=5)

btn_profesor = tk.Button(ventana, text="Entrar como Profesor",
    command=lambda: entrar_como(entry_nombre.get(), "Profesor"),
    bg="#ff9800", fg="white", font=("Arial", 12, "bold"))
btn_profesor.pack(pady=5)

btn_admin = tk.Button(ventana, text="Entrar como Administrador",
    command=lambda: entrar_como(entry_nombre.get(), "Administrador"),
    bg="#9c27b0", fg="white", font=("Arial", 12, "bold"))
btn_admin.pack(pady=5)

ventana.mainloop()