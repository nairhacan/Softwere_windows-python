import tkinter as tk
from tkinter import ttk  # untuk Combobox

# Buat jendela
aplikasi = tk.Tk()
aplikasi.title("Contoh Semua Widget - Nairha")
aplikasi.geometry("600x700")

# Frame sebagai wadah layout
wadah = tk.Frame(aplikasi)
wadah.pack(pady=10)

# 1. Label
label = tk.Label(wadah, text="Halo, ini Label!", font=("Arial", 12))
label.pack()

# 2. Entry (input 1 baris)
input_nama = tk.Entry(wadah)
input_nama.pack(pady=5)

# 3. Text (input banyak baris)
input_pesan = tk.Text(wadah, height=4, width=30)
input_pesan.pack(pady=5)

# 4. Button
def kirim():
    print("Tombol diklik! Nama:", input_nama.get())

tombol = tk.Button(wadah, text="Kirim", command=kirim)
tombol.pack(pady=5)

# 5. Checkbutton
check_var = tk.BooleanVar()
check = tk.Checkbutton(wadah, text="Saya setuju", variable=check_var)
check.pack()

# 6. Radiobutton
pilihan_var = tk.StringVar()
rb1 = tk.Radiobutton(wadah, text="Laki-laki", value="L", variable=pilihan_var)
rb2 = tk.Radiobutton(wadah, text="Perempuan", value="P", variable=pilihan_var)
rb1.pack()
rb2.pack()

# 7. Listbox
listbox = tk.Listbox(wadah, height=4)
listbox.insert(1, "Python")
listbox.insert(2, "Java")
listbox.insert(3, "C++")
listbox.pack(pady=5)

# 8. Spinbox (angka naik-turun)
spin = tk.Spinbox(wadah, from_=0, to=100)
spin.pack(pady=5)

# 9. Scale (slider)
slider = tk.Scale(wadah, from_=0, to=100, orient="horizontal")
slider.pack(pady=5)

# 10. Combobox (dropdown)
combo = ttk.Combobox(wadah, values=["Bandung", "Jakarta", "Surabaya"])
combo.set("Pilih kota")
combo.pack(pady=5)

# 11. Canvas
kanvas = tk.Canvas(wadah, width=100, height=50, bg="lightblue")
kanvas.create_oval(10, 10, 90, 40, fill="red")
kanvas.pack(pady=5)

# 12. Message
pesan_panjang = tk.Message(wadah, text="Ini contoh Message panjang, seperti paragraf.", width=300)
pesan_panjang.pack(pady=5)

# 13. Menu
menu = tk.Menu(aplikasi)
aplikasi.config(menu=menu)

menu_file = tk.Menu(menu)
menu.add_cascade(label="File", menu=menu_file)
menu_file.add_command(label="Buka")
menu_file.add_separator()
menu_file.add_command(label="Keluar", command=aplikasi.quit)

# Tampilkan aplikasi
aplikasi.mainloop()
