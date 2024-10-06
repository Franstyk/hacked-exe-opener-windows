import tkinter as tk
from tkinter import filedialog, ttk
import os

def otworz_aplikacje(sciezka):
    os.startfile(sciezka)

def wyszukaj_aplikacje():
    wprowadzony_tekst = pole_wyszukiwania.get()
    menu.destroy()

    if wprowadzony_tekst:
        for subdir, dirs, files in os.walk("C:\\Program Files"):
            for file in files:
                if file.endswith(".exe") and wprowadzony_tekst.lower() in file.lower():
                    sciezka = os.path.join(subdir, file)
                    aplikacja = ttk.Button(menu, text=file, command=lambda sciezka=sciezka: otworz_aplikacje(sciezka))
                    aplikacja.pack(pady=5)

def wyswietl_menu():
    global menu
    menu = tk.Toplevel(root)
    menu.title("Lista Aplikacji")

    scrollbar = ttk.Scrollbar(menu, orient="vertical")
    scrollbar.pack(side="right", fill="y")

    canvas = tk.Canvas(menu, yscrollcommand=scrollbar.set)
    canvas.pack(side="left", fill="both", expand=True)

    scrollbar.config(command=canvas.yview)

    frame = ttk.Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor="nw")

    for subdir, dirs, files in os.walk("C:\\Program Files"):
        for file in files:
            if file.endswith(".exe"):
                sciezka = os.path.join(subdir, file)
                aplikacja = ttk.Button(frame, text=file, command=lambda sciezka=sciezka: otworz_aplikacje(sciezka))
                aplikacja.pack(pady=5)

    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

root = tk.Tk()
root.title("Otwórz")

label = tk.Label(root, text="aplikację:")
label.pack(pady=10)

button = tk.Button(root, text="MENU", command=wyswietl_menu)
button.pack(pady=10)

pole_wyszukiwania = ttk.Entry(root)
pole_wyszukiwania.pack(pady=10)

button_wyszukiwania = ttk.Button(root, text="Szukaj", command=wyszukaj_aplikacje)
button_wyszukiwania.pack(pady=10)

root.mainloop()
