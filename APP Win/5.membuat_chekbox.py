import tkinter as tk

def tampilkan_status():
    if cek_var.get():
        hasil.config(text="Kamu menyetujui 😊")
    else:
        hasil.config(text="Kamu belum setuju 😅")

app = tk.Tk()
app.title("Checkbutton Contoh")
app.geometry("300x200")

cek_var = tk.BooleanVar()  # Variabel penyimpan status True/False
cek = tk.Checkbutton(app, text="Saya setuju", variable=cek_var)
cek.pack(pady=10)

tombol = tk.Button(app, text="Cek", command=tampilkan_status)
tombol.pack()

hasil = tk.Label(app, text="")
hasil.pack(pady=10)

app.mainloop()
