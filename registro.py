import hashlib
import json
import re
import tkinter as tk
from pathlib import Path
from tkinter import messagebox

USERS_FILE = Path(__file__).with_name("usuarios.json")


def load_users() -> dict[str, dict[str, str]]:
    if not USERS_FILE.exists():
        return {}

    try:
        with USERS_FILE.open("r", encoding="utf-8") as file:
            users = json.load(file)
    except (json.JSONDecodeError, OSError):
        return {}

    return users if isinstance(users, dict) else {}


def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


def register() -> None:
    username = username_entry.get().strip()
    email = email_entry.get().strip().lower()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()

    if not username or not email or not password or not confirm_password:
        messagebox.showwarning("Datos incompletos", "Completa todos los campos.")
        return

    if not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email):
        messagebox.showwarning("Correo inválido", "Escribe un correo electrónico válido.")
        email_entry.focus_set()
        return

    if len(password) < 4:
        messagebox.showwarning("Contraseña débil", "La contraseña debe tener al menos 4 caracteres.")
        password_entry.focus_set()
        return

    if password != confirm_password:
        messagebox.showwarning("Contraseñas diferentes", "Las contraseñas no coinciden.")
        confirm_password_entry.focus_set()
        return

    users = load_users()
    if username in users:
        messagebox.showerror("Usuario existente", "Ese usuario ya está registrado.")
        username_entry.focus_set()
        return

    users[username] = {
        "email": email,
        "password": hash_password(password),
    }

    with USERS_FILE.open("w", encoding="utf-8") as file:
        json.dump(users, file, indent=2, ensure_ascii=False)

    messagebox.showinfo("Registro correcto", "La cuenta se creó correctamente.")
    clear_fields()


def clear_fields() -> None:
    username_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    confirm_password_entry.delete(0, tk.END)
    username_entry.focus_set()


window = tk.Tk()
window.title("Crear cuenta")
window.geometry("390x390")
window.resizable(False, False)
window.configure(bg="#f4f6f8")

container = tk.Frame(window, bg="#f4f6f8", padx=32, pady=24)
container.pack(fill="both", expand=True)

tk.Label(
    container,
    text="Crear cuenta",
    font=("Segoe UI", 18, "bold"),
    bg="#f4f6f8",
    fg="#1f2937",
).pack(pady=(0, 18))


def add_field(label: str, show: str = "") -> tk.Entry:
    tk.Label(container, text=label, anchor="w", bg="#f4f6f8", fg="#374151").pack(fill="x")
    entry = tk.Entry(container, show=show, font=("Segoe UI", 11))
    entry.pack(fill="x", pady=(4, 12), ipady=4)
    return entry


username_entry = add_field("Usuario")
email_entry = add_field("Correo electrónico")
password_entry = add_field("Contraseña", show="*")
confirm_password_entry = add_field("Confirmar contraseña", show="*")

buttons = tk.Frame(container, bg="#f4f6f8")
buttons.pack(fill="x", pady=(2, 0))

tk.Button(
    buttons,
    text="Registrarme",
    command=register,
    bg="#16a34a",
    fg="white",
    activebackground="#15803d",
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
window.bind("<Return>", lambda _event: register())
window.mainloop()
