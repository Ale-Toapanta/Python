import tkinter as tk
from tkinter import messagebox

VALID_USERNAME = "admin"
VALID_PASSWORD = "1234"


def login() -> None:
    username = username_entry.get().strip()
    password = password_entry.get()

    if username == VALID_USERNAME and password == VALID_PASSWORD:
        messagebox.showinfo("Acceso correcto", f"Bienvenido, {username}.")
        password_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Acceso denegado", "Usuario o contraseña incorrectos.")
        password_entry.select_range(0, tk.END)
        password_entry.focus_set()


def clear_fields() -> None:
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    username_entry.focus_set()


window = tk.Tk()
window.title("Inicio de sesión")
window.geometry("360x250")
window.resizable(False, False)
window.configure(bg="#f4f6f8")

container = tk.Frame(window, bg="#f4f6f8", padx=32, pady=24)
container.pack(fill="both", expand=True)

tk.Label(
    container,
    text="Iniciar sesión",
    font=("Segoe UI", 18, "bold"),
    bg="#f4f6f8",
    fg="#1f2937",
).pack(pady=(0, 18))

tk.Label(container, text="Usuario", anchor="w", bg="#f4f6f8", fg="#374151").pack(fill="x")
username_entry = tk.Entry(container, font=("Segoe UI", 11))
username_entry.pack(fill="x", pady=(4, 12), ipady=4)

tk.Label(container, text="Contraseña", anchor="w", bg="#f4f6f8", fg="#374151").pack(fill="x")
password_entry = tk.Entry(container, show="*", font=("Segoe UI", 11))
password_entry.pack(fill="x", pady=(4, 16), ipady=4)

buttons = tk.Frame(container, bg="#f4f6f8")
buttons.pack(fill="x")

tk.Button(
    buttons,
    text="Entrar",
    command=login,
    bg="#2563eb",
    fg="white",
    activebackground="#1d4ed8",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    padx=12,
    pady=6,
).pack(side="left", expand=True, fill="x", padx=(0, 6))

tk.Button(
    buttons,
    text="Limpiar",
    command=clear_fields,
    relief="flat",
    cursor="hand2",
    padx=12,
    pady=6,
).pack(side="left", expand=True, fill="x", padx=(6, 0))

username_entry.focus_set()
window.bind("<Return>", lambda _event: login())
window.mainloop()
