import tkinter as tk
import onetimepad

def szyfruj_tekst():
    tekst_jawny = tekst_jawny_entry.get("1.0", "end-1c")
    szyfrogram = onetimepad.encrypt(tekst_jawny)
    szyfrogram_entry.delete("1.0", "end")
    szyfrogram_entry.insert("1.0", szyfrogram)

def deszyfruj_tekst():
    szyfrogram = szyfrogram_entry.get("1.0", "end-1c")
    tekst_jawny = onetimepad.decrypt(szyfrogram)
    tekst_jawny_entry.delete("1.0", "end")
    tekst_jawny_entry.insert("1.0", tekst_jawny)

def koniec():
    window.destroy()

def o_programie():
    tk.messagebox.showinfo("O programie", "Prosty notatnik z możliwością szyfrowania")

window = tk.Tk()
window.title("Szyfrator")
window.geometry("400x300")

# Menu
menu_bar = tk.Menu(window)
plik_menu = tk.Menu(menu_bar, tearoff=0)
plik_menu.add_command(label="Koniec", command=koniec)
menu_bar.add_cascade(label="PLIK", menu=plik_menu)

opcje_menu = tk.Menu(menu_bar, tearoff=0)
opcje_menu.add_command(label="Szyfruj", command=szyfruj_tekst)
opcje_menu.add_command(label="Deszyfruj", command=deszyfruj_tekst)
menu_bar.add_cascade(label="OPCJE", menu=opcje_menu)

menu_bar.add_command(label="O programie", command=o_programie)

window.config(menu=menu_bar)

# Interfejs użytkownika
tekst_jawny_label = tk.Label(window, text="Tekst jawny:")
tekst_jawny_label.pack()

tekst_jawny_entry = tk.Text(window, height=5, width=40)
tekst_jawny_entry.pack()

szyfrogram_label = tk.Label(window, text="Szyfrogram:")
szyfrogram_label.pack()

szyfrogram_entry = tk.Text(window, height=5, width=40)
szyfrogram_entry.pack()

szyfruj_button = tk.Button(window, text="Szyfruj", command=szyfruj_tekst)
szyfruj_button.pack()

deszyfruj_button = tk.Button(window, text="Deszyfruj", command=deszyfruj_tekst)
deszyfruj_button.pack()

window.mainloop()
