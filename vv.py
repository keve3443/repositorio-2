import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def mostrar_login():
    frame_registro.pack_forget()
    frame_login.pack()

def mostrar_registro():
    frame_login.pack_forget()
    frame_registro.pack()

def login():
    user = entry_user.get()
    password = entry_password.get()
    if user == "kevin@gmail.com" and password == "1234":
        messagebox.showinfo("Bienvenido", f"Bienvenido a AGRO.MAX, {user}")
    else:
        messagebox.showerror("Error", "usuario o contraseña incorrecta")

def registrar():
    new_user = entry_new_user.get()
    new_pass = entry_new_pass.get()
    if new_user and new_pass:
        messagebox.showinfo("Registro exitoso", f"Usuario {new_user} registrado")
        mostrar_login()
    else:
        messagebox.showerror("Error", "Completa todos los campos")

root = tk.Tk()
root.title("AGRO.MAX")
root.geometry("300x400")
root.configure(bg="#195E5E")

image = Image.open("unnamed.png")
image = image.resize((100, 100))
logo = ImageTk.PhotoImage(image)
logo_label = tk.Label(root, image=logo, bg="#195E5E")
logo_label.pack(pady=10)


frame_login = tk.Frame(root, bg="#195E5E")
tk.Label(frame_login, text="AGRO.MAX", font=("Arial", 18, "bold"), fg="white", bg="#195E5E").pack(pady=10)
tk.Label(frame_login, text="Email or username", fg="white", bg="#195E5E").pack(pady=(20, 5))
entry_user = tk.Entry(frame_login, width=30)
entry_user.pack()

tk.Label(frame_login, text="Password", fg="white", bg="#195E5E").pack(pady=(20, 5))
entry_password = tk.Entry(frame_login, show="*", width=30)
entry_password.pack()

tk.Button(frame_login, text="Log In", width=25, bg="#B7CE63", command=login).pack(pady=20)
tk.Button(frame_login, text="¿No tienes cuenta? Regístrate", bg="#195E5E", fg="white", borderwidth=0, command=mostrar_registro).pack()

frame_registro = tk.Frame(root, bg="#195E5E")
tk.Label(frame_registro, text="Registro AGRO.MAX", font=("Arial", 16, "bold"), fg="white", bg="#195E5E").pack(pady=10)
tk.Label(frame_registro, text="Nuevo usuario", fg="white", bg="#195E5E").pack(pady=(20, 5))
entry_new_user = tk.Entry(frame_registro, width=30)
entry_new_user.pack()

tk.Label(frame_registro, text="Nueva contraseña", fg="white", bg="#195E5E").pack(pady=(20, 5))
entry_new_pass = tk.Entry(frame_registro, show="*", width=30)
entry_new_pass.pack()

tk.Button(frame_registro, text="Registrarse", width=25, bg="#B7CE63", command=registrar).pack(pady=20)
tk.Button(frame_registro, text="Ya tengo cuenta. Iniciar sesión", bg="#195E5E", fg="white", borderwidth=0, command=mostrar_login).pack()

frame_login.pack()

root.mainloop()